import streamlit as st

st.set_page_config(page_title="Carrom Rules", layout="wide")

st.title("📜 Official Carrom Rules")
st.markdown("### 🏓 Know the Game Before You Play!")

st.markdown("""
<style>
.rule-box {
    background-color: #f9f9f9;
    border-left: 5px solid #f63366;
    padding: 16px;
    margin-bottom: 20px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

def rule(title, description):
    st.markdown(f"""
    <div class="rule-box">
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

rule("⏰ Reporting Time",
     "All players must report 10 minutes before the match. Failing to show on time results in walkover.")

rule("🏆 Knockout Format",
     "The entire tournament follows a knockout system. Lose once = you're out.")

rule("⚫⚪ Coin Assignment",
     "Each team gets either black or white coins. You must pocket only your coins to score.")

rule("🔴 Red Coin Rule", 
     """
     <ul>
         <li>Red can be potted only after at least one of your own coins.</li>
         <li>Red must be followed by a valid coin; else it’s placed back in center with a penalty.</li>
     </ul>
     """)

rule("🚫 Fouls & Penalties",
     """
     <ul>
         <li>Touching coins or board with body/hands is a foul.</li>
         <li>Potting opponent’s coin directly = penalty of 1 coin.</li>
         <li>First foul = warning, after that 1 coin penalty per foul.</li>
     </ul>
     """)

rule("⏱️ Striking Time Limit",
     """
     <ul>
         <li>Round 1–2: 20 sec</li>
         <li>Round 3–5: 30 sec</li>
         <li>Quarterfinals onward: 40 sec</li>
         <li>Exceeding = turn cut.</li>
     </ul>
     """)

rule("🏁 Final Coin Rule",
     "If a player pots last coin before red, opponent wins the board and gets red coin + all remaining coins as points.")

rule("🕒 Time & Points Rules",
     """
     <ul>
         <li>Match ends at max time or after X boards (depends on round).</li>
         <li>For round 1-5 time = 20 mins. For semifinals and finals time = 40 mins.</li>
         <li>Winner = team with most points.</li>
         <li>In case of tie at final board, team with least coins left on board wins.</li>
     </ul>
     """)

rule("💯 Coin Points",
     """
     <ul>
         <li>Regular coin = 1 point</li>
         <li>Red coin = 3 points (Final: 5 points)</li>
     </ul>
     """)

rule("🤝 Player Behavior",
     "No talking during opponent’s turn. No moving chair. Referee can warn or penalize 1 coin. Referee’s decision is final.")

st.markdown("## 🔄 Handling Special Cases")

rule("⏳ Time Exceeds",
     """
     <ul>
         <li>If time is up mid-board, stop immediately.</li>
         <li>Winner = team with higher points.</li>
         <li>Tie? Winner = team with least coins left on board (red not counted).</li>
     </ul>
     """)

rule("🤔 Draw Situation (Same Points & Coins)",
     """
     <ul>
         <li>1-Board Tie-Breaker Match (5 min max).</li>
         <li>If still tied, winner decided by who pockets red first in tie-breaker.</li>
     </ul>
     """)

rule("⚠️ Disruptions / Unforeseen Events",
     """
     <ul>
         <li>Game paused.</li>
         <li>Referee + Organizers decide whether to replay, resume, or forfeit based on situation.</li>
     </ul>
     """)

st.success("✅ Follow these rules and have a fair, fun tournament!")