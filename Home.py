import streamlit as st
from datetime import date, datetime
from utils import load_data


st.set_page_config(page_title="SWE4 Tournament Tracker", layout="wide")

st.title("Welcome to Carrom Tournament! ⛀⛁")
st.image("images/carrom-board.jpg", use_container_width=False)
st.sidebar.success("")
st.markdown("""
This app helps track match results, schedule games, and view the leaderboard — all in one place.

🏆 Format: Knockout (Single Elimination)  
📅 Duration: June 24 – July 10  
👥 Teams: 16  
""")

st.set_page_config(page_title="Tournament Overview", layout="wide")
st.title("📊 Tournament Overview")

# Load from data.json
data = load_data()
matches = data.get("matches", [])
players = data.get("players", [])
tournament = data.get("tournament", {})

# Extract details
total_matches = tournament.get("total_matches", len(matches))  # fallback
matches_played = len(matches)
players_count = len(players)

# Parse dates
start_date = datetime.strptime(tournament.get("start_date", "2025-06-24"), "%Y-%m-%d").date()
end_date = datetime.strptime(tournament.get("end_date", "2025-07-10"), "%Y-%m-%d").date()
duration_days = (end_date - start_date).days

# Layout: 4 metrics in a row
col1, col2, col3, col4 = st.columns(4)
col1.metric("🧑‍🤝‍🧑 Players", players_count)
col2.metric("✅ Matches Played", matches_played)
col3.metric("🎯 Total Matches", total_matches)
col4.metric("📅 Duration", f"{duration_days} days")

# Visual Progress Bar
st.markdown("### 🔄 Tournament Progress")
progress = matches_played / total_matches if total_matches > 0 else 0
st.progress(progress)

# Optional note
if matches_played == total_matches:
    st.success("🏁 Tournament Completed!")
elif matches_played > 0:
    st.info(f"{matches_played} of {total_matches} matches played.")
else:
    st.warning("No matches played yet.")


st.markdown("""
### 🔗 Quick Navigation

Use the **sidebar** to navigate:

- 👉 View **Rules** to know the game guidelines            
- 👉 Go to **Matches** view all matches  
- 👉 Open **Leaderboard** to see who’s on top  


👈 Sidebar is on the left!
""")

st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: white;
        padding: 10px;
        text-align: left;
        font-size: 0.9rem;
        color: gray;
        border-top: 1px solid #f0f0f0;
    }
    </style>

    <div class="footer">
        Made with ❤️ by the SWE4 Event Management Team
    </div>
""", unsafe_allow_html=True)



