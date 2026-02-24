import streamlit as st

st.set_page_config(page_title="EcoLearn Hub 🌱", layout="wide", initial_sidebar_state="collapsed")

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0d1b2a;
    color: #e0f2e9;
}

/* Top navbar */
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
.nav-logo {
    font-size: 1.8rem;
    font-weight: 800;
    color: #b7e4c7;
    letter-spacing: 1px;
}
.nav-right {
    display: flex;
    gap: 12px;
}

/* Tab bar */
.tab-bar {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 28px;
}

/* Hero section */
.hero-quote {
    background: linear-gradient(135deg, #1b4332 60%, #2d6a4f);
    border-radius: 20px;
    padding: 40px 36px;
    font-size: 1.25rem;
    font-style: italic;
    color: #d8f3dc;
    border-left: 6px solid #52b788;
    box-shadow: 0 4px 24px rgba(82,183,136,0.2);
    line-height: 1.8;
}
.hero-author {
    margin-top: 16px;
    font-weight: 700;
    color: #95d5b2;
    font-style: normal;
    font-size: 1rem;
}

/* CTA Cards */
.cta-card {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 16px;
    padding: 28px 24px;
    text-align: center;
    border: 2px solid #52b788;
    transition: transform 0.2s;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}
.cta-card:hover { transform: translateY(-4px); }
.cta-icon { font-size: 2.5rem; margin-bottom: 8px; }
.cta-title { font-size: 1.15rem; font-weight: 700; color: #b7e4c7; margin-bottom: 4px; }
.cta-desc { font-size: 0.9rem; color: #95d5b2; }

/* Section headings */
.section-heading {
    font-size: 1.6rem;
    font-weight: 800;
    color: #b7e4c7;
    margin: 32px 0 16px 0;
    padding-left: 12px;
    border-left: 5px solid #52b788;
}

/* Learning path card */
.lp-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1px solid #2d6a4f;
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 14px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
    transition: box-shadow 0.2s;
}
.lp-card:hover { box-shadow: 0 6px 24px rgba(82,183,136,0.25); }
.lp-title { font-size: 1.15rem; font-weight: 700; color: #d8f3dc; margin-bottom: 4px; }
.lp-meta { font-size: 0.88rem; color: #95d5b2; }
.badge {
    display: inline-block;
    background: #2d6a4f;
    color: #b7e4c7;
    border-radius: 8px;
    padding: 2px 10px;
    font-size: 0.8rem;
    margin-right: 6px;
    font-weight: 600;
}

/* Challenge card */
.ch-card {
    background: linear-gradient(135deg, #1a2744, #1e3a5f);
    border: 1px solid #2e6da1;
    border-radius: 16px;
    padding: 20px 24px;
    margin-bottom: 14px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.25);
    transition: box-shadow 0.2s;
}
.ch-card:hover { box-shadow: 0 6px 24px rgba(46,109,161,0.3); }
.ch-title { font-size: 1.15rem; font-weight: 700; color: #bde0fe; margin-bottom: 4px; }
.ch-meta { font-size: 0.88rem; color: #90c7f4; }
.ch-badge {
    display: inline-block;
    background: #1e3a5f;
    color: #90c7f4;
    border-radius: 8px;
    padding: 2px 10px;
    font-size: 0.8rem;
    margin-right: 6px;
    font-weight: 600;
}

/* Streamlit button overrides */
div.stButton > button {
    background: linear-gradient(135deg, #2d6a4f, #40916c);
    color: #d8f3dc;
    border: none;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    transition: all 0.2s;
    box-shadow: 0 2px 8px rgba(64,145,108,0.3);
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #40916c, #52b788);
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(82,183,136,0.4);
}

/* Progress bar color */
.stProgress > div > div { background-color: #52b788 !important; }

div[data-testid="stHorizontalBlock"] { gap: 16px; }
</style>
""", unsafe_allow_html=True)

# ─── Session state defaults ───────────────────────────────────────────────────
if "user_name" not in st.session_state:
    st.session_state.user_name = "Alex Johnson"
if "school" not in st.session_state:
    st.session_state.school = "Green Valley High School"
if "eco_points" not in st.session_state:
    st.session_state.eco_points = 180
if "streak" not in st.session_state:
    st.session_state.streak = 7

# ─── Top Navigation Bar ────────────────────────────────────────────────────────
st.markdown("""
<div class="top-nav">
    <div class="nav-logo">🌱 EcoLearn</div>
    <div class="nav-right">
        <span style="color:#95d5b2;font-size:0.9rem;align-self:center;">
            🌱 <strong style="color:#b7e4c7;">{pts}</strong> pts &nbsp;|&nbsp; 
            🔥 <strong style="color:#b7e4c7;">{streak}</strong>-day streak
        </span>
    </div>
</div>
""".format(pts=st.session_state.eco_points, streak=st.session_state.streak),
unsafe_allow_html=True)

# Top-right action buttons
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([5, 1.2, 1, 1])
with nav_col2:
    if st.button("👤 Dashboard"):
        st.switch_page("pages/dashboard.py")
with nav_col3:
    if st.button("⚙️ Settings"):
        st.info("Settings panel coming soon!")
with nav_col4:
    if st.button("🚪 Logout"):
        st.warning("You have been logged out.")

# ─── Main Tab Navigation Bar ──────────────────────────────────────────────────
st.markdown('<div class="section-heading" style="border:none;padding:0;margin-top:0;font-size:1rem;color:#52b788;">🗂️ Navigate</div>', unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📘 Learning", "🌿 Habits", "👥 Teams",
    "🏆 Challenges", "🎮 Games", "📊 Leaderboard", "🌐 Language"
])

with tab1:
    st.markdown("### 📘 Learning Center")
    st.write("Explore interactive lessons on climate, biodiversity, water, and waste.")
    if st.button("Go to Learning →", key="tab_learn"):
        st.switch_page("pages/learning.py")

with tab2:
    st.markdown("### 🌿 Eco Habits")
    st.write("Build daily eco-friendly habits and earn streak rewards.")
    if st.button("Go to Habits →", key="tab_habits"):
        st.switch_page("pages/habits.py")

with tab3:
    st.markdown("### 👥 Teams")
    st.write("Join or create eco teams and collaborate on challenges.")
    if st.button("Go to Teams →", key="tab_teams"):
        st.switch_page("pages/teams.py")

with tab4:
    st.markdown("### 🏆 Challenges")
    st.write("Take on real-world eco challenges and earn points.")
    if st.button("Go to Challenges →", key="tab_challenges"):
        st.switch_page("pages/challenges.py")

with tab5:
    st.markdown("### 🎮 Games")
    st.write("Play eco-themed trivia and mini-games.")
    if st.button("Go to Games →", key="tab_games"):
        st.switch_page("pages/games.py")

with tab6:
    st.markdown("### 📊 Leaderboard")
    st.write("See top eco warriors ranked by their points.")
    if st.button("Go to Leaderboard →", key="tab_leader"):
        st.switch_page("pages/leaderboard.py")

with tab7:
    st.markdown("### 🌐 Language")
    st.write("Choose your preferred language for the platform.")
    if st.button("Go to Language →", key="tab_lang"):
        st.switch_page("pages/language.py")

st.divider()

# ─── Hero Section ─────────────────────────────────────────────────────────────
hero_left, hero_right = st.columns([3, 2], gap="large")
with hero_left:
    st.markdown("""
<div class="hero-quote">
    <div style="font-size:2rem;margin-bottom:12px;">🌍</div>
    <em>"The Earth does not belong to us, we belong to the Earth. Every action you take today 
    shapes the world our grandchildren inherit tomorrow."</em>
    <div class="hero-author">— EcoLearn Mission</div>
    <br>
    <div style="font-size:0.95rem; color:#74c69d;">
        🌱 Join <strong style="color:#b7e4c7;">12,400+</strong> students already making a difference.
    </div>
</div>
""", unsafe_allow_html=True)

with hero_right:
    st.image(
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80",
        use_container_width=True,
        caption="🌿 Our planet. Our responsibility."
    )

st.divider()

# ─── CTA Cards: Join Teams + Eco Habits ──────────────────────────────────────
st.markdown('<div class="section-heading">🚀 Get Started Now</div>', unsafe_allow_html=True)

cta1, cta2 = st.columns(2, gap="large")
with cta1:
    st.markdown("""
<div class="cta-card">
    <div class="cta-icon">👥</div>
    <div class="cta-title">Join an Eco Team</div>
    <div class="cta-desc">Collaborate with classmates on green missions and multiply your impact together.</div>
</div>
""", unsafe_allow_html=True)
    st.write("")
    if st.button("👥 Join Teams Now", key="cta_teams", use_container_width=True):
        st.switch_page("pages/teams.py")

with cta2:
    st.markdown("""
<div class="cta-card" style="border-color:#52b788;background:linear-gradient(135deg,#1a3d2b,#245c3f);">
    <div class="cta-icon">🌿</div>
    <div class="cta-title">Build Eco Habits</div>
    <div class="cta-desc">Track your daily eco-actions, build streaks, and earn bonus eco points every day.</div>
</div>
""", unsafe_allow_html=True)
    st.write("")
    if st.button("🌿 Start My Habits", key="cta_habits", use_container_width=True):
        st.switch_page("pages/habits.py")

st.divider()

# ─── Interactive Learning Paths ───────────────────────────────────────────────
st.markdown('<div class="section-heading">📚 Interactive Learning Paths</div>', unsafe_allow_html=True)

learning_paths = [
    {
        "icon": "🌍", "title": "Climate Change",
        "progress": 60, "videos": 5, "lessons": 12,
        "desc": "Understand the science, causes and solutions to climate change.",
        "color": "#e63946", "key": "cc"
    },
    {
        "icon": "🦋", "title": "Biodiversity",
        "progress": 40, "videos": 3, "lessons": 8,
        "desc": "Discover Earth's rich variety of life and why it matters.",
        "color": "#f4a261", "key": "bio"
    },
    {
        "icon": "💧", "title": "Water Conservation",
        "progress": 25, "videos": 2, "lessons": 6,
        "desc": "Learn why water is precious and simple steps to conserve it.",
        "color": "#457b9d", "key": "water"
    },
    {
        "icon": "♻️", "title": "Waste Management",
        "progress": 80, "videos": 6, "lessons": 15,
        "desc": "Master the art of reducing, reusing and recycling waste.",
        "color": "#2d6a4f", "key": "waste"
    },
    {
        "icon": "☀️", "title": "Renewable Energy",
        "progress": 15, "videos": 4, "lessons": 10,
        "desc": "Explore solar, wind and other clean energy alternatives.",
        "color": "#e9c46a", "key": "energy"
    },
    {
        "icon": "🌱", "title": "Sustainable Agriculture",
        "progress": 35, "videos": 3, "lessons": 9,
        "desc": "Discover how we can feed the world without destroying it.",
        "color": "#606c38", "key": "agri"
    },
]

for i in range(0, len(learning_paths), 2):
    cols = st.columns(2, gap="large")
    for j, col in enumerate(cols):
        if i + j < len(learning_paths):
            p = learning_paths[i + j]
            with col:
                st.markdown(f"""
<div class="lp-card">
    <div style="font-size:2rem;margin-bottom:4px;">{p['icon']}</div>
    <div class="lp-title">{p['title']}</div>
    <div class="lp-meta">{p['desc']}</div>
    <div style="margin:10px 0;">
        <span class="badge">🎥 {p['videos']} Videos</span>
        <span class="badge">📘 {p['lessons']} Lessons</span>
    </div>
</div>
""", unsafe_allow_html=True)
                st.progress(p["progress"] / 100)
                st.caption(f"✅ {p['progress']}% completed")
                if st.button(f"▶️ Continue Learning", key=f"lp_{p['key']}",
                             use_container_width=True):
                    st.switch_page("pages/learning.py")

st.divider()

# ─── Real World Eco Challenges ────────────────────────────────────────────────
st.markdown('<div class="section-heading">🌱 Real World Eco Challenges</div>', unsafe_allow_html=True)

challenges_data = [
    {
        "icon": "🌳", "title": "Tree Planting Mission",
        "desc": "Plant a tree in your neighbourhood and upload a photo as proof.",
        "participants": 1247, "points": 50, "deadline": "Mar 15", "key": "tree"
    },
    {
        "icon": "♻️", "title": "Waste Segregation Week",
        "desc": "Segregate your household waste correctly for 7 days in a row.",
        "participants": 983, "points": 40, "deadline": "Mar 22", "key": "waste"
    },
    {
        "icon": "🧹", "title": "Clean-Up Drive",
        "desc": "Organise or join a community clean-up for parks, beaches or roads.",
        "participants": 2104, "points": 60, "deadline": "Mar 10", "key": "cleanup"
    },
    {
        "icon": "💧", "title": "Water Saving Sprint",
        "desc": "Reduce your daily water usage by 20% and track it for a week.",
        "participants": 756, "points": 35, "deadline": "Apr 1", "key": "water"
    },
    {
        "icon": "🚲", "title": "Cycle to School Week",
        "desc": "Use a cycle or walk instead of a car to school for 5 days.",
        "participants": 1512, "points": 45, "deadline": "Mar 28", "key": "cycle"
    },
]

for i in range(0, len(challenges_data), 2):
    cols = st.columns(2, gap="large")
    for j, col in enumerate(cols):
        if i + j < len(challenges_data):
            c = challenges_data[i + j]
            with col:
                st.markdown(f"""
<div class="ch-card">
    <div style="font-size:2rem;margin-bottom:4px;">{c['icon']}</div>
    <div class="ch-title">{c['title']}</div>
    <div class="ch-meta">{c['desc']}</div>
    <div style="margin:10px 0;">
        <span class="ch-badge">👥 {c['participants']:,} joined</span>
        <span class="ch-badge">🌱 +{c['points']} pts</span>
        <span class="ch-badge">📅 Ends {c['deadline']}</span>
    </div>
</div>
""", unsafe_allow_html=True)
                if st.button("✅ Join Now", key=f"ch_{c['key']}",
                             use_container_width=True):
                    st.switch_page("pages/challenges.py")

# ─── Footer ───────────────────────────────────────────────────────────────────
st.divider()
st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 8px 0;">
    🌱 <strong>EcoLearn</strong> &nbsp;|&nbsp; Empowering the next generation of eco-warriors
    &nbsp;|&nbsp; Made with 💚 for Planet Earth
</div>
""", unsafe_allow_html=True)
