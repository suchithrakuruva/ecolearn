import streamlit as st
import random

st.set_page_config(page_title="Eco Games | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.quiz-card {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 18px; padding: 28px 32px; margin-bottom: 16px;
    border: 1.5px solid #40916c; box-shadow: 0 4px 18px rgba(0,0,0,0.3);
}
.question-text {
    font-size: 1.15rem; font-weight: 700; color: #d8f3dc; margin-bottom: 18px;
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
.score-box {
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    border-radius: 16px; padding: 24px; text-align: center;
    border: 2px solid #52b788; box-shadow: 0 4px 20px rgba(82,183,136,0.2);
}
</style>
""", unsafe_allow_html=True)

bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">🎮 Eco Trivia Quiz</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:20px;">
    Test your eco knowledge! Answer all questions to earn bonus Eco Points. 🌍
</div>""", unsafe_allow_html=True)

questions = [
    {
        "q": "🌍 What is the main cause of global warming?",
        "options": ["Solar flares", "Greenhouse gas emissions", "Ocean currents", "Volcanic eruptions"],
        "answer": "Greenhouse gas emissions",
        "explanation": "Burning fossil fuels releases CO₂ and other greenhouse gases that trap heat in the atmosphere."
    },
    {
        "q": "💧 What percentage of Earth's water is fresh water?",
        "options": ["71%", "50%", "3%", "10%"],
        "answer": "3%",
        "explanation": "Only ~3% of Earth's water is fresh water, and most of it is locked in glaciers."
    },
    {
        "q": "♻️ Which material takes the longest to decompose?",
        "options": ["Paper", "Glass", "Plastic", "Food waste"],
        "answer": "Glass",
        "explanation": "Glass can take up to 1 million years to decompose in nature!"
    },
    {
        "q": "🌳 Which gas do trees absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Methane"],
        "answer": "Carbon Dioxide",
        "explanation": "Trees absorb CO₂ and release oxygen through photosynthesis."
    },
    {
        "q": "☀️ Which is a renewable source of energy?",
        "options": ["Coal", "Natural Gas", "Nuclear Energy", "Solar Energy"],
        "answer": "Solar Energy",
        "explanation": "Solar energy is renewable — the sun provides free, clean energy every day!"
    },
    {
        "q": "🦋 What is the biggest threat to biodiversity?",
        "options": ["Habitat loss", "Hurricanes", "Earthquakes", "Tidal waves"],
        "answer": "Habitat loss",
        "explanation": "Deforestation and urban expansion destroy habitats, making it the #1 threat to biodiversity."
    },
    {
        "q": "🌱 Which country has the largest area of tropical rainforest?",
        "options": ["India", "Congo", "Brazil", "Indonesia"],
        "answer": "Brazil",
        "explanation": "Brazil contains the Amazon rainforest, the world's largest tropical rainforest."
    },
    {
        "q": "🚗 Transport accounts for approximately what % of global CO₂ emissions?",
        "options": ["5%", "16%", "37%", "50%"],
        "answer": "16%",
        "explanation": "Transport (cars, planes, ships) accounts for about 16% of global CO₂ emissions."
    },
]

# Session state for quiz
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if not st.session_state.quiz_submitted:
    for i, q in enumerate(questions):
        st.markdown(f"""
<div class="quiz-card">
    <div class="question-text">Q{i+1}. {q['q']}</div>
</div>""", unsafe_allow_html=True)
        selected = st.radio(
            label=f"Q{i+1}",
            options=q["options"],
            key=f"q_{i}",
            label_visibility="collapsed"
        )
        if selected:
            st.session_state.quiz_answers[i] = selected
        st.markdown("---")

    if st.button("🎯 Submit Quiz!", use_container_width=True):
        st.session_state.quiz_submitted = True
        st.rerun()
else:
    # Show results
    score = sum(1 for i, q in enumerate(questions)
                if st.session_state.quiz_answers.get(i) == q["answer"])
    pts_earned = score * 10

    pct = int(score / len(questions) * 100)
    if pct >= 80:
        grade = "🏆 Eco Champion!"
        color = "#52b788"
    elif pct >= 60:
        grade = "🌿 Eco Warrior!"
        color = "#f4a261"
    else:
        grade = "🌱 Eco Learner!"
        color = "#90c7f4"

    st.markdown(f"""
<div class="score-box">
    <div style="font-size:3rem;margin-bottom:8px;">{grade}</div>
    <div style="font-size:2.5rem;font-weight:800;color:{color};">{score} / {len(questions)}</div>
    <div style="color:#74c69d;margin:8px 0;">You scored {pct}% — Earned <strong style="color:#b7e4c7;">+{pts_earned} Eco Points!</strong></div>
</div>
<br>""", unsafe_allow_html=True)

    if pct >= 80:
        st.balloons()

    st.markdown('<div class="section-heading">📋 Review Your Answers</div>', unsafe_allow_html=True)
    for i, q in enumerate(questions):
        user_ans = st.session_state.quiz_answers.get(i, "Not answered")
        correct = user_ans == q["answer"]
        bg = "#152b22" if correct else "#2d1515"
        border = "#52b788" if correct else "#e63946"
        icon = "✅" if correct else "❌"
        st.markdown(f"""
<div style="background:{bg};border:1.5px solid {border};border-radius:12px;padding:16px 20px;margin-bottom:12px;">
    <div style="font-weight:700;color:#d8f3dc;margin-bottom:6px;">{icon} Q{i+1}. {q['q']}</div>
    <div style="font-size:0.88rem;margin-bottom:4px;">
        Your answer: <strong style="color:{'#52b788' if correct else '#e63946'};">{user_ans}</strong>
    </div>
    {"" if correct else f'<div style="font-size:0.88rem;color:#95d5b2;margin-bottom:4px;">Correct answer: <strong>{q["answer"]}</strong></div>'}
    <div style="font-size:0.83rem;color:#74c69d;margin-top:6px;">💡 {q['explanation']}</div>
</div>""", unsafe_allow_html=True)

    if st.button("🔄 Retake Quiz", use_container_width=True):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers = {}
        st.rerun()

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 4px;">
    🌱 <strong>EcoLearn</strong> — Learn while you play! 🎮
</div>""", unsafe_allow_html=True)

