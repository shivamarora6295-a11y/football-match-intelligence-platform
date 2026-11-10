-- =====================================================
-- Team Performance View
-- =====================================================

DROP VIEW IF EXISTS vw_team_performance;

CREATE VIEW vw_team_performance AS
SELECT
    home_team,
    COUNT(*) AS matches_played,
    SUM(home_score) AS goals_scored,
    ROUND(AVG(home_score),2) AS avg_goals
FROM raw_match_results
GROUP BY home_team;


-- =====================================================
-- Tournament Analysis View
-- =====================================================

DROP VIEW IF EXISTS vw_tournament_analysis;

CREATE VIEW vw_tournament_analysis AS
SELECT
    tournament,
    COUNT(*) AS matches_played,
    SUM(home_score + away_score) AS total_goals
FROM raw_match_results
GROUP BY tournament;


-- =====================================================
-- Country Analysis View
-- =====================================================

DROP VIEW IF EXISTS vw_country_analysis;

CREATE VIEW vw_country_analysis AS
SELECT
    country,
    COUNT(*) AS matches_hosted
FROM raw_match_results
GROUP BY country;