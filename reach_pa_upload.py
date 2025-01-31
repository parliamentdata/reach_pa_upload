import yaml
import pandas as pd
from sqlalchemy import create_engine

# Load the downloaded Excel file
excel_path = "data/input/participation_agreement_status.xlsx"
data = pd.read_excel(excel_path)

# Select specified columns
data_subset = data[['rcdts', 'date']]

# Convert 'date' column to datetime
data_subset['date'] = pd.to_datetime(data_subset['date'])

# Sort by 'rcdts' and 'date' to ensure the oldest row comes first
data_subset = data_subset.sort_values(by=['rcdts', 'date'])

# Remove duplicates based on 'rcdts', keeping the first (oldest) row
data_subset = data_subset.drop_duplicates(subset=['rcdts'], keep='first')

# Reformat 'date' column as mm/dd/yyyy for SQL upload
data_subset['date'] = data_subset['date'].dt.strftime('%m/%d/%Y')

# Path to your config.yml file
config_file_path = "../utility/config.yml"

# Read the YAML configuration
with open(config_file_path, 'r') as file:
    config = yaml.safe_load(file)

# Extract the connection arguments from the config
conn_args = config['rssi-data-warehouse']['dataconnection']

# Format the connection string for SQLAlchemy
db_url = f"postgresql+psycopg2://{conn_args['uid']}:{conn_args['pwd']}@{conn_args['server']}:{conn_args['port']}/{conn_args['database']}"

# Create the engine
engine = create_engine(db_url)

# Upload the DataFrame to a new table in the RSSI data warehouse
table_name = "participation_agreement_status"
data_subset.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Data successfully uploaded to the table {table_name} in the RSSI data warehouse.")
