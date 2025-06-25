import streamlit as st
from datetime import date, datetime
from utils import load_data


st.set_page_config(
    page_title="SWE4 Tournaments",
    layout="wide",
    initial_sidebar_state ="expanded",
    menu_items={
        'About': "Made with ❤️ by the SWE4 Event Management Team"
    }
)
MAIN_LOGO_URL="images/main-logo.jpg"
SMALL_LOGO_URL="images/small-logo.jpeg"
st.logo(
    MAIN_LOGO_URL,
    icon_image=SMALL_LOGO_URL,
    size="large"
)
st.image("images/carrom-board.jpg", use_container_width=True)
st.title("Welcome to Carrom Tournament! ⛀⛁")

st.markdown("""
This app helps track match results, schedule games, and view the leaderboard — all in one place.

🏆 Format: Knockout (Single Elimination) :sunglasses:  
📅 Tournament Duration: July 07 – July 21
""")

st.balloons()
st.subheader("📊 Tournament Overview", divider="gray")

# Load from data.json
data = load_data()
matches = data.get("matches", [])
players = data.get("players", [])
tournament = data.get("tournament", {})
teams = data.get("teams", [])

# Extract details
matches_played = len(matches)
players_count = len(players)

# Parse dates
start_date = datetime.strptime(tournament.get("start_date", "2025-06-24"), "%Y-%m-%d").date()
end_date = datetime.strptime(tournament.get("end_date", "2025-07-10"), "%Y-%m-%d").date()
duration_days = (end_date - start_date).days

# Layout: 4 metrics in a row
col1, col2, col3 = st.columns(3)
col1.metric("🧑‍🤝‍🧑 Players", players_count)
col2.metric("🏆 Teams", len(teams))
col3.metric("✅ Matches", matches_played)


st.divider(width="stretch")
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
