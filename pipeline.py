import pandas as pd
import glob
import os
import logging

# Setup a log file to track when the automation runs
logging.basicConfig(
    filename='pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def run_etl_pipeline():
    logging.info("Pipeline execution started.")
    
    # 1. EXTRACT: Find and load all monthly CSVs from the folder
    file_paths = glob.glob("raw_data/*.csv")
    if not file_paths:
        print("Error: No CSV files found in the 'raw_data' folder.")
        return

    df_list = [pd.read_csv(file) for file in file_paths]
    df = pd.concat(df_list, ignore_index=True)
    logging.info(f"Successfully merged {len(file_paths)} files.")

    # 2. TRANSFORM: Clean the data and calculate metrics
    df = df.dropna(how='all')  # Drop completely empty rows
    df = df[df['Order Date'] != 'Order Date']  # Remove stray header rows
    
    # Convert data types for calculations
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    
    # Engineer a new column
    df['Total_Sales'] = df['Quantity Ordered'] * df['Price Each']
    logging.info("Data cleaned and transformed.")

    # 3. LOAD: Generate a master summary report
    os.makedirs("output", exist_ok=True)
    
    summary = df.groupby('Product')['Total_Sales'].sum().reset_index()
    summary = summary.sort_values(by='Total_Sales', ascending=False)
    
    output_path = "output/yearly_product_sales_summary.csv"
    summary.to_csv(output_path, index=False)
    
    logging.info("Pipeline execution finished successfully.")
    print(f"Pipeline ran successfully. Master report saved to '{output_path}'.")

if __name__ == "__main__":
    run_etl_pipeline()