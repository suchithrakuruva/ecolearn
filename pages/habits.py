import streamlit as st
from datetime import date

st.set_page_config(page_title="Eco Habits | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.habit-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1.5px solid #2d6a4f; border-radius: 14px;
    padding: 18px 22px; margin-bottom: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    display: flex; justify-content: space-between; align-items: center;
}
.habit-card-done {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border: 1.5px solid #52b788;
}
.habit-title { font-size: 1rem; font-weight: 700; color: #d8f3dc; }
.habit-desc { font-size: 0.82rem; color: #74c69d; }
.pts-badge {
    background: #1b4332; border: 1px solid #52b788;
    color: #b7e4c7; border-radius: 8px; padding: 4px 12px;
    font-size: 0.82rem; font-weight: 700; white-space: nowrap;
}
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
.stProgress > div > div { background-color: #52b788 !important; }
.stat-box {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 14px; padding: 20px; text-align: center;
    border: 1px solid #40916c; box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">🌿 Build Eco Habits</div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:16px;">
    📅 Today: <strong style="color:#b7e4c7;">{date.today().strftime('%A, %d %B %Y')}</strong>
    &nbsp;|&nbsp; Track your daily eco habits and build a streak! 🔥
</div>""", unsafe_allow_html=True)

# Session state for habits
if "completed_habits" not in st.session_state:
    st.session_state.completed_habits = set()

habits = [
    ("🚰", "Use a Reusable Bottle", "Avoid single-use plastic bottles today.", 5),
    ("🛍️", "No Plastic Bags", "Use cloth or paper bags for all shopping.", 5),
    ("🚶", "Walk or Cycle", "Travel at least one trip by foot or cycle.", 8),
    ("🌿", "Eat Plant-Based Meal", "Have at least one vegetarian or vegan meal.", 6),
    ("💡", "Switch Off Unused Lights", "Turn off lights whenever you leave a room.", 4),
    ("🚿", "Short Shower (< 5 min)", "Cut your shower time to under 5 minutes.", 6),
    ("📰", "Say No to Paper Printouts", "Go digital for all notes and assignments today.", 4),
    ("♻️", "Segregate Your Waste", "Sort your waste into wet, dry and hazardous.", 7),
    ("🌱", "Water a Plant", "Water a plant at home, school or your garden.", 3),
    ("📲", "Share an Eco Tip", "Share one eco tip with a friend or on social media.", 4),
    ("🍽️", "No Food Waste", "Finish your plate and pack leftovers properly.", 5),
    ("🔌", "Unplug Chargers", "Unplug all unused chargers and standby devices.", 4),
]

st.markdown('<div class="section-heading">✅ Today\'s Habits Checklist</div>', unsafe_allow_html=True)
today_points = 0

for icon, title, desc, pts in habits:
    key = f"habit_{title}"
    done = key in st.session_state.completed_habits
    border_style = "habit-card habit-card-done" if done else "habit-card"

    c1, c2, c3 = st.columns([5, 1.5, 1.5])
    with c1:
        st.markdown(f"""
<div class="{border_style}">
    <div>
        <div class="habit-title">{icon} &nbsp;{title} {'✅' if done else ''}</div>
        <div class="habit-desc">{desc}</div>
    </div>
    <span class="pts-badge">+{pts} pts</span>
</div>""", unsafe_allow_html=True)
    with c2:
        if not done:
            if st.button("✅ Done!", key=f"btn_{key}", use_container_width=True):
                st.session_state.completed_habits.add(key)
                st.rerun()
        else:
            st.markdown("<div style='padding-top:8px;color:#52b788;font-weight:700;'>Completed!</div>",
                        unsafe_allow_html=True)
    with c3:
        if done:
            today_points += pts

# Progress summary
total_pts = sum(pts for _, _, _, pts in habits)
earned_pts = sum(pts for _, title, _, pts in habits
                 if f"habit_{title}" in st.session_state.completed_habits)
done_count = len(st.session_state.completed_habits)

st.divider()
st.markdown('<div class="section-heading">📊 Today\'s Summary</div>', unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    st.markdown(f"""
<div class="stat-box">
    <div style="font-size:2rem;">✅</div>
    <div style="font-size:1.8rem;font-weight:800;color:#b7e4c7;">{done_count}</div>
    <div style="color:#74c69d;font-size:0.88rem;">Habits Completed</div>
</div>""", unsafe_allow_html=True)
with s2:
    st.markdown(f"""
<div class="stat-box">
    <div style="font-size:2rem;">🌱</div>
    <div style="font-size:1.8rem;font-weight:800;color:#b7e4c7;">{earned_pts}</div>
    <div style="color:#74c69d;font-size:0.88rem;">Eco Points Earned</div>
</div>""", unsafe_allow_html=True)
with s3:
    pct = int(done_count / len(habits) * 100)
    st.markdown(f"""
<div class="stat-box">
    <div style="font-size:2rem;">🏆</div>
    <div style="font-size:1.8rem;font-weight:800;color:#b7e4c7;">{pct}%</div>
    <div style="color:#74c69d;font-size:0.88rem;">Daily Goal Progress</div>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.progress(done_count / len(habits))

if done_count == len(habits):
    st.success("🎉 **Perfect Day!** You've completed ALL today's eco habits! You earned a +20 Bonus streak point!")
    st.balloons()
elif done_count >= len(habits) // 2:
    st.info(f"🌿 Great job! You're past halfway — keep going! {len(habits) - done_count} habits left.")
elif done_count > 0:
    st.warning(f"🌱 Good start! {len(habits) - done_count} more habits to complete today.")

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 4px;">
    🌱 <strong>EcoLearn</strong> — Small daily habits create a big impact. Keep going! 💚
</div>""", unsafe_allow_html=True)

