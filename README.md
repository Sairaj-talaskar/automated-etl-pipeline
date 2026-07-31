# ⚙️ Automated ETL (Extract, Transform, Load) Pipeline

## 📌 Project Overview
This project features a custom-built, automated ETL pipeline designed to streamline the flow of data and digital assets between various platforms. By replacing manual data extraction and formatting with scheduled Python scripts, this pipeline ensures that clean, structured data is consistently available for downstream analytics, reporting, and operational workflows.

## 🎯 Objectives
* **Automation:** Eliminate manual data entry and file handling by scheduling automated script executions.
* **API Integration:** Seamlessly connect discrete platforms (e.g., Google Drive APIs, external analytics platforms, and databases) to establish a unified data flow.
* **Data Transformation:** Cleanse, reformat, and validate raw data streams to ensure high accuracy and consistency.
* **Scalability:** Build a modular architecture that allows for easy addition of new data sources or destination endpoints.

## 🛠️ Tech Stack
* **Programming Language:** Python
* **Data Processing:** Pandas, NumPy
* **Integration & Web:** RESTful APIs, JSON, `requests` library
* **Authentication:** OAuth 2.0 (for secure API access)
* **Database:** SQL (for staging and loading processed data)
* **Task Scheduling:** Cron Jobs / Windows Task Scheduler

## 🔄 Pipeline Architecture (The ETL Process)
1. **Extract (E):** The script securely authenticates and pulls raw data/assets from source APIs (such as extracting scheduled content assets and metadata from Google Drive).
2. **Transform (T):** Python handles the core logic—parsing JSON responses, handling missing values, standardizing date/time formats, and restructuring the data into analytical tables.
3. **Load (L):** The cleaned and structured data is automatically pushed into a centralized SQL database or exported as formatted CSV/Excel reports, ready to be ingested by Business Intelligence dashboards.

## 💡 Results & Business Impact
* **Time Efficiency:** Reduced hours of manual weekly data aggregation down to a script execution time of seconds.
* **Error Reduction:** Minimized human error in data entry, ensuring high data integrity for business reporting.
* **Analytics Readiness:** Provided a reliable foundation of structured data, allowing analysts to focus strictly on generating insights rather than cleaning datasets.

## 🚀 How to Run the Project
1. Clone the repository: `git clone https://github.com/Sairaj-talaskar/automated-etl-pipeline.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your environment variables: Create a `.env` file and add your specific API Keys and Database URIs.
4. (Optional) Review the `config.json` file to modify source endpoints and target destinations.
5. Execute the main pipeline script: `python main_pipeline.py`
