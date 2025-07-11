import streamlit as st
import json
from utils import show_footer
import pandas as pd

# Load tournament data
with open("data.json") as f:
    data = json.load(f)

# Build team -> player mapping
team_players_map = {
    team["name"]: team["players"]
    for team in data.get("teams", [])
}

st.title("🏆 Carrom Tournament Leaderboard")

# Define rounds explicitly
rounds = [
    ("Round 1", "matches"),
    ("Round 2", "round_2_matches"),
    ("Grand Finale", "final_matches")
]

# Display each round winners
for round_name, key in rounds:
    matches = data.get(key, [])
    winners = []

    for match in matches:
        winner_team = match.get("winner", "").strip()
        if winner_team:
            players = team_players_map.get(winner_team, ["-", "-"])
            winners.append({
                "Team": winner_team,
                "Player 1": players[0],
                "Player 2": players[1],
            })

    st.subheader(f"{round_name} Winners")

    if winners:
        df = pd.DataFrame(winners)
        df.index = range(1, len(df) + 1)  # Index starting from 1
        st.table(df)
    else:
        st.info("No winners recorded yet.")

show_footer()
