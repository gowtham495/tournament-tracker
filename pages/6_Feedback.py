import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Feedback Form", layout="centered")

st.markdown("""
    <div style="
        background-color: #d9f9ff;
        padding: 10px;
        border-left: 5px solid #00bcd4;
        font-size: 18px;
        margin-bottom: 1rem;
    ">
        📣 <b>Note:</b> Submit button will be enabled after Grand Finale!
    </div>
""", unsafe_allow_html=True)

st.title("💬 Feedback Form")
st.write("We’d love to hear your thoughts about the tournament!")

# Feedback form
with st.form("feedback_form"):
    name = st.text_input("Name", max_chars=50)
    rating = st.slider("Rate your experience (1 - Poor, 5 - Excellent)", 1, 5, 4)
    what_went_good = st.text_area("✅ What you enjoyed ?", height=100)
    what_to_improve = st.text_area("⚠️ What needs to be improved?", height=100)
    submitted = st.form_submit_button("Submit", disabled=True)

    if submitted:
        if not name.strip() or not what_went_good.strip():
            st.error("Name and 'What went good?' are required.")
        else:
            # Load existing data.json
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                st.error("Could not load data.json.")
                st.stop()

            # Ensure 'feedback' key exists and is a list
            if "feedback" not in data or not isinstance(data["feedback"], list):
                data["feedback"] = []

            # Create feedback entry
            entry = {
                "timestamp": datetime.now().isoformat(),
                "name": name.strip(),
                "rating": rating,
                "what_went_good": what_went_good.strip(),
                "what_to_improve": what_to_improve.strip()
            }

            # Append and save
            data["feedback"].append(entry)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=2)

            st.success("🎉 Thank you for your feedback!")
