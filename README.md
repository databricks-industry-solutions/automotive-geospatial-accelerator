<img src=https://raw.githubusercontent.com/databricks-industry-solutions/.github/main/profile/solacc_logo.png width="600px">

[![DBR](https://img.shields.io/badge/DBR-CHANGE_ME-red?logo=databricks&style=for-the-badge)](https://docs.databricks.com/release-notes/runtime/CHANGE_ME.html)
[![CLOUD](https://img.shields.io/badge/CLOUD-CHANGE_ME-blue?logo=googlecloud&style=for-the-badge)](https://databricks.com/try-databricks)

## Business Problem
Geospatial data is rich, complex, nuanced, and is integral to many businesses, especially the automotive industry. With its high velocity, complex representations, and time-bound nature, unlocking its full value requires a high performance platform. 

This Solution Accelerator helps organizations harness real-time geospatial, telematics, and sensor data. The key use cases include primarily road safety and risk prevention; future releases will include smart mobility, EV infrastructure optimization, and driving-based insurance.

These geospatial analytics and AI capabilities on Databricks allow companies to achieve improvements up to 30% in fleet efficiency, reduce infrastructure costs by up to 25%, and enable better road safety by decreasing accident rates by up to 20%.


## Reference Architecture

The content in this repository builds an end-to-end ingestion pipeline for combining multiple datasets and a pipeline to train a collision prediction ML model using hyperparameter tuning and traffic‑volume data with AutoML. We also provide a sample dashboard and a Databricks App. Everything can be quickly deployed using the provided Databricks Asset Bundle files (DAB).


![Auto Geospatial Reference Architecture](auto-geospatial-ref-architecture.png)

## Authors
- [Eumar Assis](mailto:eumar.assis@databricks.com)
- [Himanshu Gupta](mailto:himanshu.gupta@databricks.com)
- [Andres Urrutia](mailto:andres.urrutia@databricks.com)
- [Michael Johns](mailto:mjohns@databricks.com)
- [Varun Mahajan](mailto:varun.mahajan@databricks.com)
- [Eric Lind](mailto:eric.lind@databricks.com)
- [Fareed Aref](mailto:fareed.aref@databricks.com)
- [Zachary Ryan](mailto:zachary.ryan@databricks.com)
  
## Project support 

Please note the code in this project is provided for your exploration only, and are not formally supported by Databricks with Service Level Agreements (SLAs). They are provided AS-IS and we do not make any guarantees of any kind. Please do not submit a support ticket relating to any issues arising from the use of these projects. The source in this project is provided subject to the Databricks [License](./LICENSE.md). All included or referenced third party libraries are subject to the licenses set forth below.

Any issues discovered through the use of this project should be filed as GitHub Issues on the Repo. They will be reviewed as time permits, but there are no formal SLAs for support. 

## License

&copy; 2024 Databricks, Inc. All rights reserved. The source in this notebook is provided subject to the Databricks License [https://databricks.com/db-license-source].  All included or referenced third party libraries are subject to the licenses set forth below.

| library                | description                                                   | license                   | source                                             |
|------------------------|---------------------------------------------------------------|---------------------------|----------------------------------------------------|
| branca                 | HTML colormap library for leaflet.js                          | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/branca)            |
| databricks-sdk         | Databricks SDK for interacting with the Databricks REST APIs  | Apache 2.0                | [PyPI](https://pypi.org/project/databricks-sdk)    |
| folium                 | Python wrapper for leaflet.js maps                            | MIT License               | [PyPI](https://pypi.org/project/folium)            |
| geopandas              | Pandas support for geospatial data                            | BSD License               | [PyPI](https://pypi.org/project/geopandas)         |
| jmespath               | JSON matching & extraction library                            | MIT License               | [PyPI](https://pypi.org/project/jmespath)          |
| keplergl               | Python wrapper for kepler.gl interactive maps                 | MIT License               | [PyPI](https://pypi.org/project/keplergl)          |
| matplotlib             | Comprehensive library for static & interactive visualizations | PSF License               | [PyPI](https://pypi.org/project/matplotlib)        |
| matplotlib-inline      | Matplotlib inline backend for Jupyter notebooks               | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/matplotlib-inline) |
| mermaid-python         | Generate Mermaid diagrams from Python                         | MIT License               | [PyPI](https://pypi.org/project/mermaid-python)    |
| networkx               | Graph creation, manipulation, and study of networks           | BSD License               | [PyPI](https://pypi.org/project/networkx)          |
| nbformat               | Jupyter notebook format APIs                                  | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/nbformat)          |
| numpy                  | Fundamental package for scientific computing                  | BSD License               | [PyPI](https://pypi.org/project/numpy)             |
| openmeteo-requests     | Python client for the Open‑Meteo weather API                  | MIT License               | [PyPI](https://pypi.org/project/openmeteo-requests) |
| osmnx                  | Retrieve, model, analyze & visualize OSM networks             | MIT License               | [PyPI](https://pypi.org/project/osmnx)             |
| pandas                 | Data structures & data analysis tools                         | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/pandas)            |
| pgeocode               | Postal code geocoding library                                 | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/pgeocode)          |
| plotly                 | Interactive plotting library for Python                       | MIT License               | [PyPI](https://pypi.org/project/plotly)            |
| pyparsing              | Text parsing toolkit                                          | MIT License               | [PyPI](https://pypi.org/project/pyparsing)         |
| requests-cache         | Persistent caching for `requests` HTTP library                | BSD 2‑Clause License      | [PyPI](https://pypi.org/project/requests-cache)    |
| retry-requests         | Automatic retry logic for `requests` HTTP calls               | MIT License               | [PyPI](https://pypi.org/project/retry-requests)    |
| scikit-learn           | Machine learning in Python                                    | BSD 3‑Clause License      | [PyPI](https://pypi.org/project/scikit-learn)      |
| seaborn                | Statistical data visualization                                | BSD License               | [PyPI](https://pypi.org/project/seaborn)           |
| streamlit              | Framework for building interactive data apps in Python        | Apache 2.0                | [PyPI](https://pypi.org/project/streamlit)         |