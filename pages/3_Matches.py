import streamlit as st
from datetime import date
import pandas as pd
from utils import load_data, save_data, show_footer

st.set_page_config(page_title="Match Entry", layout="wide")

data = load_data()
teams = [team["name"] for team in data["teams"]]

st.title("📋 Matches Summary")
st.subheader("Round 1", divider=True)

if data["matches"]:
    match_df = pd.DataFrame(data["matches"])

    # Add Serial Number column
    match_df.insert(0, "Match #", range(1, len(match_df) + 1))

    # Display without index
    st.dataframe(match_df, use_container_width=True, hide_index=True)

    # Download without index
    csv = match_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Round 1 Matches", csv, "carrom_matches.csv", "text/csv")
else:
    st.info("No matches recorded yet.")


st.subheader("Round 2", divider=True)
if data["round_2_matches"]:
    match_df = pd.DataFrame(data["round_2_matches"])

    # Add Serial Number column
    match_df.insert(0, "Match #", range(1, len(match_df) + 1))

    # Display without index
    st.dataframe(match_df, use_container_width=True, hide_index=True)

    # Download without index
    csv = match_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Round 2 Matches", csv, "carrom_matches.csv", "text/csv")
else:
    st.info("No matches recorded yet.")

show_footer()
