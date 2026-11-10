DROP VIEW IF EXISTS vw_team_performance;

CREATE VIEW vw_team_performance AS
SELECT
    home_team,
    COUNT(*) AS matches_played,
    SUM(home_score) AS goals_scored,
    ROUND(AVG(home_score),2) AS avg_goals
FROM raw_match_results
GROUP BY home_team;