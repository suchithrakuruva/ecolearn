import streamlit as st

st.set_page_config(page_title="My Dashboard | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0d1b2a;
    color: #e0f2e9;
}
.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 24px;
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(45,106,79,0.4);
}
.profile-card {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 20px;
    padding: 32px;
    display: flex;
    gap: 28px;
    align-items: flex-start;
    box-shadow: 0 6px 28px rgba(0,0,0,0.3);
    border: 1px solid #40916c;
    margin-bottom: 24px;
}
.profile-name {
    font-size: 1.8rem;
    font-weight: 800;
    color: #d8f3dc;
    margin: 0 0 4px 0;
}
.profile-school {
    font-size: 1rem;
    color: #95d5b2;
    margin-bottom: 16px;
}
.stat-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(0,0,0,0.25);
    border: 1px solid #52b788;
    border-radius: 50px;
    padding: 6px 16px;
    font-size: 0.95rem;
    font-weight: 600;
    color: #b7e4c7;
    margin-right: 10px;
    margin-bottom: 8px;
}
.section-heading {
    font-size: 1.3rem;
    font-weight: 700;
    color: #b7e4c7;
    margin: 24px 0 12px 0;
    padding-left: 12px;
    border-left: 4px solid #52b788;
}
.achievement-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1px solid #2d6a4f;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.2);
}
.streak-box {
    background: linear-gradient(135deg, #3d1e00, #6b3300);
    border: 1px solid #e36414;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.2);
}
.goal-card {
    background: linear-gradient(135deg, #1a2744, #1e3a5f);
    border: 1px solid #2e6da1;
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}
div.stButton > button {
    background: linear-gradient(135deg, #2d6a4f, #40916c);
    color: #d8f3dc;
    border: none;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    transition: all 0.2s;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #40916c, #52b788);
    transform: translateY(-2px);
}
.stProgress > div > div { background-color: #52b788 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Session state defaults ─────────────────────────────────────────────────
if "user_name" not in st.session_state:
    st.session_state.user_name = "Alex Johnson"
if "school" not in st.session_state:
    st.session_state.school = "Green Valley High School"
if "eco_points" not in st.session_state:
    st.session_state.eco_points = 180
if "streak" not in st.session_state:
    st.session_state.streak = 7

# ─── Top Navigation ─────────────────────────────────────────────────────────
nav_l, nav_r = st.columns([4, 2])
with nav_l:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")
with nav_r:
    r1, r2 = st.columns(2)
    with r1:
        if st.button("⚙️ Settings"):
            st.info("Settings panel coming soon!")
    with r2:
        if st.button("🚪 Logout"):
            st.warning("You have been logged out.")

st.markdown("---")

# ─── Profile Card ───────────────────────────────────────────────────────────
st.markdown(f"""
<div class="profile-card">
    <img src="https://api.dicebear.com/7.x/adventurer/svg?seed=EcoKid&backgroundColor=2d6a4f"
         width="110" style="border-radius:50%;border:3px solid #52b788;flex-shrink:0;" />
    <div>
        <div class="profile-name">{st.session_state.user_name}</div>
        <div class="profile-school">🏫 {st.session_state.school}</div>
        <div>
            <span class="stat-pill">🌱 {st.session_state.eco_points} Eco Points</span>
            <span class="stat-pill">🔥 {st.session_state.streak}-Day Streak</span>
            <span class="stat-pill">🏅 Level 4 — Eco Warrior</span>
            <span class="stat-pill">📅 Member since Jan 2025</span>
        </div>
        <div style="margin-top:10px;font-size:0.88rem;color:#74c69d;">
            🎯 120 more points to reach <strong style="color:#b7e4c7;">Level 5 — Eco Champion</strong>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Dashboard Tabs ─────────────────────────────────────────────────────────
tab_ov, tab_str, tab_prog, tab_ach, tab_imp, tab_goal = st.tabs([
    "🌍 Overview", "🔥 Streaks", "📈 Progress", "🏅 Achievements", "🌱 Impact", "🎯 Goals"
])

# --- Overview ---
with tab_ov:
    st.markdown('<div class="section-heading">Your Eco Journey at a Glance</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for col, icon, label, val in [
        (c1, "🌱", "Eco Points", str(st.session_state.eco_points)),
        (c2, "🔥", "Day Streak", str(st.session_state.streak)),
        (c3, "📘", "Lessons Done", "34"),
        (c4, "🏆", "Challenges", "6"),
    ]:
        with col:
            st.markdown(f"""
<div class="achievement-card">
    <div style="font-size:2rem;">{icon}</div>
    <div style="font-size:1.6rem;font-weight:800;color:#b7e4c7;">{val}</div>
    <div style="font-size:0.85rem;color:#95d5b2;">{label}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="section-heading">Recent Activity</div>', unsafe_allow_html=True)
    activities = [
        ("🎥", "Watched: Climate Change — Greenhouse Effect", "2 hours ago", "+5 pts"),
        ("✅", "Completed: Waste Segregation Week Challenge", "Yesterday", "+40 pts"),
        ("🔥", "Maintained 7-day learning streak!", "Yesterday", "+15 pts"),
        ("📘", "Finished: Biodiversity Lesson 3", "2 days ago", "+8 pts"),
        ("👥", "Joined Team: Green Guardians", "3 days ago", "+10 pts"),
    ]
    for icon, act, time, pts in activities:
        st.markdown(f"""
<div style="display:flex;justify-content:space-between;align-items:center;
            padding:12px 16px;background:#152b22;border-radius:10px;
            border:1px solid #2d6a4f;margin-bottom:8px;">
    <div>{icon} &nbsp; <span style="color:#d8f3dc;">{act}</span></div>
    <div style="text-align:right;">
        <span style="color:#95d5b2;font-size:0.8rem;">{time}</span>&nbsp;&nbsp;
        <span style="color:#52b788;font-weight:700;font-size:0.9rem;">{pts}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Streaks ---
with tab_str:
    st.markdown('<div class="section-heading">🔥 Your Streaks</div>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("""
<div class="streak-box">
    <div style="font-size:3rem;">🔥</div>
    <div style="font-size:2rem;font-weight:800;color:#f4a261;">7</div>
    <div style="color:#f4a261;font-size:0.9rem;">Current Streak</div>
</div>""", unsafe_allow_html=True)
    with s2:
        st.markdown("""
<div class="streak-box" style="background:linear-gradient(135deg,#1a2744,#1e3a5f);border-color:#457b9d;">
    <div style="font-size:3rem;">⚡</div>
    <div style="font-size:2rem;font-weight:800;color:#90c7f4;">21</div>
    <div style="color:#90c7f4;font-size:0.9rem;">Longest Streak</div>
</div>""", unsafe_allow_html=True)
    with s3:
        st.markdown("""
<div class="streak-box" style="background:linear-gradient(135deg,#1b3320,#2d5a3d);border-color:#52b788;">
    <div style="font-size:3rem;">📅</div>
    <div style="font-size:2rem;font-weight:800;color:#95d5b2;">42</div>
    <div style="color:#95d5b2;font-size:0.9rem;">Total Active Days</div>
</div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-heading">This Week</div>', unsafe_allow_html=True)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    done = [True, True, True, True, True, True, True]
    cols = st.columns(7)
    for i, (col, day, d) in enumerate(zip(cols, days, done)):
        with col:
            bg = "#52b788" if d else "#2d3748"
            emoji = "🔥" if d else "⬜"
            st.markdown(f"""
<div style="text-align:center;background:{bg};border-radius:10px;padding:12px 4px;">
    <div style="font-size:1.3rem;">{emoji}</div>
    <div style="font-size:0.8rem;font-weight:700;color:{'#d8f3dc' if d else '#888'};">{day}</div>
</div>""", unsafe_allow_html=True)

# --- Progress ---
with tab_prog:
    st.markdown('<div class="section-heading">📈 Learning Progress</div>', unsafe_allow_html=True)
    progress_items = [
        ("🌍 Climate Change", 60, 12, 12),
        ("🦋 Biodiversity", 40, 8, 8),
        ("💧 Water Conservation", 25, 6, 6),
        ("♻️ Waste Management", 80, 15, 15),
        ("☀️ Renewable Energy", 15, 10, 10),
        ("🌱 Sustainable Agriculture", 35, 9, 9),
    ]
    for title, pct, total_lessons, _ in progress_items:
        done_lessons = int(total_lessons * pct / 100)
        st.markdown(f"""
<div style="padding:14px 18px;background:#152b22;border-radius:12px;
            border:1px solid #2d6a4f;margin-bottom:10px;">
    <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
        <span style="font-weight:700;color:#d8f3dc;">{title}</span>
        <span style="color:#52b788;font-weight:700;">{pct}%</span>
    </div>
    <div style="color:#74c69d;font-size:0.82rem;margin-bottom:8px;">
        {done_lessons} / {total_lessons} lessons completed
    </div>
</div>""", unsafe_allow_html=True)
        st.progress(pct / 100)

# --- Achievements ---
with tab_ach:
    st.markdown('<div class="section-heading">🏅 Your Badges</div>', unsafe_allow_html=True)
    badges = [
        ("🌱", "First Step", "Completed your first lesson", True),
        ("🔥", "7-Day Warrior", "Maintained a 7-day streak", True),
        ("♻️", "Recycler Pro", "Completed Waste Management path", True),
        ("🌍", "Climate Aware", "Finished Climate Change module", True),
        ("👥", "Team Player", "Joined an eco team", True),
        ("🏆", "Challenge Champ", "Won 3 challenges", False),
        ("💧", "Water Guardian", "Completed Water Conservation", False),
        ("🌳", "Tree Hugger", "Planted 5 trees", False),
    ]
    rows = [badges[i:i+4] for i in range(0, len(badges), 4)]
    for row in rows:
        cols = st.columns(4)
        for col, (icon, name, desc, earned) in zip(cols, row):
            with col:
                opacity = "1" if earned else "0.35"
                border = "#52b788" if earned else "#2d3748"
                st.markdown(f"""
<div style="text-align:center;padding:16px;background:#152b22;border-radius:14px;
            border:2px solid {border};opacity:{opacity};margin-bottom:8px;">
    <div style="font-size:2.5rem;">{icon}</div>
    <div style="font-weight:700;color:#d8f3dc;font-size:0.9rem;">{name}</div>
    <div style="font-size:0.75rem;color:#74c69d;margin-top:4px;">{desc}</div>
    <div style="margin-top:6px;font-size:0.75rem;color:{'#52b788' if earned else '#555'};">
        {'✅ Earned' if earned else '🔒 Locked'}
    </div>
</div>""", unsafe_allow_html=True)

# --- Impact ---
with tab_imp:
    st.markdown('<div class="section-heading">🌱 Your Real-World Impact</div>', unsafe_allow_html=True)
    i1, i2, i3, i4 = st.columns(4)
    for col, icon, val, label in [
        (i1, "🌳", "5", "Trees Planted"),
        (i2, "♻️", "20 kg", "Waste Recycled"),
        (i3, "💧", "200 L", "Water Saved"),
        (i4, "🚲", "18 km", "Car Trips Replaced"),
    ]:
        with col:
            st.markdown(f"""
<div class="achievement-card" style="padding:24px;">
    <div style="font-size:2.2rem;">{icon}</div>
    <div style="font-size:1.6rem;font-weight:800;color:#b7e4c7;">{val}</div>
    <div style="font-size:0.82rem;color:#74c69d;">{label}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
<div style="background:linear-gradient(135deg,#1b4332,#2d6a4f);border-radius:16px;
            padding:24px;border:1px solid #52b788;text-align:center;">
    <div style="font-size:1.1rem;color:#b7e4c7;">🌍 Equivalent CO₂ offset by your actions</div>
    <div style="font-size:3rem;font-weight:800;color:#52b788;margin:8px 0;">12.4 kg</div>
    <div style="color:#74c69d;font-size:0.9rem;">Keep going — every action counts! 💚</div>
</div>""", unsafe_allow_html=True)

# --- Goals ---
with tab_goal:
    st.markdown('<div class="section-heading">🎯 Your Goals</div>', unsafe_allow_html=True)
    goals = [
        ("🌱 Reach 300 Eco Points", 180, 300, "#52b788"),
        ("📘 Complete Climate Change Path", 60, 100, "#e63946"),
        ("🔥 Achieve 21-Day Streak", 7, 21, "#f4a261"),
        ("🏆 Win 5 Challenges", 3, 5, "#457b9d"),
        ("🌳 Plant 10 Trees", 5, 10, "#606c38"),
    ]
    for title, current, target, color in goals:
        pct = int(current / target * 100)
        st.markdown(f"""
<div class="goal-card">
    <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
        <span style="font-weight:700;color:#bde0fe;">{title}</span>
        <span style="color:{color};font-weight:700;">{current} / {target}</span>
    </div>
</div>""", unsafe_allow_html=True)
        st.progress(pct / 100)
        st.caption(f"{pct}% complete")

# Footer
st.divider()
st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:8px 0;">
    🌱 <strong>EcoLearn</strong> — Your personal eco journey dashboard
</div>""", unsafe_allow_html=True)
