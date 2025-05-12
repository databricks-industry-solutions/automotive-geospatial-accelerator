import os
import time
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.components.v1 import html, components
import folium
from branca.colormap import linear
from folium.features import GeoJsonTooltip
from databricks.sdk import WorkspaceClient


workspace_client = WorkspaceClient()

# --- ENV CONFIG ---
GENIE_ROOM_ID = os.getenv('DATABRICKS_GENIE_ROOM_ID', '01f02ec9fa6214918284618c1d04c9fa') 
WORKSPACE_URL = workspace_client.config.host
GENIE_URL = f"{WORKSPACE_URL}/genie/rooms/{GENIE_ROOM_ID}"
DASHBOARD_ID = os.getenv('DATABRICKS_DASHBOARD_ID', '01f0217063f418458606ec631d3c5c31')

DASHBOARD_URL = f"{WORKSPACE_URL}/embed/dashboardsv3/{DASHBOARD_ID}"


# --- GENIE QUERY FUNCTION ---
def run_genie_query(prompt):
    try:

        start_conv_url = f"/api/2.0/genie/spaces/{GENIE_ROOM_ID}/start-conversation"
        response = workspace_client.api_client.do("POST", start_conv_url, headers={"Content-Type": "application/json"}, body={"content": "Init"})
        conversation_id = response["conversation_id"]

        create_msg_url = f"/api/2.0/genie/spaces/{GENIE_ROOM_ID}/conversations/{conversation_id}/messages"
        response = workspace_client.api_client.do("POST", create_msg_url, headers={"Content-Type": "application/json"}, body={"content": prompt})
        message_id = response["message_id"]

        get_msg_url = f"/api/2.0/genie/spaces/{GENIE_ROOM_ID}/conversations/{conversation_id}/messages/{message_id}"
        status = "ASKING_AI"
        retries = 0
        while status == "ASKING_AI" and retries < 100:
            time.sleep(5)
            response = workspace_client.api_client.do("GET", get_msg_url, headers={"Content-Type": "application/json"})
            status = response.get("status")
            retries += 1

        statement_id = response.get("query_result", {}).get("statement_id")
        if not statement_id:
            return pd.DataFrame(), "No statement ID returned."

        get_result_url = f"/api/2.0/sql/statements/{statement_id}"
        result_json = workspace_client.api_client.do("GET", get_result_url, headers={"Content-Type": "application/json"})

        schema = result_json.get("manifest", {}).get("schema", {}).get("columns", [])
        columns = [col.get("name", f"col_{i}") for i, col in enumerate(schema)]
        data = result_json.get("result", {}).get("data_array", [])

        return pd.DataFrame(data, columns=columns), "Query successful."
    except Exception as e:
        
        print(f"Error: {str(e)}")
        return pd.DataFrame(), f"Error: {str(e)}"

# --- STREAMLIT UI ---

st.set_page_config(page_title="AutoBricks Collision Analytics", layout="wide", page_icon="🏎️")

#tab1, tab2 = st.tabs(["Ask Your Own Question", "Dashboard View"])

# Get query string parameters
query_params = st.query_params
debug_mode = query_params.get("debug", "false").lower()

# Conditionally hide the top-right menu
if debug_mode == "false":
    st.markdown("""
    <style>
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

#Loader style
st.markdown("""
    <style>
        #custom-loader {
            position: fixed;
            top: 200px; left: 0;
            width: 100%; height: 100%;
            z-index: 9999;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

#App Header    
st.markdown(f"""
    <div style='display: flex; justify-content: space-between; margin-top: -100px;'>
        <div style='font-size: 2em; font-weight: bold;'>AutoBricks</div>
        <div style='text-align: right;'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Ali_Ghodsi.jpg" width="48" style="border-radius: 50%; vertical-align: middle; margin-right: 10px;"/>
            <span style='vertical-align: middle;'>Ali G<br/><small>VP of Vehicle Software</small></span>
        </div>
    </div>
    <h1 style='text-align: center;'>Collision Geospatial Analytics</h1>
    <p style='text-align: center;'>Use these example prompts below.</a></p>
    <p style='text-align: center;'><a href="{GENIE_URL}" target="_blank">Or ask your own questions</a></p>
""", unsafe_allow_html=True)


# App Buttons
PROMPTS = [
    "What are the most common contributing factors to collisions?",
    "Are collisions more or less likely to occur when there is predicipitation?",
    "How does collision frequency change with varying traffic volume throughout the day?",
    "How does collision severity correlate with traffic volume during peak hours?",
    "What telematics patterns (e.g., sudden braking, speeding) are most predictive of collision risk?"
]

buttons = [
    "🌍 Top Collision Factors",
    "🧭 Precipitation Impact on Collision Frequency",
    "🚦 Collision Frequency vs Traffic Volume",
    "📊 Collision Severity vs Traffic Volume",
    "📡 Telematics-Driven Collision Insights"
]


st.markdown("""
    <style>
    div.stButton > button {
        height: 80px !important;
        width: 200px !important;
        display: block;
        font-size: 0.85em;
        white-space: normal;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZATION ---
if "selected_prompt" not in st.session_state:
    st.session_state.selected_prompt = None; #PROMPTS[0]  # default to first prompt'''

if "just_clicked" not in st.session_state:
    st.session_state.just_clicked = None

# Render buttons in columns
cols = st.columns(len(buttons))
for i, label in enumerate(buttons):
    with cols[i]:
        is_selected = st.session_state.selected_prompt == PROMPTS[i]
        if st.button(label, type="primary" if is_selected else "secondary", use_container_width=True):
            st.session_state.just_clicked = PROMPTS[i]

# Update selected_prompt after the loop to trigger correct styles
if st.session_state.just_clicked:
    st.session_state.selected_prompt = st.session_state.just_clicked
    st.session_state.just_clicked = None
    st.rerun()

       
# --- RUN QUERY IF SOMETHING IS SELECTED ---
selected = st.session_state.selected_prompt
if selected:
        # Show the loader overlay
    loader = st.empty()
    loader.markdown('<div id="custom-loader">🔄 Running query, please wait...</div>', unsafe_allow_html=True)

    try:
        df, msg = run_genie_query(selected)
        
        #TODO: Add a map and better visualizations - for now just show the dataframe
        
        st.dataframe(df, use_container_width=True)
        
        
        loader.empty()  # Remove the loader

    except Exception as e:
        st.error(f"Error: {str(e)}")
        loader.markdown('<div id="custom-loader">⚠️ Error loading. Please try again.</div>', unsafe_allow_html=True)

st.components.v1.iframe(DASHBOARD_URL,
                        height=800)
