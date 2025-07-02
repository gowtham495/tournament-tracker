import streamlit as st
import json
from utils import show_footer

# Load tournament data
with open("data.json") as f:
    data = json.load(f)

# Build team -> player mapping
team_players_map = {
    team["name"]: team["players"]
    for team in data.get("teams", [])
}

# Title
st.title("🏆 Carrom Tournament Leaderboard")

# Detect round keys dynamically
round_keys = [k for k in data.keys() if "matches" in k]

# Sort round keys to show Round 1, Round 2, etc.
round_keys = sorted(round_keys, key=lambda k: (0 if k == "matches" else int(k.split('_')[1])))

# Display round-wise winners
for i, key in enumerate(round_keys, 1):
    matches = data[key]
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

    st.subheader(f"Round {i} Winners")

    if winners:
        st.table(winners)
    else:
        st.info("No winners recorded yet.")

show_footer()
