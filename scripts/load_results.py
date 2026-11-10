import pandas as pd
from sqlalchemy import create_engine

path = r"C:\Football_AI_Project\datasets\datasets\martj42\international-football-results-from-1872-to-2017\versions\138"

df = pd.read_csv(path + r"\results.csv")

engine = create_engine(
    "postgresql+psycopg2://postgres:Jhakas%402412@localhost:5432/Football_DB"
)

df.to_sql(
    "raw_match_results",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")