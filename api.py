"""
EcoLearn Flask REST API Backend
Run: pip install flask flask-cors
     python api.py
Serves on http://127.0.0.1:5000
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ─── In-memory state ──────────────────────────────────────────────────────────
STATE = {
    "user": {
        "name": "Alex Johnson",
        "school": "Green Valley High School",
        "eco_points": 180,
        "streak": 7,
        "level": 4,
        "level_title": "Eco Warrior",
        "member_since": "Jan 2025",
        "next_level_pts": 120,
    },
    "joined_challenges": set(),
    "completed_habits": set(),
    "joined_teams": set(),
    "quiz_submitted": False,
    "quiz_answers": {},
    "language": "English",
}

# ─── Data ─────────────────────────────────────────────────────────────────────
LEARNING_PATHS = [
    {"icon": "🌍", "title": "Climate Change",     "progress": 60, "videos": 5, "lessons": 12,
     "desc": "Understand the science, causes and solutions to climate change.", "key": "cc"},
    {"icon": "🦋", "title": "Biodiversity",       "progress": 40, "videos": 3, "lessons": 8,
     "desc": "Discover Earth's rich variety of life and why it matters.",       "key": "bio"},
    {"icon": "💧", "title": "Water Conservation", "progress": 25, "videos": 2, "lessons": 6,
     "desc": "Learn why water is precious and simple steps to conserve it.",    "key": "water"},
    {"icon": "♻️", "title": "Waste Management",  "progress": 80, "videos": 6, "lessons": 15,
     "desc": "Master the art of reducing, reusing and recycling waste.",        "key": "waste"},
    {"icon": "☀️", "title": "Renewable Energy",  "progress": 15, "videos": 4, "lessons": 10,
     "desc": "Explore solar, wind and other clean energy alternatives.",         "key": "energy"},
    {"icon": "🌱", "title": "Sustainable Agriculture", "progress": 35, "videos": 3, "lessons": 9,
     "desc": "Discover how we can feed the world without destroying it.",       "key": "agri"},
]

CHALLENGES = [
    {"icon": "🌳", "title": "Tree Planting Mission",
     "desc": "Plant at least one tree in your neighbourhood, school, or local park. Upload a photo with your name card as proof of planting.",
     "participants": 1247, "points": 50, "deadline": "Mar 15, 2026",
     "difficulty": "⭐⭐ Easy", "duration": "1 Day",
     "steps": ["Find a suitable spot", "Get a sapling from a nursery", "Plant it with care", "Water it daily", "Upload your proof photo"],
     "key": "tree"},
    {"icon": "♻️", "title": "Waste Segregation Week",
     "desc": "Correctly segregate your home waste into dry, wet, and hazardous categories every day for 7 consecutive days.",
     "participants": 983, "points": 40, "deadline": "Mar 22, 2026",
     "difficulty": "⭐⭐⭐ Medium", "duration": "7 Days",
     "steps": ["Get 3 bins (dry/wet/hazardous)", "Label each bin clearly", "Segregate daily", "Log your progress each night", "Submit your week summary"],
     "key": "waste"},
    {"icon": "🧹", "title": "Community Clean-Up Drive",
     "desc": "Organise or participate in a local clean-up event at a park, beach, road, or school campus.",
     "participants": 2104, "points": 60, "deadline": "Mar 10, 2026",
     "difficulty": "⭐⭐ Easy", "duration": "Half Day",
     "steps": ["Choose a location", "Gather gloves & bags", "Recruit friends or classmates", "Clean the area for 2+ hours", "Weigh/estimate the waste collected", "Post a group photo"],
     "key": "cleanup"},
    {"icon": "💧", "title": "Water Saving Sprint",
     "desc": "Track and reduce your daily water usage by at least 20% compared to your baseline for one full week.",
     "participants": 756, "points": 35, "deadline": "Apr 1, 2026",
     "difficulty": "⭐⭐⭐ Medium", "duration": "7 Days",
     "steps": ["Measure your current water use", "Set a 20% reduction target", "Practice short showers", "Fix dripping taps", "Use water-saving techniques", "Log daily usage", "Submit your data sheet"],
     "key": "water"},
    {"icon": "🚲", "title": "Cycle to School Week",
     "desc": "Travel to school by cycle, walk, or public transport instead of a private vehicle for 5 consecutive school days.",
     "participants": 1512, "points": 45, "deadline": "Mar 28, 2026",
     "difficulty": "⭐⭐ Easy", "duration": "5 Days",
     "steps": ["Plan your route in advance", "Use a cycle or walk each day", "Track your km saved", "Calculate CO₂ avoided", "Share your experience"],
     "key": "cycle"},
    {"icon": "🌿", "title": "Plastic-Free Day Challenge",
     "desc": "Go completely plastic-free for one entire day — no single-use plastics at all.",
     "participants": 3212, "points": 30, "deadline": "Apr 7, 2026",
     "difficulty": "⭐ Beginner", "duration": "1 Day",
     "steps": ["List all plastic items you use daily", "Find reusable alternatives", "Go plastic-free for the full day", "Log any slips and learn", "Share your experience"],
     "key": "plasticfree"},
]

HABITS = [
    {"icon": "🚰", "title": "Use a Reusable Bottle",     "desc": "Avoid single-use plastic bottles today.",                   "pts": 5,  "key": "bottle"},
    {"icon": "🛍️", "title": "No Plastic Bags",           "desc": "Use cloth or paper bags for all shopping.",                  "pts": 5,  "key": "bags"},
    {"icon": "🚶", "title": "Walk or Cycle",              "desc": "Travel at least one trip by foot or cycle.",                 "pts": 8,  "key": "walk"},
    {"icon": "🌿", "title": "Eat Plant-Based Meal",       "desc": "Have at least one vegetarian or vegan meal.",                "pts": 6,  "key": "plantmeal"},
    {"icon": "💡", "title": "Switch Off Unused Lights",   "desc": "Turn off lights whenever you leave a room.",                 "pts": 4,  "key": "lights"},
    {"icon": "🚿", "title": "Short Shower (< 5 min)",     "desc": "Cut your shower time to under 5 minutes.",                   "pts": 6,  "key": "shower"},
    {"icon": "📰", "title": "Say No to Paper Printouts",  "desc": "Go digital for all notes and assignments today.",            "pts": 4,  "key": "nopaper"},
    {"icon": "♻️", "title": "Segregate Your Waste",      "desc": "Sort your waste into wet, dry and hazardous.",               "pts": 7,  "key": "segregate"},
    {"icon": "🌱", "title": "Water a Plant",              "desc": "Water a plant at home, school or your garden.",              "pts": 3,  "key": "plant"},
    {"icon": "📲", "title": "Share an Eco Tip",           "desc": "Share one eco tip with a friend or on social media.",        "pts": 4,  "key": "ecotip"},
    {"icon": "🍽️", "title": "No Food Waste",             "desc": "Finish your plate and pack leftovers properly.",             "pts": 5,  "key": "foodwaste"},
    {"icon": "🔌", "title": "Unplug Chargers",            "desc": "Unplug all unused chargers and standby devices.",            "pts": 4,  "key": "unplug"},
]

TEAMS = [
    {"icon": "🌿", "name": "Green Guardians",
     "desc": "A passionate group dedicated to protecting local green spaces and planting trees.",
     "members": 34, "points": 4250, "missions": 12, "focus": "Tree Planting & Parks", "rank": "#1 in School", "key": "green_guardians"},
    {"icon": "♻️", "name": "Recyclers United",
     "desc": "Champions of zero-waste living. We tackle plastic pollution and waste segregation.",
     "members": 28, "points": 3680, "missions": 10, "focus": "Waste & Recycling", "rank": "#2 in School", "key": "recyclers_united"},
    {"icon": "💧", "name": "Water Warriors",
     "desc": "Fighting water wastage one drop at a time with saving campaigns and awareness drives.",
     "members": 19, "points": 2900, "missions": 8, "focus": "Water Conservation", "rank": "#3 in School", "key": "water_warriors"},
    {"icon": "☀️", "name": "Solar Squad",
     "desc": "Advocates for clean and renewable energy in our school and community.",
     "members": 15, "points": 2100, "missions": 6, "focus": "Renewable Energy", "rank": "#4 in School", "key": "solar_squad"},
    {"icon": "🦋", "name": "Biodiversity Buddies",
     "desc": "We study and protect the amazing variety of life around us — plants, insects, and birds!",
     "members": 12, "points": 1870, "missions": 5, "focus": "Biodiversity & Wildlife", "rank": "#5 in School", "key": "bio_buddies"},
    {"icon": "🌾", "name": "Eco Farmers",
     "desc": "Promoting school gardens, composting, and sustainable food choices.",
     "members": 23, "points": 3100, "missions": 9, "focus": "Sustainable Agriculture", "rank": "#3 Overall", "key": "eco_farmers"},
]

QUIZ_QUESTIONS = [
    {"q": "🌍 What is the main cause of global warming?",
     "options": ["Solar flares", "Greenhouse gas emissions", "Ocean currents", "Volcanic eruptions"],
     "answer": "Greenhouse gas emissions",
     "explanation": "Burning fossil fuels releases CO₂ and other greenhouse gases that trap heat in the atmosphere."},
    {"q": "💧 What percentage of Earth's water is fresh water?",
     "options": ["71%", "50%", "3%", "10%"],
     "answer": "3%",
     "explanation": "Only ~3% of Earth's water is fresh water, and most of it is locked in glaciers."},
    {"q": "♻️ Which material takes the longest to decompose?",
     "options": ["Paper", "Glass", "Plastic", "Food waste"],
     "answer": "Glass",
     "explanation": "Glass can take up to 1 million years to decompose in nature!"},
    {"q": "🌳 Which gas do trees absorb from the atmosphere?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Methane"],
     "answer": "Carbon Dioxide",
     "explanation": "Trees absorb CO₂ and release oxygen through photosynthesis."},
    {"q": "☀️ Which is a renewable source of energy?",
     "options": ["Coal", "Natural Gas", "Nuclear Energy", "Solar Energy"],
     "answer": "Solar Energy",
     "explanation": "Solar energy is renewable — the sun provides free, clean energy every day!"},
    {"q": "🦋 What is the biggest threat to biodiversity?",
     "options": ["Habitat loss", "Hurricanes", "Earthquakes", "Tidal waves"],
     "answer": "Habitat loss",
     "explanation": "Deforestation and urban expansion destroy habitats, making it the #1 threat to biodiversity."},
    {"q": "🌱 Which country has the largest area of tropical rainforest?",
     "options": ["India", "Congo", "Brazil", "Indonesia"],
     "answer": "Brazil",
     "explanation": "Brazil contains the Amazon rainforest, the world's largest tropical rainforest."},
    {"q": "🚗 Transport accounts for approximately what % of global CO₂ emissions?",
     "options": ["5%", "16%", "37%", "50%"],
     "answer": "16%",
     "explanation": "Transport (cars, planes, ships) accounts for about 16% of global CO₂ emissions."},
]

LEADERBOARD = [
    {"rank": "🥇", "name": "Priya Sharma",  "school": "Green Valley High",   "pts": 850, "badge": "🌍 Climate Expert",  "color": "#FFD700"},
    {"rank": "🥈", "name": "Arjun Mehta",   "school": "Sunrise Academy",     "pts": 822, "badge": "♻️ Recycling Pro",  "color": "#C0C0C0"},
    {"rank": "🥉", "name": "Zara Khan",     "school": "Green Valley High",   "pts": 790, "badge": "💧 Water Warrior",  "color": "#CD7F32"},
    {"rank": "4",  "name": "Riya Patel",    "school": "Bloom International", "pts": 745, "badge": "🦋 Bio Champion",   "color": "#b7e4c7"},
    {"rank": "5",  "name": "Kabir Singh",   "school": "Sunrise Academy",     "pts": 720, "badge": "☀️ Solar Advocate", "color": "#b7e4c7"},
    {"rank": "6",  "name": "Ananya Iyer",   "school": "Green Valley High",   "pts": 695, "badge": "🌱 Habit Builder",  "color": "#b7e4c7"},
    {"rank": "7",  "name": "Dev Kumar",     "school": "Bloom International", "pts": 668, "badge": "🌳 Tree Planter",   "color": "#b7e4c7"},
    {"rank": "8",  "name": "Meera Joshi",   "school": "Green Valley High",   "pts": 650, "badge": "🎮 Quiz Master",    "color": "#b7e4c7"},
    {"rank": "9",  "name": "Alex Johnson",  "school": "Green Valley High",   "pts": 612, "badge": "🔥 Streak King",   "color": "#52b788", "is_me": True},
    {"rank": "10", "name": "Fatima Noor",   "school": "Sunrise Academy",     "pts": 589, "badge": "🏆 Team Leader",   "color": "#b7e4c7"},
    {"rank": "11", "name": "Raj Verma",     "school": "Green Valley High",   "pts": 540, "badge": "🌿 Eco Starter",   "color": "#6c757d"},
    {"rank": "12", "name": "Sara Hussain",  "school": "Bloom International", "pts": 512, "badge": "📘 Quick Learner", "color": "#6c757d"},
    {"rank": "13", "name": "Neel Gupta",    "school": "Sunrise Academy",     "pts": 490, "badge": "🌱 Green Rookie",  "color": "#6c757d"},
    {"rank": "14", "name": "Diya Thomas",   "school": "Green Valley High",   "pts": 475, "badge": "🔋 Energy Saver",  "color": "#6c757d"},
    {"rank": "15", "name": "Vikram Rao",    "school": "Bloom International", "pts": 460, "badge": "🐝 Bee Keeper",    "color": "#6c757d"},
]

LANGUAGES = [
    {"flag": "🇬🇧", "name": "English",                  "native": "English",          "support": "Full Support ✅"},
    {"flag": "🇮🇳", "name": "Hindi",                    "native": "हिंदी",             "support": "Full Support ✅"},
    {"flag": "🇮🇳", "name": "Tamil",                    "native": "தமிழ்",             "support": "Full Support ✅"},
    {"flag": "🇮🇳", "name": "Telugu",                   "native": "తెలుగు",            "support": "Partial Support 🟡"},
    {"flag": "🇮🇳", "name": "Kannada",                  "native": "ಕನ್ನಡ",             "support": "Partial Support 🟡"},
    {"flag": "🇮🇳", "name": "Malayalam",                "native": "മലയാളം",            "support": "Partial Support 🟡"},
    {"flag": "🇮🇳", "name": "Bengali",                  "native": "বাংলা",             "support": "Coming Soon 🔜"},
    {"flag": "🇫🇷", "name": "French",                   "native": "Français",          "support": "Coming Soon 🔜"},
    {"flag": "🇪🇸", "name": "Spanish",                  "native": "Español",           "support": "Coming Soon 🔜"},
    {"flag": "🇩🇪", "name": "German",                   "native": "Deutsch",           "support": "Coming Soon 🔜"},
    {"flag": "🇯🇵", "name": "Japanese",                 "native": "日本語",            "support": "Coming Soon 🔜"},
    {"flag": "🇨🇳", "name": "Chinese",                  "native": "中文",              "support": "Coming Soon 🔜"},
]

LEARNING_PATH_DETAILS = {
    "cc": {
        "label": "🌍 Climate Change",
        "color": "#e63946", "progress": 60,
        "desc": "Understand why Earth's climate is changing and what we can do about it.",
        "videos": [
            {"title": "What is Climate Change?",    "url": "https://www.youtube.com/watch?v=G4H1N_yXBiA", "watched": True},
            {"title": "Greenhouse Effect Explained","url": "https://www.youtube.com/watch?v=SN5-DnOHQmE", "watched": True},
            {"title": "Effects on Wildlife",        "url": "https://www.youtube.com/watch?v=DCGiOzOLOvU", "watched": False},
            {"title": "Climate Action & Solutions", "url": "https://www.youtube.com/watch?v=ZAsyei5S7ME", "watched": False},
            {"title": "Youth Climate Leaders",      "url": "https://www.youtube.com/watch?v=TMrtLsQbaok", "watched": False},
        ],
        "lessons": [
            {"title": "Introduction to Climate Science", "done": True},
            {"title": "Carbon Cycle & Emissions",        "done": True},
            {"title": "Greenhouse Gases",                "done": True},
            {"title": "Global Temperature Rise",         "done": True},
            {"title": "Ocean Acidification",             "done": True},
            {"title": "Extreme Weather Events",          "done": True},
            {"title": "Impact on Ecosystems",            "done": False},
            {"title": "Renewable Energy Solutions",      "done": False},
            {"title": "International Climate Agreements","done": False},
            {"title": "Individual vs Collective Action", "done": False},
            {"title": "Carbon Footprint Calculator",     "done": False},
            {"title": "Project: My Climate Pledge",      "done": False},
        ],
    },
    "bio": {
        "label": "🦋 Biodiversity",
        "color": "#f4a261", "progress": 40,
        "desc": "Explore Earth's amazing variety of life and why protecting it matters.",
        "videos": [
            {"title": "What is Biodiversity?",  "url": "https://www.youtube.com/watch?v=GK_vRtHJZu4", "watched": True},
            {"title": "Endangered Species",     "url": "https://www.youtube.com/watch?v=5mUT9Q8hPLY", "watched": False},
            {"title": "Rainforest Ecosystems",  "url": "https://www.youtube.com/watch?v=Ic9ZbVbHBas", "watched": False},
        ],
        "lessons": [
            {"title": "What is Biodiversity?",   "done": True},
            {"title": "Ecosystems & Food Webs",  "done": True},
            {"title": "Endangered vs Extinct",   "done": True},
            {"title": "Habitat Destruction",     "done": False},
            {"title": "Conservation Efforts",    "done": False},
            {"title": "How You Can Help",         "done": False},
            {"title": "Marine Biodiversity",     "done": False},
            {"title": "Quiz: Test Your Knowledge","done": False},
        ],
    },
    "water": {
        "label": "💧 Water Conservation",
        "color": "#457b9d", "progress": 25,
        "desc": "Discover why fresh water is precious and simple ways to conserve it.",
        "videos": [
            {"title": "The Water Crisis",   "url": "https://www.youtube.com/watch?v=FCMbsKNDFbI", "watched": True},
            {"title": "Water-Saving Tips",  "url": "https://www.youtube.com/watch?v=OWQFgEwUfCU", "watched": False},
        ],
        "lessons": [
            {"title": "Earth's Water Supply",  "done": True},
            {"title": "Water Scarcity Facts",  "done": False},
            {"title": "Daily Water Footprint", "done": False},
            {"title": "Water-Saving Habits",   "done": False},
            {"title": "Rainwater Harvesting",  "done": False},
            {"title": "Quiz: Water Wisdom",    "done": False},
        ],
    },
    "waste": {
        "label": "♻️ Waste Management",
        "color": "#2d6a4f", "progress": 80,
        "desc": "Master reduce, reuse, and recycle to keep our planet clean.",
        "videos": [
            {"title": "Zero Waste Lifestyle", "url": "https://www.youtube.com/watch?v=pF72px2R3Hg", "watched": True},
            {"title": "Segregation 101",      "url": "https://www.youtube.com/watch?v=_gd-0GVkWQc", "watched": True},
            {"title": "Composting at Home",   "url": "https://www.youtube.com/watch?v=egyNJ7xPyoQ", "watched": True},
            {"title": "Plastic Pollution",    "url": "https://www.youtube.com/watch?v=RS7IiCCDRks", "watched": True},
            {"title": "E-Waste Management",   "url": "https://www.youtube.com/watch?v=ITCNVgGWBlk", "watched": True},
            {"title": "Upcycling Ideas",      "url": "https://www.youtube.com/watch?v=bR_oGnlNMuU", "watched": False},
        ],
        "lessons": [
            {"title": "Types of Waste",      "done": True}, {"title": "The 3 R's",           "done": True},
            {"title": "Dry vs Wet Waste",    "done": True}, {"title": "Composting",           "done": True},
            {"title": "Plastic-Free Living", "done": True}, {"title": "E-Waste Dangers",      "done": True},
            {"title": "Waste to Energy",     "done": True}, {"title": "Zero Waste Goals",     "done": True},
            {"title": "Industry & Waste",    "done": True}, {"title": "Community Action",     "done": True},
            {"title": "My Waste Audit",      "done": True}, {"title": "Final Challenge",     "done": True},
            {"title": "Advanced Techniques", "done": False},{"title": "Policy & Advocacy",   "done": False},
            {"title": "Project: Waste-Free Week","done": False},
        ],
    },
    "energy": {
        "label": "☀️ Renewable Energy",
        "color": "#e9c46a", "progress": 15,
        "desc": "Explore solar, wind, and other clean energy sources for the future.",
        "videos": [
            {"title": "How Solar Panels Work", "url": "https://www.youtube.com/watch?v=xKxrkht7CpY", "watched": True},
            {"title": "Wind Energy",           "url": "https://www.youtube.com/watch?v=xy9nj94xvpA", "watched": False},
        ],
        "lessons": [
            {"title": "Why Clean Energy?",    "done": True},
            {"title": "Solar Power Basics",   "done": False},
            {"title": "Wind Energy",          "done": False},
            {"title": "Hydro & Tidal Power",  "done": False},
            {"title": "Geothermal Energy",    "done": False},
            {"title": "Energy Storage",       "done": False},
            {"title": "Green Homes",          "done": False},
            {"title": "Future of Energy",     "done": False},
            {"title": "Energy Quiz",          "done": False},
            {"title": "My Energy Pledge",     "done": False},
        ],
    },
    "agri": {
        "label": "🌱 Sustainable Agriculture",
        "color": "#606c38", "progress": 35,
        "desc": "Discover how we can feed the world without destroying it.",
        "videos": [
            {"title": "What is Sustainable Farming?", "url": "https://www.youtube.com/watch?v=gLOLGsKA6XQ", "watched": True},
            {"title": "Permaculture Basics",          "url": "https://www.youtube.com/watch?v=QUgO7bYAWCY", "watched": False},
            {"title": "Food Waste Crisis",            "url": "https://www.youtube.com/watch?v=ishA6kry8nc", "watched": False},
        ],
        "lessons": [
            {"title": "Feeding the World",           "done": True},
            {"title": "Soil Health & Farming",       "done": True},
            {"title": "Organic Farming Basics",      "done": True},
            {"title": "Water in Agriculture",        "done": False},
            {"title": "Permaculture",                "done": False},
            {"title": "Food Waste Reduction",        "done": False},
            {"title": "School Garden Project",       "done": False},
            {"title": "Composting Deep Dive",        "done": False},
            {"title": "Final: My Food Pledge",       "done": False},
        ],
    },
}

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/api/user", methods=["GET"])
def get_user():
    return jsonify(STATE["user"])


@app.route("/api/learning-paths", methods=["GET"])
def get_learning_paths():
    return jsonify(LEARNING_PATHS)


@app.route("/api/learning-paths/<key>", methods=["GET"])
def get_learning_path_detail(key):
    path = LEARNING_PATH_DETAILS.get(key)
    if not path:
        return jsonify({"error": "Not found"}), 404
    return jsonify(path)


@app.route("/api/challenges", methods=["GET"])
def get_challenges():
    result = []
    for ch in CHALLENGES:
        item = dict(ch)
        item["joined"] = ch["key"] in STATE["joined_challenges"]
        result.append(item)
    return jsonify(result)


@app.route("/api/challenges/<key>/join", methods=["POST"])
def join_challenge(key):
    challenge = next((c for c in CHALLENGES if c["key"] == key), None)
    if not challenge:
        return jsonify({"error": "Not found"}), 404
    if key not in STATE["joined_challenges"]:
        STATE["joined_challenges"].add(key)
        STATE["user"]["eco_points"] += challenge["points"] // 5
    return jsonify({"success": True, "eco_points": STATE["user"]["eco_points"]})


@app.route("/api/habits", methods=["GET"])
def get_habits():
    result = []
    for h in HABITS:
        item = dict(h)
        item["completed"] = h["key"] in STATE["completed_habits"]
        result.append(item)
    return jsonify(result)


@app.route("/api/habits/<key>/complete", methods=["POST"])
def complete_habit(key):
    habit = next((h for h in HABITS if h["key"] == key), None)
    if not habit:
        return jsonify({"error": "Not found"}), 404
    if key not in STATE["completed_habits"]:
        STATE["completed_habits"].add(key)
        STATE["user"]["eco_points"] += habit["pts"]
    return jsonify({"success": True, "eco_points": STATE["user"]["eco_points"]})


@app.route("/api/teams", methods=["GET"])
def get_teams():
    result = []
    for t in TEAMS:
        item = dict(t)
        item["joined"] = t["key"] in STATE["joined_teams"]
        result.append(item)
    return jsonify(result)


@app.route("/api/teams/<key>/join", methods=["POST"])
def join_team(key):
    team = next((t for t in TEAMS if t["key"] == key), None)
    if not team:
        return jsonify({"error": "Not found"}), 404
    STATE["joined_teams"].add(key)
    return jsonify({"success": True, "team_name": team["name"]})


@app.route("/api/games/questions", methods=["GET"])
def get_questions():
    return jsonify(QUIZ_QUESTIONS)


@app.route("/api/games/submit", methods=["POST"])
def submit_quiz():
    data = request.get_json()
    answers = data.get("answers", {})  # {index: selected_option}
    score = 0
    results = []
    for i, q in enumerate(QUIZ_QUESTIONS):
        user_ans = answers.get(str(i), "")
        correct = user_ans == q["answer"]
        if correct:
            score += 1
        results.append({
            "q": q["q"],
            "user_answer": user_ans,
            "correct_answer": q["answer"],
            "correct": correct,
            "explanation": q["explanation"],
        })
    pts_earned = score * 10
    STATE["user"]["eco_points"] += pts_earned
    pct = int(score / len(QUIZ_QUESTIONS) * 100)
    if pct >= 80:
        grade = "🏆 Eco Champion!"
    elif pct >= 60:
        grade = "🌿 Eco Warrior!"
    else:
        grade = "🌱 Eco Learner!"
    return jsonify({
        "score": score,
        "total": len(QUIZ_QUESTIONS),
        "pct": pct,
        "grade": grade,
        "pts_earned": pts_earned,
        "eco_points": STATE["user"]["eco_points"],
        "results": results,
    })


@app.route("/api/leaderboard", methods=["GET"])
def get_leaderboard():
    return jsonify(LEADERBOARD)


@app.route("/api/language", methods=["GET"])
def get_language():
    result = []
    for lang in LANGUAGES:
        item = dict(lang)
        item["selected"] = lang["name"] == STATE["language"]
        result.append(item)
    return jsonify({"current": STATE["language"], "languages": result})


@app.route("/api/language", methods=["POST"])
def set_language():
    data = request.get_json()
    lang_name = data.get("language", "English")
    STATE["language"] = lang_name
    return jsonify({"success": True, "language": lang_name})


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🌱 EcoLearn API running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
