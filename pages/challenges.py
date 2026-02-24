import streamlit as st

st.set_page_config(page_title="Eco Challenges | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.ch-card {
    background: linear-gradient(135deg, #1a2744, #1e3a5f);
    border: 1.5px solid #2e6da1; border-radius: 18px;
    padding: 24px 26px; margin-bottom: 16px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.3);
    transition: box-shadow 0.2s, transform 0.2s;
}
.ch-card:hover { box-shadow: 0 8px 28px rgba(46,109,161,0.35); transform: translateY(-2px); }
.ch-title { font-size: 1.25rem; font-weight: 800; color: #bde0fe; margin-bottom: 6px; }
.ch-desc { font-size: 0.92rem; color: #90c7f4; margin-bottom: 12px; line-height: 1.6; }
.ch-badge {
    display: inline-block; background: rgba(46,109,161,0.35);
    color: #90c7f4; border-radius: 8px; border: 1px solid #2e6da1;
    padding: 3px 12px; font-size: 0.82rem; margin-right: 8px; margin-bottom: 6px; font-weight: 600;
}
div.stButton > button {
    background: linear-gradient(135deg, #2d6a4f, #40916c);
    color: #d8f3dc; border: none; border-radius: 10px;
    padding: 8px 20px; font-weight: 600; font-family: 'Poppins', sans-serif;
    transition: all 0.2s; box-shadow: 0 2px 8px rgba(64,145,108,0.3);
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #40916c, #52b788);
    transform: translateY(-2px);
}
.step-card {
    background: #152b22; border: 1px solid #2d6a4f;
    border-radius: 10px; padding: 12px 16px; margin-bottom: 8px;
    color: #b7e4c7; font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# ─── Back ─────────────────────────────────────────────────────────────────────
bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">🌱 Real World Eco Challenges</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:20px;">
    Take on real eco-challenges, make a difference in your community, and earn eco points! 🌍
</div>""", unsafe_allow_html=True)

challenges = [
    {
        "icon": "🌳", "title": "Tree Planting Mission",
        "desc": "Plant at least one tree in your neighbourhood, school, or local park. Upload a photo with your name card as proof of planting.",
        "participants": 1247, "points": 50, "deadline": "Mar 15, 2026",
        "difficulty": "⭐⭐ Easy", "duration": "1 Day",
        "steps": ["Find a suitable spot", "Get a sapling from a nursery", "Plant it with care", "Water it daily", "Upload your proof photo"],
        "key": "tree"
    },
    {
        "icon": "♻️", "title": "Waste Segregation Week",
        "desc": "Correctly segregate your home waste into dry, wet, and hazardous categories every day for 7 consecutive days.",
        "participants": 983, "points": 40, "deadline": "Mar 22, 2026",
        "difficulty": "⭐⭐⭐ Medium", "duration": "7 Days",
        "steps": ["Get 3 bins (dry/wet/hazardous)", "Label each bin clearly", "Segregate daily", "Log your progress each night", "Submit your week summary"],
        "key": "waste"
    },
    {
        "icon": "🧹", "title": "Community Clean-Up Drive",
        "desc": "Organise or participate in a local clean-up event at a park, beach, road, or school campus.",
        "participants": 2104, "points": 60, "deadline": "Mar 10, 2026",
        "difficulty": "⭐⭐ Easy", "duration": "Half Day",
        "steps": ["Choose a location", "Gather gloves & bags", "Recruit friends or classmates", "Clean the area for 2+ hours", "Weigh/estimate the waste collected", "Post a group photo"],
        "key": "cleanup"
    },
    {
        "icon": "💧", "title": "Water Saving Sprint",
        "desc": "Track and reduce your daily water usage by at least 20% compared to your baseline for one full week.",
        "participants": 756, "points": 35, "deadline": "Apr 1, 2026",
        "difficulty": "⭐⭐⭐ Medium", "duration": "7 Days",
        "steps": ["Measure your current water use", "Set a 20% reduction target", "Practice short showers", "Fix dripping taps", "Use water-saving techniques", "Log daily usage", "Submit your data sheet"],
        "key": "water"
    },
    {
        "icon": "🚲", "title": "Cycle to School Week",
        "desc": "Travel to school by cycle, walk, or public transport instead of a private vehicle for 5 consecutive school days.",
        "participants": 1512, "points": 45, "deadline": "Mar 28, 2026",
        "difficulty": "⭐⭐ Easy", "duration": "5 Days",
        "steps": ["Plan your route in advance", "Use a cycle or walk each day", "Track your km saved", "Calculate CO₂ avoided", "Share your experience"],
        "key": "cycle"
    },
    {
        "icon": "🌿", "title": "Plastic-Free Day Challenge",
        "desc": "Go completely plastic-free for one entire day — no single-use plastics at all.",
        "participants": 3212, "points": 30, "deadline": "Apr 7, 2026",
        "difficulty": "⭐ Beginner", "duration": "1 Day",
        "steps": ["List all plastic items you use daily", "Find reusable alternatives", "Go plastic-free for the full day", "Log any slips and learn", "Share your experience"],
        "key": "plasticfree"
    },
]

# Track joined challenges in session state
if "joined_challenges" not in st.session_state:
    st.session_state.joined_challenges = set()

for ch in challenges:
    st.markdown(f"""
<div class="ch-card">
    <div style="font-size:2.2rem;margin-bottom:6px;">{ch['icon']}</div>
    <div class="ch-title">{ch['title']}</div>
    <div class="ch-desc">{ch['desc']}</div>
    <div>
        <span class="ch-badge">👥 {ch['participants']:,} participants</span>
        <span class="ch-badge">🌱 +{ch['points']} Eco Points</span>
        <span class="ch-badge">📅 Ends {ch['deadline']}</span>
        <span class="ch-badge">🎯 {ch['difficulty']}</span>
        <span class="ch-badge">⏱️ {ch['duration']}</span>
    </div>
</div>""", unsafe_allow_html=True)

    with st.expander(f"📋 How to complete: {ch['title']}"):
        for i, step in enumerate(ch["steps"], 1):
            st.markdown(f"""
<div class="step-card">
    <strong style="color:#52b788;">Step {i}:</strong> {step}
</div>""", unsafe_allow_html=True)

    already_joined = ch["key"] in st.session_state.joined_challenges
    if already_joined:
        st.success(f"✅ You've joined **{ch['title']}**! Check your dashboard for progress.")
    else:
        if st.button(f"✅ Join: {ch['title']}", key=f"join_{ch['key']}", use_container_width=True):
            st.session_state.joined_challenges.add(ch["key"])
            st.session_state.eco_points = st.session_state.get("eco_points", 180) + ch["points"] // 5
            st.success(f"🎉 You've joined **{ch['title']}**! Complete it to earn +{ch['points']} eco points!")
            st.balloons()

    st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:8px 0;">
    🌱 <strong>EcoLearn</strong> — Every challenge is a step towards a greener planet.
</div>""", unsafe_allow_html=True)
