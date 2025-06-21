import streamlit as st
import pandas as pd
from datetime import date

# Initialize storage
if 'matches' not in st.session_state:
    st.session_state.matches = []

st.title("🏓 Carrom Tournament Tracker")

# Player input
with st.form("match_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        player1 = st.text_input("Player 1")
    with col2:
        player2 = st.text_input("Player 2")
    with col3:
        match_date = st.date_input("Match Date", date.today())

    winner = st.selectbox("Winner", options=[player1, player2] if player1 and player2 else [])

    submitted = st.form_submit_button("Add Match")
    if submitted and player1 and player2 and winner:
        st.session_state.matches.append({
            "Date": match_date,
            "Player 1": player1,
            "Player 2": player2,
            "Winner": winner
        })
        st.success("Match added!")

# Show match history
if st.session_state.matches:
    st.subheader("📋 Match History")
    match_df = pd.DataFrame(st.session_state.matches)
    st.dataframe(match_df)

    # Leaderboard
    st.subheader("🏆 Leaderboard")
    leaderboard = match_df['Winner'].value_counts().reset_index()
    leaderboard.columns = ['Player', 'Wins']
    st.dataframe(leaderboard)

# Export option
if st.session_state.matches:
    csv = pd.DataFrame(st.session_state.matches).to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download CSV", csv, file_name="carrom_matches.csv", mime='text/csv')
