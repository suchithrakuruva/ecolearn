import streamlit as st

st.set_page_config(page_title="Learning Center | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.lesson-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1px solid #2d6a4f; border-radius: 14px;
    padding: 16px 20px; margin-bottom: 10px;
    display: flex; justify-content: space-between; align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2); transition: box-shadow 0.2s;
}
.lesson-card:hover { box-shadow: 0 6px 20px rgba(82,183,136,0.2); }
.video-card {
    background: linear-gradient(135deg, #1a2744, #1e3a5f);
    border: 1px solid #2e6da1; border-radius: 14px;
    padding: 16px 20px; margin-bottom: 10px;
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
.path-header {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 20px; padding: 28px 32px;
    margin-bottom: 24px; border: 1px solid #40916c;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ─── Back navigation ─────────────────────────────────────────────────────────
bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

# ─── Path selection ──────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">📚 Learning Center</div>', unsafe_allow_html=True)

paths = {
    "🌍 Climate Change": {
        "color": "#e63946", "progress": 60,
        "desc": "Understand why Earth's climate is changing and what we can do about it.",
        "videos": [
            ("What is Climate Change?", "https://www.youtube.com/watch?v=G4H1N_yXBiA", True),
            ("Greenhouse Effect Explained", "https://www.youtube.com/watch?v=SN5-DnOHQmE", True),
            ("Effects on Wildlife", "https://www.youtube.com/watch?v=DCGiOzOLOvU", False),
            ("Climate Action & Solutions", "https://www.youtube.com/watch?v=ZAsyei5S7ME", False),
            ("Youth Climate Leaders", "https://www.youtube.com/watch?v=TMrtLsQbaok", False),
        ],
        "lessons": [
            ("Introduction to Climate Science", True),
            ("Carbon Cycle & Emissions", True),
            ("Greenhouse Gases", True),
            ("Global Temperature Rise", True),
            ("Ocean Acidification", True),
            ("Extreme Weather Events", True),
            ("Impact on Ecosystems", False),
            ("Renewable Energy Solutions", False),
            ("International Climate Agreements", False),
            ("Individual vs Collective Action", False),
            ("Carbon Footprint Calculator", False),
            ("Project: My Climate Pledge", False),
        ]
    },
    "🦋 Biodiversity": {
        "color": "#f4a261", "progress": 40,
        "desc": "Explore Earth's amazing variety of life and why protecting it matters.",
        "videos": [
            ("What is Biodiversity?", "https://www.youtube.com/watch?v=GK_vRtHJZu4", True),
            ("Endangered Species", "https://www.youtube.com/watch?v=5mUT9Q8hPLY", False),
            ("Rainforest Ecosystems", "https://www.youtube.com/watch?v=Ic9ZbVbHBas", False),
        ],
        "lessons": [
            ("What is Biodiversity?", True),
            ("Ecosystems & Food Webs", True),
            ("Endangered vs Extinct", True),
            ("Habitat Destruction", False),
            ("Conservation Efforts", False),
            ("How You Can Help", False),
            ("Marine Biodiversity", False),
            ("Quiz: Test Your Knowledge", False),
        ]
    },
    "💧 Water Conservation": {
        "color": "#457b9d", "progress": 25,
        "desc": "Discover why fresh water is precious and simple ways to conserve it.",
        "videos": [
            ("The Water Crisis", "https://www.youtube.com/watch?v=FCMbsKNDFbI", True),
            ("Water-Saving Tips", "https://www.youtube.com/watch?v=OWQFgEwUfCU", False),
        ],
        "lessons": [
            ("Earth's Water Supply", True),
            ("Water Scarcity Facts", False),
            ("Daily Water Footprint", False),
            ("Water-Saving Habits", False),
            ("Rainwater Harvesting", False),
            ("Quiz: Water Wisdom", False),
        ]
    },
    "♻️ Waste Management": {
        "color": "#2d6a4f", "progress": 80,
        "desc": "Master reduce, reuse, and recycle to keep our planet clean.",
        "videos": [
            ("Zero Waste Lifestyle", "https://www.youtube.com/watch?v=pF72px2R3Hg", True),
            ("Segregation 101", "https://www.youtube.com/watch?v=_gd-0GVkWQc", True),
            ("Composting at Home", "https://www.youtube.com/watch?v=egyNJ7xPyoQ", True),
            ("Plastic Pollution", "https://www.youtube.com/watch?v=RS7IiCCDRks", True),
            ("E-Waste Management", "https://www.youtube.com/watch?v=ITCNVgGWBlk", True),
            ("Upcycling Ideas", "https://www.youtube.com/watch?v=bR_oGnlNMuU", False),
        ],
        "lessons": [
            ("Types of Waste", True), ("The 3 R's", True),
            ("Dry vs Wet Waste", True), ("Composting", True),
            ("Plastic-Free Living", True), ("E-Waste Dangers", True),
            ("Waste to Energy", True), ("Zero Waste Goals", True),
            ("Industry & Waste", True), ("Community Action", True),
            ("My Waste Audit", True), ("Final Challenge", True),
            ("Advanced Techniques", False), ("Policy & Advocacy", False),
            ("Project: Waste-Free Week", False),
        ]
    },
    "☀️ Renewable Energy": {
        "color": "#e9c46a", "progress": 15,
        "desc": "Explore solar, wind, and other clean energy sources for the future.",
        "videos": [
            ("How Solar Panels Work", "https://www.youtube.com/watch?v=xKxrkht7CpY", True),
            ("Wind Energy", "https://www.youtube.com/watch?v=xy9nj94xvpA", False),
        ],
        "lessons": [
            ("Why Clean Energy?", True),
            ("Solar Power Basics", False),
            ("Wind Energy", False),
            ("Hydro & Tidal Power", False),
            ("Geothermal Energy", False),
            ("Energy Storage", False),
            ("Green Homes", False),
            ("Future of Energy", False),
            ("Energy Quiz", False),
            ("My Energy Pledge", False),
        ]
    },
}

selected_path = st.selectbox(
    "Choose a Learning Path:",
    list(paths.keys()),
    index=0
)

path = paths[selected_path]

# ─── Path Header ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="path-header">
    <div style="font-size:2rem;font-weight:800;color:#d8f3dc;margin-bottom:6px;">{selected_path}</div>
    <div style="color:#95d5b2;margin-bottom:16px;">{path['desc']}</div>
    <div>
        <span style="background:rgba(0,0,0,0.2);border:1px solid #52b788;border-radius:8px;
                    padding:4px 12px;font-size:0.85rem;color:#b7e4c7;margin-right:8px;">
            🎥 {len(path['videos'])} Videos
        </span>
        <span style="background:rgba(0,0,0,0.2);border:1px solid #52b788;border-radius:8px;
                    padding:4px 12px;font-size:0.85rem;color:#b7e4c7;margin-right:8px;">
            📘 {len(path['lessons'])} Lessons
        </span>
        <span style="background:rgba(0,0,0,0.2);border:1px solid #52b788;border-radius:8px;
                    padding:4px 12px;font-size:0.85rem;color:#b7e4c7;">
            ✅ {path['progress']}% Complete
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

st.progress(path["progress"] / 100)
st.caption(f"Overall Progress: {path['progress']}%")

st.divider()

# ─── Videos + Lessons columns ────────────────────────────────────────────────
vid_col, less_col = st.columns([3, 2], gap="large")

with vid_col:
    st.markdown('<div class="section-heading">🎥 Videos</div>', unsafe_allow_html=True)

    # Show the first unwatched (or first) video
    next_video = next((v for v in path["videos"] if not v[2]), path["videos"][0])
    st.markdown(f"""
<div style="font-weight:700;color:#b7e4c7;margin-bottom:8px;font-size:1rem;">
    ▶️ Now Playing: {next_video[0]}
</div>""", unsafe_allow_html=True)
    st.video(next_video[1])

    st.markdown('<div style="margin-top:16px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">All Videos in This Path</div>', unsafe_allow_html=True)
    for v_title, v_url, watched in path["videos"]:
        icon = "✅" if watched else "▶️"
        color = "#52b788" if watched else "#b7e4c7"
        st.markdown(f"""
<div class="video-card" style="opacity:{'1' if not watched else '0.85'};">
    <span style="color:{color};font-weight:700;">{icon} {v_title}</span>
    <span style="color:{'#52b788' if watched else '#90c7f4'};font-size:0.82rem;float:right;">
        {'Watched' if watched else 'Up next'}
    </span>
</div>""", unsafe_allow_html=True)

with less_col:
    st.markdown('<div class="section-heading">📘 Lessons</div>', unsafe_allow_html=True)
    for i, (lesson, done) in enumerate(path["lessons"], 1):
        icon = "✅" if done else f"📄"
        bg = "#1b4332" if done else "#152b22"
        color = "#52b788" if done else "#b7e4c7"
        st.markdown(f"""
<div class="lesson-card" style="background:{bg};">
    <span>{icon} &nbsp;<span style="color:{color};font-weight:{'700' if not done else '400'};">
        {i}. {lesson}
    </span></span>
    <span style="font-size:0.8rem;color:{'#52b788' if done else '#555'};">
        {'Done' if done else ''}
    </span>
</div>""", unsafe_allow_html=True)

st.divider()
cl, _ = st.columns([2, 3])
with cl:
    next_lesson = next((l for l in path["lessons"] if not l[1]), None)
    if next_lesson:
        if st.button(f"▶️ Continue: {next_lesson[0]}", use_container_width=True):
            st.success(f"Opening: {next_lesson[0]}...")
    else:
        st.success("🎉 You've completed all lessons in this path!")

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 4px;">
    🌱 <strong>EcoLearn</strong> — Learn. Act. Inspire.
</div>""", unsafe_allow_html=True)
