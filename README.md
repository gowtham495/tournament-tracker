# 🏆 Tournament Tracker

A visually rich and interactive **Streamlit-based** web application for managing tournaments—track rules, register teams, generate fixtures, manage matches, view leaderboards, and collect feedback all in one place.

---

## 📁 Project Structure

```
tournament-tracker/
├── app.py                   # Main entry point for the Streamlit app
├── Home.py                 # Landing page with intro and overview
├── pages/
│   ├── 1_Rules.py          # Tournament rules page
│   ├── 2_Teams.py          # Team registration and management
│   ├── 3_Matches.py        # Match result recording
│   ├── 4_Leaderboard.py    # Dynamic leaderboard
│   ├── 5_Fixtures.py       # Fixture generation and viewing
│   ├── 6_Feedback.py       # Feedback form
├── utils.py                # Utility functions for app logic
├── data.json               # Data store (teams, matches, scores)
├── requirements.txt        # Python dependencies
├── .gitignore
├── .streamlit/
│   └── config.toml         # Streamlit app settings
├── .devcontainer/
│   └── devcontainer.json   # Dev container config for VS Code
└── images/
    ├── carrom-board.jpg
    ├── main-logo.jpg
    └── small-logo.jpeg
```

---

## 🚀 Features

- ✅ **Modular Pages** using Streamlit multipage support
- 🎮 **Add/Manage Teams** dynamically
- 🎯 **Create Match Fixtures** and record results
- 📊 **Live Leaderboard** updated with scores
- 🧾 **Rules Section** for transparency
- 📝 **Feedback Collection** for improvements
- 🖼️ Logo and image assets for a polished interface

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** (for UI)
- **JSON** (as a lightweight data store)
- Optional: Docker development container via `.devcontainer`

---

## 🧩 Setup & Installation

### 🔧 Prerequisites
- Python 3.8+
- `pip` for Python package management

### 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the app
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---
### 🖼️ Streamlit UI Snapshots
<img width="940" height="404" alt="image" src="https://github.com/user-attachments/assets/26a23504-e559-4fcc-ac5b-588bf057ab80" />
<img width="940" height="457" alt="image" src="https://github.com/user-attachments/assets/bb8be801-cb14-4e07-b04b-4ff0a142e674" />
<img width="940" height="470" alt="image" src="https://github.com/user-attachments/assets/ea9fe74a-44ee-4469-b7fd-6944662ed203" />
<img width="940" height="634" alt="image" src="https://github.com/user-attachments/assets/656f368b-672f-4e36-8d64-c14c46816165" />

---

## 💡 Future Improvements

- Persistent storage (SQLite/PostgreSQL)
- User authentication
- Export results as PDF/Excel
- Admin controls for edits

---

## 🤝 Contributing

1. Fork the repository
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👥 Contributors

Made with ❤️ by:

- [Gowtham](https://github.com/gowtham495)
- [Malvisha](https://github.com/Malvisha)

If you contributed to this project, feel free to open a PR to add your name here!
