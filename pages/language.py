import streamlit as st

st.set_page_config(page_title="Language | EcoLearn", layout="wide", initial_sidebar_state="collapsed")

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
.lang-card {
    background: linear-gradient(135deg, #152b22, #1b4332);
    border: 1.5px solid #2d6a4f; border-radius: 14px;
    padding: 18px 22px; text-align: center; cursor: pointer;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2); transition: all 0.2s;
    margin-bottom: 10px;
}
.lang-card:hover { box-shadow: 0 6px 20px rgba(82,183,136,0.25); transform: translateY(-3px); }
.lang-card-selected {
    border-color: #52b788; background: linear-gradient(135deg, #1b4332, #2d6a4f) !important;
    box-shadow: 0 4px 18px rgba(82,183,136,0.35) !important;
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
</style>
""", unsafe_allow_html=True)

bc, _ = st.columns([1, 5])
with bc:
    if st.button("⬅ Back to Hub"):
        st.switch_page("app.py")

st.markdown('<div class="section-heading">🌐 Language Settings</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:#74c69d;font-size:0.95rem;margin-bottom:20px;">
    Choose the language you'd like to use in EcoLearn. More languages are being added! 🌍
</div>""", unsafe_allow_html=True)

if "language" not in st.session_state:
    st.session_state.language = "English"

languages = [
    ("🇬🇧", "English", "Full Support ✅"),
    ("🇮🇳", "Hindi — हिंदी", "Full Support ✅"),
    ("🇮🇳", "Tamil — தமிழ்", "Full Support ✅"),
    ("🇮🇳", "Telugu — తెలుగు", "Partial Support 🟡"),
    ("🇮🇳", "Kannada — ಕನ್ನಡ", "Partial Support 🟡"),
    ("🇮🇳", "Malayalam — മലയാളം", "Partial Support 🟡"),
    ("🇮🇳", "Bengali — বাংলা", "Coming Soon 🔜"),
    ("🇫🇷", "French — Français", "Coming Soon 🔜"),
    ("🇪🇸", "Spanish — Español", "Coming Soon 🔜"),
    ("🇩🇪", "German — Deutsch", "Coming Soon 🔜"),
    ("🇯🇵", "Japanese — 日本語", "Coming Soon 🔜"),
    ("🇨🇳", "Chinese — 中文", "Coming Soon 🔜"),
]

rows = [languages[i:i+3] for i in range(0, len(languages), 3)]
selected = st.session_state.language

for row in rows:
    cols = st.columns(3)
    for col, (flag, lang, support) in zip(cols, row):
        lang_name = lang.split(" —")[0]
        is_selected = lang_name == selected or lang == selected
        border = "#52b788" if is_selected else "#2d6a4f"
        bg_extra = "background:linear-gradient(135deg,#1b4332,#2d6a4f);" if is_selected else ""
        check = "✅ " if is_selected else ""
        with col:
            st.markdown(f"""
<div class="lang-card {'lang-card-selected' if is_selected else ''}"
     style="{bg_extra}border-color:{border};">
    <div style="font-size:2.2rem;">{flag}</div>
    <div style="font-weight:700;color:#d8f3dc;font-size:0.95rem;margin:6px 0;">
        {check}{lang_name}
    </div>
    <div style="font-size:0.78rem;color:#74c69d;">{lang}</div>
    <div style="font-size:0.75rem;margin-top:6px;color:#95d5b2;">{support}</div>
</div>""", unsafe_allow_html=True)
            if not is_selected:
                if st.button(f"Select", key=f"lang_{lang_name}", use_container_width=True):
                    st.session_state.language = lang_name
                    st.success(f"🌐 Language set to **{lang_name}**!")
                    st.rerun()

st.divider()
st.markdown(f"""
<div style="background:linear-gradient(135deg,#1b4332,#2d6a4f);border-radius:14px;
            padding:18px 22px;border:1px solid #40916c;">
    <div style="font-weight:700;color:#b7e4c7;font-size:1rem;">
        🌐 Currently Selected: <strong style="color:#52b788;">{st.session_state.language}</strong>
    </div>
    <div style="font-size:0.85rem;color:#74c69d;margin-top:6px;">
        The platform will use this language for all content, lessons and notifications.
        Translations are AI-assisted and improve over time. 💚
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#52b788;font-size:0.85rem;padding:16px 0 4px;">
    🌱 <strong>EcoLearn</strong> — Learning eco concepts in your language. 🌍
</div>""", unsafe_allow_html=True)

