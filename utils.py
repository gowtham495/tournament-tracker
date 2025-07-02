import json
import os
import streamlit as st

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"teams": [], "matches": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_footer():
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #fafafa;
            padding: 10px 20px;
            text-align: left;
            font-size: 0.85rem;
            color: #777;
            border-top: 1px solid #eee;
            z-index: 999;
        }
        </style>

        <div class="footer">
            Crafted with ❤️ by the SWE4 Event Management Team | 🚀 2025 Edition
        </div>
    """, unsafe_allow_html=True)
