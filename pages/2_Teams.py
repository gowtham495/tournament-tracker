import pandas as pd
import streamlit as st
from utils import load_data, save_data

st.set_page_config(page_title="Register Team", layout="wide")
st.title("👥 Register Your Team")

data = load_data()
all_players = data.get("players", [])
existing_teams = data.get("teams", [])

# Gather all assigned players across existing teams
used_players = set(p for team in existing_teams for p in team["players"])

# Form to create a team
with st.form("create_team_form"):
    team_name = st.text_input("Team Name")

    st.markdown("### 🎯 Select 2 Players for the Team")

    col1, col2 = st.columns(2)
    with col1:
        player1 = st.selectbox("Player 1", [p for p in all_players if p not in used_players], key="player1")
    with col2:
        player2 = st.selectbox("Player 2", [p for p in all_players if p not in used_players and p != player1], key="player2")

    submit = st.form_submit_button("Register Team")

    if submit:
        name_exists = any(team["name"].lower() == team_name.lower() for team in existing_teams)
        player_conflict = player1 in used_players or player2 in used_players

        if not team_name or not player1 or not player2:
            st.warning("⚠️ Please provide all required inputs.")
        elif name_exists:
            st.error(f"🚫 A team named **{team_name}** already exists.")
        elif player1 == player2:
            st.error("🚫 Please choose two different players.")
        elif player_conflict:
            st.error("🚫 One or both players are already in another team.")
        else:
            new_team = {
                "name": team_name.strip(),
                "players": [player1, player2]
            }
            data["teams"].append(new_team)
            save_data(data)
            st.success(f"✅ Team **{team_name}** created with **{player1}** and **{player2}**.")


# --- Show Existing Teams in Table ---
if data["teams"]:
    st.subheader("📋 Registered Teams")
    team_df = pd.DataFrame([
        {"Team Name": team["name"], "Players": ", ".join(team["players"])}
        for team in data["teams"]
    ])
    st.dataframe(team_df, use_container_width=True)
else:
    st.info("No teams registered yet.")

