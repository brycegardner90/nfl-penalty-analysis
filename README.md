🏈 NFL Penalty Bias Analysis (2016–2025)
Project 2 of 5 | Tools: Python · SQL · Power BI

The Origin Story
A friend of mine — shoutout to Vyredrac — is a Detroit Lions fan. And like most Lions fans, he has a theory. Armed with YouTube highlight reels and the unshakeable confidence of someone who has watched their team suffer for decades, he insisted that Detroit gets more blown calls than any other team in the NFL.
I could have just disagreed. Instead, I spent a significant number of hours building a multi-source data pipeline, writing Python scripts, querying SQLite databases, and building a three-page Power BI dashboard to find out.
This is that project.

The Question

Do certain NFL teams consistently receive more game-altering penalties than others — and does the data support the Detroit Lions' reputation as the most officiated-against team in the league?


What I Found
Short answer: Vyredrac is wrong. Detroit finished within 50 penalty yards of neutral officiating in 8 of the last 10 seasons. They are about as middle-of-the-road as it gets.
But the data told a much more interesting story along the way.
Key Findings

🔴 New Orleans Saints are the most consistently penalized team over the last 10 seasons — not Detroit. They finished negative in nearly every season, bottoming out at nearly -400 net penalty yards in 2020 alone.
🟢 Indianapolis Colts and Cincinnati Bengals benefited most from officiating over the same period — consistently on the positive side of the ledger.
🏠 San Francisco 49ers get penalized the most heavily on the road compared to at home — the largest home/away split in the league. Meanwhile Philadelphia gets called more at home than anywhere else.
😲 Kansas City Chiefs — arguably the most complained-about team for "getting all the calls" — sit almost perfectly neutral in the data. The narrative and the numbers don't match.
📊 Defensive Pass Interference is by far the most called penalty leaguewide with 2,838 accepted calls over 10 seasons — nearly double the next most common penalty type.
⚠️ Detroit's one bad year: 2024 was genuinely their worst officiated season at -131 net yards. So Vyredrac gets partial credit for the timing of his argument.


Dashboard Preview
Page 1 — Team Differentials
Net penalty yard differential across all 32 teams + home vs away breakdown
Show Image
Page 2 — Season by Season Trend
Interactive line chart with team slicer — track any team's officiating trend across 10 seasons
Show Image
Page 3 — Deep Dive Analysis
Penalty type breakdown by team + high leverage 4th quarter analysis + Lions spotlight
Show Image

Data Sources
SourceDescriptionSeasonsNFLPenalties.comSeason-level penalty summary by team — against count, beneficiary count, net yards, home/away splits2016–2025nflverse (nflfastR)Play-by-play data — every penalty play with quarter, score differential, win probability, and penalty type2016–2025

Tools & Tech Stack
ToolPurposePython (pandas)Data cleaning, combining 10 seasons of play-by-play CSVs, franchise relocation fixes (OAK→LV, SD→LAC)SQLite / DB BrowserData transformation, aggregation, and query buildingPower BI DesktopInteractive dashboard — 3 pages, 6 visualizations, conditional formatting, slicersGoogle SheetsManual data collection from NFLPenalties.com across 10 seasons

Project Structure
NFL Penalties Project/
│
├── nfl_penalty_prep.py          # Python script — cleans and combines raw nflverse CSVs
├── nfl_bias_penalty_project.pbix  # Power BI dashboard file
├── nfl_penalties.sqbpro         # SQLite database with both tables and saved queries
│
├── CSV Files/
│   ├── nflverse raw files/      # Raw play-by-play CSVs (2016–2025)
│   ├── nfl_penalties_combined.csv  # Python output — cleaned play-by-play penalties
│   ├── PowerBI_CSV/             # Exported query results for Power BI
│       ├── query1_net_differential.csv
│       ├── query2_season_trend.csv
│       ├── query3_lions_spotlight.csv
│       ├── query4_high_leverage.csv
│       ├── query5_penalty_types.csv
│       └── query6_home_away.csv
│
└── PNG Files/
    ├── TeamDifferential.png
    ├── SeasonBySeasonTrend.png
    └── Deep Dive.png

SQL Highlights
Six queries power this analysis. A sample:
Net Penalty Differential by Team (All 10 Years)
sqlSELECT 
    Team,
    SUM("Against Count") AS total_against,
    SUM("Beneficiary Count") AS total_beneficiary,
    SUM("Net Count") AS total_net_count,
    SUM("Net Yards") AS total_net_yards,
    COUNT(Season) AS seasons
FROM nfl_penalties_32_teams
GROUP BY Team
ORDER BY total_net_yards ASC;
High Leverage Penalties — 4th Quarter, Within 8 Points
sqlSELECT
    season,
    penalty_team,
    penalty_type,
    COUNT(*) AS penalty_count,
    SUM(penalty_yards) AS total_yards
FROM play_by_play_combined
WHERE qtr = 4
    AND ABS(score_differential) <= 8
    AND penalty = 1.0
GROUP BY season, penalty_team, penalty_type
ORDER BY penalty_count DESC;

Python Script
The nfl_penalty_prep.py script handles all raw data processing:

Loops through 10 seasons of nflverse play-by-play CSVs
Filters to accepted penalty plays only
Keeps only the 15 relevant columns out of 370+
Fixes franchise relocations (Oakland → Las Vegas, San Diego → LA Chargers)
Outputs one clean combined CSV ready for SQL

This was my first Python script — written and executed as part of building this project from scratch.

Methodology Notes

"Blown call" proxy: There is no official NFL blown call database. This analysis uses accepted penalty differentials as a proxy — specifically net penalty yards (penalties against minus penalties drawn). This is an intentional simplification in service of using clean, verifiable data.
Franchise relocations: Oakland Raiders data is merged with Las Vegas Raiders. San Diego Chargers data is merged with LA Chargers. No teams were added to the league in the 2016–2025 window.
Declined and offsetting penalties are excluded from all counts per NFLPenalties.com methodology.
High leverage definition: 4th quarter plays with a score differential of 8 points or fewer (one possession game).


About This Project
This is Project 2 of 5 in my data analytics portfolio. Each project is designed to demonstrate a different combination of tools and analytical approaches.
ProjectTopicToolsProject 1Video Game Sales AnalysisSQL · Power BIProject 2NFL Penalty Bias AnalysisPython · SQL · Power BIProjects 3–5Coming SoonTableau · Python · and more

Connect
GitHub: brycegardner90
LinkedIn: Bryce Gardner

Built because a friend had a take. The data had other plans.
