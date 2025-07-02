import streamlit as st
import pandas as pd
from collections import defaultdict
from utils import load_data

st.set_page_config(page_title="Leaderboard", layout="centered")

st.title("🏆 Tournament Leaderboard")

# data = load_data()
# matches = data.get("matches", [])
# teams = data.get("teams", [])
# all_team_names = [t["name"] for t in teams]

# if not matches:
#     st.info("No matches found yet. Add matches to see leaderboard.")
# else:
#     match_df = pd.DataFrame(matches)

#     # Compute champion
#     champion = match_df.iloc[-1]["winner"]

#     # Count matches played and wins
#     matches_played = defaultdict(int)
#     wins = defaultdict(int)

#     for match in matches:
#         matches_played[match["team1"]] += 1
#         matches_played[match["team2"]] += 1
#         wins[match["winner"]] += 1

#     # Build leaderboard with status
#     leaderboard_rows = []
#     max_wins = max(wins.values()) if wins else 0

#     for team in set(matches_played.keys()).union(wins.keys()):
#         played = matches_played[team]
#         win_count = wins.get(team, 0)

#         if team == champion:
#             status = "🏆 Champion"
#         elif win_count == max_wins and team != champion:
#             status = "Finalist"
#         elif win_count == max_wins - 1:
#             status = "Semi-Finalist"
#         else:
#             status = "Eliminated"

#         leaderboard_rows.append({
#             "Team": team,
#             "Matches Played": played,
#             "Wins": win_count,
#             "Status": status
#         })

#     leaderboard_df = pd.DataFrame(leaderboard_rows)
#     leaderboard_df = leaderboard_df.sort_values(by=["Wins", "Matches Played"], ascending=False).reset_index(drop=True)

#     st.dataframe(leaderboard_df, use_container_width=True)

#     # Optional: Warn if some match teams are not in current teams list
#     match_teams = set(match_df["team1"]).union(set(match_df["team2"]))
#     unregistered = match_teams - set(all_team_names)
#     if unregistered:
#         st.warning(f"⚠️ Some teams in match history are not in the team list: {', '.join(unregistered)}")
