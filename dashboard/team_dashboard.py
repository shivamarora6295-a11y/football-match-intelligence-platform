import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# PostgreSQL Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Hello%40123@localhost:5432/Football_DB"
)

# =========================
# KPI Queries
# =========================

total_matches = pd.read_sql(
    "SELECT COUNT(*) cnt FROM raw_match_results",
    engine
).iloc[0]["cnt"]

total_goals = pd.read_sql(
    """
    SELECT SUM(home_score + away_score) goals
    FROM raw_match_results
    """,
    engine
).iloc[0]["goals"]

total_teams = pd.read_sql(
    """
    SELECT COUNT(*) cnt
    FROM dim_team
    """,
    engine
).iloc[0]["cnt"]

total_countries = pd.read_sql(
    """
    SELECT COUNT(DISTINCT country) cnt
    FROM raw_match_results
    """,
    engine
).iloc[0]["cnt"]

# =========================
# Dashboard Header
# =========================

st.title("⚽ Football Match Intelligence Platform")

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

col1.metric("Matches", f"{total_matches:,}")
col2.metric("Goals", f"{total_goals:,}")
col3.metric("Teams", f"{total_teams:,}")
col4.metric("Countries", f"{total_countries:,}")

# =========================
# Team Performance
# =========================

team_df = pd.read_sql(
    """
    SELECT *
    FROM vw_team_performance
    ORDER BY goals_scored DESC
    LIMIT 10
    """,
    engine
)

st.subheader("Top 10 Scoring Teams")

fig1 = px.bar(
    team_df,
    x="home_team",
    y="goals_scored",
    color="goals_scored",
    title="Top Scoring Teams"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# Tournament Analysis
# =========================

tournament_df = pd.read_sql(
    """
    SELECT *
    FROM vw_tournament_analysis
    ORDER BY matches_played DESC
    LIMIT 10
    """,
    engine
)

st.subheader("Top Tournaments")

fig2 = px.bar(
    tournament_df,
    x="tournament",
    y="matches_played",
    color="matches_played",
    title="Most Played Tournaments"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# Country Analysis
# =========================

country_df = pd.read_sql(
    """
    SELECT *
    FROM vw_country_analysis
    ORDER BY matches_hosted DESC
    LIMIT 10
    """,
    engine
)

st.subheader("Top Hosting Countries")

fig3 = px.bar(
    country_df,
    x="country",
    y="matches_hosted",
    color="matches_hosted",
    title="Countries Hosting Most Matches"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# Data Preview
# =========================

st.subheader("Team Performance Data")

st.dataframe(team_df)