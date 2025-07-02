import streamlit as st
import random
import time
from utils import load_data, save_data, show_footer

st.set_page_config(page_title="Fixtures Generator", layout="centered")
st.info("⚙️ Fixtures cooked up in our randomness lab. Pure chaos. Fair play guaranteed.", icon="🧪")
st.title("🥊 Fixtures Generator")

data = load_data()
teams = data.get("teams", [])
team_names = [team["name"] for team in teams]

# Identify already selected teams
used_teams = set()
for match in data.get("matches", []):
    used_teams.add(match["team1"])
    used_teams.add(match["team2"])

available_teams = list(set(team_names) - used_teams)
available_teams.sort()

# Initialize session state
if "generated_match" not in st.session_state:
    st.session_state.generated_match = ("", "")

# Button press logic (no on_click)
if len(available_teams) >= 2:
    if st.button("🎰 Spin to Generate Match", disabled=True):
        team1, team2 = random.sample(available_teams, 2)
        st.session_state.generated_match = (team1, team2)

        # Save to matches
        data["matches"].append({
            "date": "",
            "team1": team1,
            "team2": team2,
            "team1_points": "",
            "team2_points": "",
            "winner": ""
        })
        save_data(data)

        # Force rerun AFTER saving
        st.rerun()

    # Show last match
    if st.session_state.generated_match[0]:
        team1, team2 = st.session_state.generated_match
        with st.spinner("Pairing teams..."):
            time.sleep(1)
        st.success("✅ Match Paired!")
        st.markdown(f"""
            <div style="text-align:center; margin-top: 30px;">
                <span style="font-size: 2.3em; font-weight: bold;">{team1}</span>
                <span style="font-size: 2em; margin: 0 20px; color: crimson;">vs</span>
                <span style="font-size: 2.3em; font-weight: bold;">{team2}</span>
            </div>
        """, unsafe_allow_html=True)
else:
    st.success("✅ All teams have been paired for this round!")

# Show all matches
if data["matches"]:
    st.markdown("### 📋 Knockout Matchups")
    table = [
        {"Match #": i + 1, "Team 1": m["team1"], "Team 2": m["team2"]}
        for i, m in enumerate(data["matches"])
    ]
    st.dataframe(table, use_container_width=True)

# Optional reset
st.divider()

show_footer()
