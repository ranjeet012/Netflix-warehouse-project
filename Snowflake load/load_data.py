import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
df = pd.read_csv(
    "C:/netflix_warehouse_project/data/netflix_titles.csv"
)

print(df.head())

# Snowflake connection details
user = "RANJEET2222PAL2"
password = quote_plus("Ranjeetpal@143m")
account = "WLIWIVH-HW57459"
warehouse = "COMPUTE_WH"
database = "NETFLIX_WAREHOUSE"
schema = "PUBLIC"

# Create Snowflake engine
engine = create_engine(
    f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
)
with engine.connect() as conn:
    result = conn.execute(text("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()"))
    print(result.fetchall())
# Load data
df.to_sql(
    "NETFLIX_STAGING",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into Snowflake")