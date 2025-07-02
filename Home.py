import streamlit as st
from datetime import datetime
from utils import load_data
from utils import show_footer

# --- Config ---
st.set_page_config(
    page_title="SWE4 Tournaments",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Crafted with ❤️ by the SWE4 Event Management Team"
    }
)

st.markdown("""
    <div style="
        background-color: #d9f9ff;
        padding: 10px;
        border-left: 5px solid #00bcd4;
        font-size: 18px;
        margin-bottom: 1rem;
    ">
        📣 <b>Latest Update:</b> Fixtures have been released for Round 1. Click Matches in Sidebar to view!
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div style="
        background-color: #fff0e6;
        background-image: linear-gradient(315deg, #ffd3b6 0%, #ff6f61 74%);
        padding: 1rem 2rem;
        border-radius: 10px;
        text-align: center;
        color: #802b1a;  /* warm coral text */
        font-size: 22px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    ">
        🙌 The stage is set, the coins are stacked — SWE4 Carrom Tournament 2025 begins now! Let the best team win! 🥇
    </div>
""", unsafe_allow_html=True)

st.image("images/carrom-board.jpg", use_container_width=True)

st.title("🎯 Welcome to SWE4 Carrom Tournament 2025 !")

st.markdown("""
> **Smashes. Strikes. Sudden wins.**  
> Get ready to witness the ultimate knockout battle! This app helps you track results, fixtures, and who's inching closer to glory.
""")

# --- Quick Info ---
st.markdown("""
### 📅 Tournament Details

- **Format**: Knockout (Single Elimination)  
- **Duration**: July 07 – July 21  
- **Venue**: SWE4 Recreation Zone  (4th Floor Canteen)
""")

st.balloons()

# --- Overview Section ---
st.subheader("📊 Tournament Overview", divider="gray")

data = load_data()
matches = data.get("matches", [])
players = data.get("players", [])
teams = data.get("teams", [])
tournament = data.get("tournament", {})

players_count = len(teams) * 2
matches_played = len(matches)

start_date = datetime.strptime(tournament.get("start_date", "2025-07-07"), "%Y-%m-%d").date()
end_date = datetime.strptime(tournament.get("end_date", "2025-07-21"), "%Y-%m-%d").date()
duration_days = (end_date - start_date).days

# --- Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("👥 Players", players_count)
col2.metric("💪 Teams", len(teams))
col3.metric("🎯 Matches", matches_played)

st.divider()

# --- Quick Navigation ---
st.markdown("### 🧭 Quick Navigation")

st.markdown("""
👈 Use the **sidebar** to explore:

- 📌 **Rules** – Know what counts  
- 🗓️ **Matches** – See fixtures and results  
- 🥇 **Leaderboard** – Track who’s climbing to the top  
- 🎮 **Live Updates** – Coming soon!
""")

show_footer()
