# RUNME: Auto‑Geospatial Accelerator

This repository builds an end‑to‑end ingestion pipeline for combining multiple datasets and a pipeline to train a collision‑prediction ML model using hyperparameter tuning and traffic‑volume data with AutoML. You’ll also get a sample dashboard and app. All assets are easilly deployable via our Databricks Asset Bundle (DAB) file.

You may work with this repo's assets on a Databricks Workspace or locally in an IDE like VS Code.

---

## 1. Prerequisites (local development )

1. **Git**  
   ```bash
   git clone https://github.com/<your‑org>/automotive‑geospatial‑accelerator.git
   cd automotive‑geospatial‑accelerator
   ```

2. **Python libs**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Databricks CLI**  
   ```bash
   pip install databricks-cli
   databricks configure --token 
   ```

## 2. Configure

Open `Config.ipynb` (or inspect the first code cell) and set:

```python
catalog_name = "auto_geospatial"      # Catalog name
schema_name  = "default_v1"           # Schema Name
volume_name  = "data"                 # UC volume for raw/staged files
```

---

## 3. Deploy the Asset Bundle

All clusters, jobs, and dashboard definitions live in `databricks.yml` under the `auto-geospatial-bundle`. Push and deploy:

```bash

# deploy bundle
databricks bundles deploy   --environment dev   --bundle auto-geospatial-bundle
```

This creates:
- **Clusters**:  
  - `auto-geospatial-ml-cluster` (Photon, autoscale 1–2 workers)  
- **Job Tasks**:  
  1. `ingestion-job` → runs `1-Data Ingestion.ipynb`  
  2. `run-model-training-job` → runs `2-Model Training.ipynb` after ingestion  
- **Dashboard**:  
  - `Collision Analytics` from `3-Collision Analytics.lvdash.json`
- **App**:  
  - `Collision Analytics App` from `./app`

---

## 4. Run the Pipelines

1. **Ingestion**  
   - In Databricks UI → **Workflows → Auto Geospatial Ingestion and ML Training Job** → **Run now**  
2. **Training**  
   - Training task triggers automatically when ingestion task succeeds.  
3. **Monitor**  
   - Check the **Spark UI** for stages, task skew, shuffle partitions.  
   - Use `.repartition()` or `.coalesce()` in notebooks to tune parallelism.

---

## 5. Verify Outputs

In a SQL notebook or the Databricks SQL Editor:

```sql
USE CATALOG auto_geospatial;
USE SCHEMA default_v1;

-- list your new tables
SHOW TABLES;
-- spot‑check data
SELECT * FROM trip_analytics_synthesis_gold LIMIT 10;
```

Your ML model will be registered in **MLflow** under the same catalog/schema by default.

---

## 6. Import & Explore the Dashboard

The bundle deploy creates the dashboard for you, but you can also import manually:

```bash
databricks workspace import   3-Collision\ Analytics.lvdash.json   /Users/<you>/dashboards/Collision\ Analytics   --json
```

Open it, and explore filters on borough, date, contributing factors, traffic vs. collisions, telematics patterns, etc.

---

## 7. Configure the Genie‑Backed App (Optional)

1. **Create a Genie Space**  
   In the Databricks UI, go to **Genie → New**, name it `collision‑analytics‑app`, and click **Create**.

2. **Add the synthesis table**  
   Within your new Genie Space, click **Configure → Data → Add** and select `trip_analytics_synthesis_gold`.

3. **Update the app configuration**  
   In the app folder, open `app.yaml`, and set:  
   - `DATABRICKS_GENIE_ROOM_ID` to the ID of the Genie Space from step 1  
   - `DATABRICKS_DASHBOARD_ID` to your Collision Analytics dashboard ID

4. **Redeploy the bundle**  
   Un-comment the apps section of the bundle file (`databricks.yml`)
   Run your deployment command again (e.g., `databricks bundles deploy`) to apply these changes.  



---


# You’re ready!  

Run “ingestion-job”, watch “run-model-training-job” finish, then dive into collision insights in the dashboard.

Happy building! 🎉
