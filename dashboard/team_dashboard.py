import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# PostgreSQL Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Hello%40123@localhost:5432/Football_DB"
)

# Query
query = """
SELECT *
FROM vw_team_performance
ORDER BY goals_scored DESC
LIMIT 10
"""

df = pd.read_sql(query, engine)

# Dashboard Title
st.title("⚽ Football Match Intelligence Platform")

st.subheader("Top 10 Scoring Teams")

# Chart
fig = px.bar(
    df,
    x="home_team",
    y="goals_scored",
    color="goals_scored",
    title="Top 10 Scoring Teams"
)

st.plotly_chart(fig)

# Data Grid
st.dataframe(df)