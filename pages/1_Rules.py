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

rule("🎯 Objective",
     "Pocket all your carrom men (white or black depending on your side) before your opponent, and finally the red queen — with proper cover.")

rule("🟡 Carrom Men Colors",
     "- **White** and **Black** pieces (9 each)\n- **Red** is the **Queen**")

rule("🥇 Queen Rules",
     "You can pocket the red queen **only after** pocketing at least one of your own pieces. You must cover the queen in your **next shot**, or it is returned to the center.")

rule("🚫 Foul Rules",
     "- Pocketing opponent’s pieces\n- Pocketing the striker\n- Failure to cover the queen\n- Touching any piece with hand or clothing\n- Double striking")

rule("🕰️ Time Rules (if applicable)",
     "Set a time limit per turn (e.g., 15 seconds). If the player fails to strike within the time, it is considered a foul.")

rule("🎮 Turns",
     "Each player takes turns to strike. If you pocket a piece, you continue. If you miss, the turn goes to the opponent.")

rule("📏 Arrangement",
     "Pieces are placed in the center circle with the red queen at the center. Alternate colors are arranged around the queen.")

rule("🥌 Striker",
     "You must place the striker behind the baseline and hit it in a forward direction only. Bouncing off side cushions is allowed.")

st.success("✅ Follow these rules and have a fair, fun tournament!")
