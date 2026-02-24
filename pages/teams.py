import streamlit as st

st.set_page_config(page_title="Eco Teams | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.team-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1.5px solid #2d6a4f; border-radius: 18px;
    padding: 22px 26px; margin-bottom: 14px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
    transition: box-shadow 0.2s, transform 0.2s;
}
.team-card:hover { box-shadow: 0 8px 28px rgba(82,183,136,0.2); transform: translateY(-2px); }
.team-title { font-size: 1.2rem; font-weight: 800; color: #d8f3dc; margin-bottom: 4px; }
.team-desc { font-size: 0.9rem; color: #74c69d; margin-bottom: 12px; }
.team-badge {
    display: inline-block; background: #2d6a4f;
    color: #b7e4c7; border-radius: 8px; padding: 3px 12px;
    font-size: 0.82rem; margin-right: 8px; margin-bottom: 6px; font-weight: 600;
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
.my-team-section {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 16px; padding: 22px 26px; margin-bottom: 24px;
    border: 1px solid #40916c;
}
</style>
""", unsafe_allow_html=True)

bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">👥 Eco Teams</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:20px;">
    Join a team, collaborate on green missions, and multiply your collective impact! 🌍
</div>""", unsafe_allow_html=True)

if "joined_teams" not in st.session_state:
    st.session_state.joined_teams = set()

# Show My Team if any
if st.session_state.joined_teams:
    team_names = list(st.session_state.joined_teams)
    st.markdown(f"""
<div class="my-team-section">
    <div style="font-size:1.1rem;font-weight:700;color:#b7e4c7;margin-bottom:8px;">
        🏅 My Team(s)
    </div>
    <div style="color:#95d5b2;">You are a member of: <strong style="color:#d8f3dc;">
        {', '.join(team_names)}
    </strong></div>
    <div style="margin-top:8px;font-size:0.85rem;color:#74c69d;">
        🌱 Team activities and missions are tracked on your dashboard.
    </div>
</div>""", unsafe_allow_html=True)

teams_data = [
    {
        "icon": "🌿", "name": "Green Guardians",
        "desc": "A passionate group dedicated to protecting local green spaces and planting trees.",
        "members": 34, "points": 4250, "missions": 12,
        "focus": "Tree Planting & Parks", "rank": "#1 in School",
        "key": "green_guardians"
    },
    {
        "icon": "♻️", "name": "Recyclers United",
        "desc": "Champions of zero-waste living. We tackle plastic pollution and waste segregation.",
        "members": 28, "points": 3680, "missions": 10,
        "focus": "Waste & Recycling", "rank": "#2 in School",
        "key": "recyclers_united"
    },
    {
        "icon": "💧", "name": "Water Warriors",
        "desc": "Fighting water wastage one drop at a time with saving campaigns and awareness drives.",
        "members": 19, "points": 2900, "missions": 8,
        "focus": "Water Conservation", "rank": "#3 in School",
        "key": "water_warriors"
    },
    {
        "icon": "☀️", "name": "Solar Squad",
        "desc": "Advocates for clean and renewable energy in our school and community.",
        "members": 15, "points": 2100, "missions": 6,
        "focus": "Renewable Energy", "rank": "#4 in School",
        "key": "solar_squad"
    },
    {
        "icon": "🦋", "name": "Biodiversity Buddies",
        "desc": "We study and protect the amazing variety of life around us — plants, insects, and birds!",
        "members": 12, "points": 1870, "missions": 5,
        "focus": "Biodiversity & Wildlife", "rank": "#5 in School",
        "key": "bio_buddies"
    },
    {
        "icon": "🌾", "name": "Eco Farmers",
        "desc": "Promoting school gardens, composting, and sustainable food choices.",
        "members": 23, "points": 3100, "missions": 9,
        "focus": "Sustainable Agriculture", "rank": "#3 Overall",
        "key": "eco_farmers"
    },
]

st.markdown('<div class="section-heading">🔍 Browse All Teams</div>', unsafe_allow_html=True)

for team in teams_data:
    st.markdown(f"""
<div class="team-card">
    <div style="font-size:2rem;margin-bottom:6px;">{team['icon']}</div>
    <div class="team-title">{team['name']}</div>
    <div class="team-desc">{team['desc']}</div>
    <div>
        <span class="team-badge">👥 {team['members']} Members</span>
        <span class="team-badge">🌱 {team['points']:,} Team Points</span>
        <span class="team-badge">🎯 {team['missions']} Missions Done</span>
        <span class="team-badge">🏆 {team['rank']}</span>
        <span class="team-badge">🔎 Focus: {team['focus']}</span>
    </div>
</div>""", unsafe_allow_html=True)

    already = team["key"] in st.session_state.joined_teams
    if already:
        st.success(f"✅ You are a member of **{team['name']}**!")
    else:
        if st.button(f"👥 Join {team['name']}", key=f"team_{team['key']}", use_container_width=True):
            st.session_state.joined_teams.add(team["name"])
            st.success(f"🎉 Welcome to **{team['name']}**! Check your dashboard for team missions.")
            st.balloons()
    st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:8px 0;">
    🌱 <strong>EcoLearn</strong> — Stronger together for a greener world.
</div>""", unsafe_allow_html=True)

