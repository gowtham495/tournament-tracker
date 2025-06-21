import streamlit as st
from datetime import date
import pandas as pd
from utils import load_data, save_data

st.set_page_config(page_title="Match Entry", layout="wide")

data = load_data()
teams = [team["name"] for team in data["teams"]]

st.title("📋 Matches Summary")

if data["matches"]:
    match_df = pd.DataFrame(data["matches"])

    # Add Serial Number column
    match_df.insert(0, "Match #", range(1, len(match_df) + 1))

    # Display without index
    st.dataframe(match_df, use_container_width=True, hide_index=True)

    # Download without index
    csv = match_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Match Data", csv, "carrom_matches.csv", "text/csv")
else:
    st.info("No matches recorded yet.")
