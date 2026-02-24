import streamlit as st

st.set_page_config(page_title="Leaderboard | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0d1b2a;
    color: #e0f2e9;
}
.section-heading {
    font-size: 1.35rem; font-weight: 800; color: #b7e4c7;
    margin: 24px 0 14px 0; padding-left: 12px; border-left: 5px solid #52b788;
}
.lb-row {
    display: flex; align-items: center; gap: 16px;
    padding: 14px 20px; border-radius: 14px; margin-bottom: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2); transition: transform 0.15s;
}
.lb-row:hover { transform: translateX(4px); }
.lb-name { font-size: 1rem; font-weight: 700; color: #d8f3dc; }
.lb-school { font-size: 0.8rem; color: #74c69d; }
.lb-pts { font-size: 1.1rem; font-weight: 800; }
div.stButton > button {
    background: linear-gradient(135deg, #2d6a4f, #40916c);
    color: #d8f3dc; border: none; border-radius: 10px;
    padding: 8px 20px; font-weight: 600; font-family: 'Poppins', sans-serif;
    transition: all 0.2s;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #40916c, #52b788);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">📊 EcoLearn Leaderboard</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:16px;">
    Top eco warriors ranked by their points this month. Can you make the top 10? 🏆
</div>""", unsafe_allow_html=True)

# Filters
filter_col1, filter_col2 = st.columns([2, 2])
with filter_col1:
    scope = st.selectbox("Filter by:", ["🏫 My School", "🌍 All Schools", "👥 My Team"])
with filter_col2:
    period = st.selectbox("Time Period:", ["📅 This Month", "📅 This Week", "📅 All Time"])

# Leaderboard data
leaderboard = [
    ("🥇", "Priya Sharma", "Green Valley High", 850, "🌍 Climate Expert", "#FFD700"),
    ("🥈", "Arjun Mehta", "Sunrise Academy", 822, "♻️ Recycling Pro", "#C0C0C0"),
    ("🥉", "Zara Khan", "Green Valley High", 790, "💧 Water Warrior", "#CD7F32"),
    ("4", "Riya Patel", "Bloom International", 745, "🦋 Bio Champion", "#b7e4c7"),
    ("5", "Kabir Singh", "Sunrise Academy", 720, "☀️ Solar Advocate", "#b7e4c7"),
    ("6", "Ananya Iyer", "Green Valley High", 695, "🌱 Habit Builder", "#b7e4c7"),
    ("7", "Dev Kumar", "Bloom International", 668, "🌳 Tree Planter", "#b7e4c7"),
    ("8", "Meera Joshi", "Green Valley High", 650, "🎮 Quiz Master", "#b7e4c7"),
    ("9", "Alex Johnson", "Green Valley High", 612, "🔥 Streak King", "#52b788"),
    ("10", "Fatima Noor", "Sunrise Academy", 589, "🏆 Team Leader", "#b7e4c7"),
    ("11", "Raj Verma", "Green Valley High", 540, "🌿 Eco Starter", "#6c757d"),
    ("12", "Sara Hussain", "Bloom International", 512, "📘 Quick Learner", "#6c757d"),
    ("13", "Neel Gupta", "Sunrise Academy", 490, "🌱 Green Rookie", "#6c757d"),
    ("14", "Diya Thomas", "Green Valley High", 475, "🔋 Energy Saver", "#6c757d"),
    ("15", "Vikram Rao", "Bloom International", 460, "🐝 Bee Keeper", "#6c757d"),
]

# Podium for top 3
st.markdown('<div class="section-heading">🏆 Top 3 This Month</div>', unsafe_allow_html=True)
p2, p1, p3 = st.columns(3)
podium_data = [
    (p1, leaderboard[0], "🥇", "2.2rem", "#FFD700", "#3a3000"),
    (p2, leaderboard[1], "🥈", "1.8rem", "#C0C0C0", "#2a2a2a"),
    (p3, leaderboard[2], "🥉", "1.6rem", "#CD7F32", "#2a1500"),
]
for col, player, medal, size, color, bg in podium_data:
    with col:
        st.markdown(f"""
<div style="text-align:center;background:linear-gradient(135deg,{bg},{bg}aa);
            border:2px solid {color};border-radius:18px;padding:22px 16px;
            box-shadow:0 4px 20px rgba(0,0,0,0.3);">
    <div style="font-size:2.5rem;">{medal}</div>
    <div style="font-size:{size};font-weight:800;color:{color};">{player[1]}</div>
    <div style="font-size:0.82rem;color:#74c69d;margin:4px 0;">{player[2]}</div>
    <div style="font-size:1rem;color:{color};font-weight:700;">{player[4]}</div>
    <div style="font-size:1.5rem;font-weight:800;color:{color};margin-top:6px;">
        🌱 {player[3]} pts
    </div>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="margin-top:24px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">📋 Full Rankings</div>', unsafe_allow_html=True)

# Highlight current user (rank 9 = Alex Johnson)
current_user = "Alex Johnson"
for rank, name, school, pts, badge, color in leaderboard:
    is_me = name == current_user
    bg = "linear-gradient(135deg, #1e4d38, #2d6a4f)" if is_me else \
         ("linear-gradient(135deg, #3a3000, #4d4000)" if rank == "🥇" else
          "linear-gradient(135deg, #2a2a2a, #3a3a3a)") if rank in ["🥇","🥈","🥉"] else \
         "linear-gradient(135deg, #152b22, #1b4332)"
    border = "#52b788" if is_me else color

    st.markdown(f"""
<div class="lb-row" style="background:{bg};border:1.5px solid {border};">
    <div style="font-size:1.4rem;min-width:38px;text-align:center;font-weight:800;color:{color};">{rank}</div>
    <img src="https://api.dicebear.com/7.x/adventurer/svg?seed={name.replace(' ','')}&backgroundColor=2d6a4f"
         width="42" style="border-radius:50%;border:2px solid {color};flex-shrink:0;" />
    <div style="flex:1;">
        <div class="lb-name">{name} {'<span style="background:#52b788;color:#0d1b2a;border-radius:6px;padding:2px 8px;font-size:0.75rem;margin-left:8px;">YOU</span>' if is_me else ''}</div>
        <div class="lb-school">🏫 {school} &nbsp;|&nbsp; {badge}</div>
    </div>
    <div class="lb-pts" style="color:{color};">🌱 {pts}</div>
</div>""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 4px;">
    🌱 <strong>EcoLearn</strong> — Rise through the ranks, save the planet! 🌍
</div>""", unsafe_allow_html=True)

