/**
 * EcoLearn — Shared Frontend Logic
 * All pages include this file. Each page calls initPage() after DOM ready.
 */

const API = "http://127.0.0.1:5000/api";

/* ─── API Helper ──────────────────────────────────────────────────────────── */
async function api(path, method = "GET", body = null) {
    const opts = { method, headers: { "Content-Type": "application/json" } };
    if (body) opts.body = JSON.stringify(body);
    const res = await fetch(API + path, opts);
    return res.json();
}

/* ─── Toast Notification ─────────────────────────────────────────────────── */
function showToast(msg) {
    let t = document.getElementById("toast");
    if (!t) {
        t = document.createElement("div");
        t.id = "toast";
        t.className = "toast";
        document.body.appendChild(t);
    }
    t.innerHTML = msg;
    t.classList.add("show");
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove("show"), 3200);
}

/* ─── Progress Bar Helper ─────────────────────────────────────────────────── */
function pbar(pct, label = "") {
    return `<div class="pbar-wrap"><div class="pbar-fill" style="width:${pct}%"></div></div>
          <div class="pbar-caption">${label}</div>`;
}

/* ─── Shared Navbar ───────────────────────────────────────────────────────── */
async function renderNav(activePage) {
    const user = await api("/user");
    const pages = [
        { id: "index", label: "🏠 Home", href: "index.html" },
        { id: "learning", label: "📘 Learning", href: "learning.html" },
        { id: "habits", label: "🌿 Habits", href: "habits.html" },
        { id: "teams", label: "👥 Teams", href: "teams.html" },
        { id: "challenges", label: "🏆 Challenges", href: "challenges.html" },
        { id: "games", label: "🎮 Games", href: "games.html" },
        { id: "leaderboard", label: "📊 Leaderboard", href: "leaderboard.html" },
        { id: "language", label: "🌐 Language", href: "language.html" },
    ];
    const tabs = pages.map(p =>
        `<a href="${p.href}" class="nav-tab${activePage === p.id ? " active" : ""}">${p.label}</a>`
    ).join("");

    document.getElementById("nav-placeholder").innerHTML = `
<nav class="top-nav">
  <div class="nav-logo">🌱 Eco<span>Learn</span></div>
  <div class="nav-center">${tabs}</div>
  <div class="nav-right">
    <span class="nav-stats">🌱 <strong id="nav-pts">${user.eco_points}</strong> pts &nbsp;|&nbsp; 🔥 <strong>${user.streak}</strong>-day streak</span>
    <a href="dashboard.html"><button class="nav-btn">👤 Dashboard</button></a>
  </div>
</nav>`;
    return user;
}

/* ─── Update Points in Nav ────────────────────────────────────────────────── */
function updateNavPts(pts) {
    const el = document.getElementById("nav-pts");
    if (el) el.textContent = pts;
}

/* ─── Tab System ─────────────────────────────────────────────────────────── */
function initTabs() {
    document.querySelectorAll(".tab-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const target = btn.dataset.tab;
            document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
            btn.classList.add("active");
            document.getElementById(target).classList.add("active");
        });
    });
}

/* ─── Footer ─────────────────────────────────────────────────────────────── */
function renderFooter(msg = "Empowering the next generation of eco-warriors") {
    return `<div class="footer">🌱 <strong>EcoLearn</strong> &nbsp;|&nbsp; ${msg} &nbsp;|&nbsp; Made with 💚 for Planet Earth</div>`;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: index.html — Home Hub
═══════════════════════════════════════════════════════════════════════════ */
async function initHome() {
    await renderNav("index");

    // Learning paths
    const paths = await api("/learning-paths");
    const lpGrid = document.getElementById("lp-grid");
    if (lpGrid) {
        lpGrid.innerHTML = paths.map(p => `
      <div>
        <div class="lp-card">
          <div class="lp-icon">${p.icon}</div>
          <div class="lp-title">${p.title}</div>
          <div class="lp-meta">${p.desc}</div>
          <div>
            <span class="badge">🎥 ${p.videos} Videos</span>
            <span class="badge">📘 ${p.lessons} Lessons</span>
          </div>
        </div>
        ${pbar(p.progress, `✅ ${p.progress}% completed`)}
        <a href="learning.html?path=${p.key}">
          <button class="btn full" style="margin-top:4px;">▶️ Continue Learning</button>
        </a>
      </div>
    `).join("");
    }

    // Challenges (preview)
    const challenges = await api("/challenges");
    const chGrid = document.getElementById("ch-grid");
    if (chGrid) {
        chGrid.innerHTML = challenges.map(c => `
      <div class="ch-card">
        <div class="ch-icon">${c.icon}</div>
        <div class="ch-title">${c.title}</div>
        <div class="ch-desc">${c.desc}</div>
        <div>
          <span class="ch-badge">👥 ${c.participants.toLocaleString()} joined</span>
          <span class="ch-badge">🌱 +${c.points} pts</span>
          <span class="ch-badge">📅 Ends ${c.deadline}</span>
        </div>
        <div style="margin-top:12px;">
          <a href="challenges.html"><button class="btn full sm">✅ Join Now</button></a>
        </div>
      </div>
    `).join("");
    }

    document.getElementById("footer").innerHTML = renderFooter();
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: challenges.html
═══════════════════════════════════════════════════════════════════════════ */
async function initChallenges() {
    await renderNav("challenges");
    const challenges = await api("/challenges");
    const container = document.getElementById("challenges-list");

    function renderAll() {
        container.innerHTML = challenges.map(c => `
      <div class="ch-card" id="ch-${c.key}">
        <div class="ch-icon">${c.icon}</div>
        <div class="ch-title">${c.title}</div>
        <div class="ch-desc">${c.desc}</div>
        <div>
          <span class="ch-badge">👥 ${c.participants.toLocaleString()} participants</span>
          <span class="ch-badge">🌱 +${c.points} Eco Points</span>
          <span class="ch-badge">📅 Ends ${c.deadline}</span>
          <span class="ch-badge">🎯 ${c.difficulty}</span>
          <span class="ch-badge">⏱️ ${c.duration}</span>
        </div>
        <div style="margin-top:12px;">
          <button class="steps-toggle" onclick="toggleSteps('${c.key}')">📋 How to complete: ${c.title}</button>
          <div class="steps-list" id="steps-${c.key}">
            ${c.steps.map((s, i) => `<div class="step-card"><strong>Step ${i + 1}:</strong> ${s}</div>`).join("")}
          </div>
          ${c.joined
                ? `<div style="color:var(--green2);font-weight:700;padding:8px 0;">✅ You've joined <strong>${c.title}</strong>! Check your dashboard for progress.</div>`
                : `<button class="btn full" id="join-${c.key}" onclick="joinChallenge('${c.key}', ${c.points})">✅ Join: ${c.title}</button>`
            }
        </div>
      </div>
      <hr class="eco">
    `).join("");
    }

    renderAll();

    window.toggleSteps = (key) => {
        const el = document.getElementById(`steps-${key}`);
        el.classList.toggle("open");
    };

    window.joinChallenge = async (key, pts) => {
        const res = await api(`/challenges/${key}/join`, "POST");
        const ch = challenges.find(c => c.key === key);
        ch.joined = true;
        renderAll();
        updateNavPts(res.eco_points);
        showToast(`🎉 Joined ${ch.title}! Complete it to earn +${pts} eco points!`);
    };

    document.getElementById("footer").innerHTML = renderFooter("Every challenge is a step towards a greener planet.");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: habits.html
═══════════════════════════════════════════════════════════════════════════ */
async function initHabits() {
    await renderNav("habits");

    // Today's date
    const now = new Date();
    document.getElementById("today-date").textContent =
        now.toLocaleDateString("en-GB", { weekday: "long", day: "2-digit", month: "long", year: "numeric" });

    let habits = await api("/habits");

    function renderHabits() {
        const list = document.getElementById("habits-list");
        list.innerHTML = habits.map(h => `
      <div class="habit-row${h.completed ? " done" : ""}" id="habit-${h.key}">
        <div class="habit-icon">${h.icon}</div>
        <div class="habit-info">
          <div class="habit-title">${h.title} ${h.completed ? "✅" : ""}</div>
          <div class="habit-desc">${h.desc}</div>
        </div>
        <span class="pts-badge">+${h.pts} pts</span>
        ${!h.completed
                ? `<button class="btn sm" onclick="completeHabit('${h.key}')">✅ Done!</button>`
                : `<span style="color:var(--green2);font-weight:700;font-size:0.82rem;">Completed!</span>`}
      </div>
    `).join("");

        const done = habits.filter(h => h.completed).length;
        const earned = habits.filter(h => h.completed).reduce((s, h) => s + h.pts, 0);
        const total = habits.length;
        const pct = Math.round(done / total * 100);

        document.getElementById("stat-done").textContent = done;
        document.getElementById("stat-pts").textContent = earned;
        document.getElementById("stat-pct").textContent = pct + "%";
        document.getElementById("habit-pbar").style.width = pct + "%";

        const msg = document.getElementById("habit-msg");
        if (done === total) {
            msg.innerHTML = `<div style="color:var(--green2);font-weight:700;padding:12px;background:var(--bg2);border-radius:10px;border:1px solid var(--green2);">🎉 <strong>Perfect Day!</strong> You've completed ALL today's eco habits! You earned a +20 Bonus streak point!</div>`;
        } else if (done >= Math.floor(total / 2)) {
            msg.innerHTML = `<div style="color:var(--blue5);padding:12px;background:var(--blue1);border-radius:10px;border:1px solid var(--blue3);">🌿 Great job! You're past halfway — keep going! ${total - done} habits left.</div>`;
        } else if (done > 0) {
            msg.innerHTML = `<div style="color:#f4a261;padding:12px;background:#2a1f00;border-radius:10px;border:1px solid #e36414;">🌱 Good start! ${total - done} more habits to complete today.</div>`;
        } else {
            msg.innerHTML = "";
        }
    }

    renderHabits();

    window.completeHabit = async (key) => {
        const res = await api(`/habits/${key}/complete`, "POST");
        habits = habits.map(h => h.key === key ? { ...h, completed: true } : h);
        renderHabits();
        updateNavPts(res.eco_points);
        showToast("✅ Habit completed! Eco points awarded 🌱");
    };

    document.getElementById("footer").innerHTML = renderFooter("Small daily habits create a big impact. Keep going! 💚");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: teams.html
═══════════════════════════════════════════════════════════════════════════ */
async function initTeams() {
    await renderNav("teams");
    let teams = await api("/teams");

    function renderTeams() {
        const myTeams = teams.filter(t => t.joined);
        const mySection = document.getElementById("my-teams");
        if (myTeams.length > 0) {
            mySection.innerHTML = `
        <div class="my-team-section">
          <div style="font-size:1.05rem;font-weight:700;color:var(--green5);margin-bottom:8px;">🏅 My Team(s)</div>
          <div style="color:var(--green4);">You are a member of: <strong style="color:var(--green6);">${myTeams.map(t => t.name).join(", ")}</strong></div>
          <div style="margin-top:8px;font-size:0.83rem;color:var(--green3);">🌱 Team activities and missions are tracked on your dashboard.</div>
        </div>`;
        } else {
            mySection.innerHTML = "";
        }

        const list = document.getElementById("teams-list");
        list.innerHTML = teams.map(t => `
      <div class="team-card">
        <div class="team-icon">${t.icon}</div>
        <div class="team-title">${t.name}</div>
        <div class="team-desc">${t.desc}</div>
        <div>
          <span class="team-badge">👥 ${t.members} Members</span>
          <span class="team-badge">🌱 ${t.points.toLocaleString()} Team Points</span>
          <span class="team-badge">🎯 ${t.missions} Missions Done</span>
          <span class="team-badge">🏆 ${t.rank}</span>
          <span class="team-badge">🔎 Focus: ${t.focus}</span>
        </div>
        <div style="margin-top:12px;">
          ${t.joined
                ? `<div style="color:var(--green2);font-weight:700;padding:8px 0;">✅ You are a member of <strong>${t.name}</strong>!</div>`
                : `<button class="btn full" onclick="joinTeam('${t.key}')">👥 Join ${t.name}</button>`}
        </div>
      </div>
      <hr class="eco">
    `).join("");
    }

    renderTeams();

    window.joinTeam = async (key) => {
        const res = await api(`/teams/${key}/join`, "POST");
        teams = teams.map(t => t.key === key ? { ...t, joined: true } : t);
        renderTeams();
        showToast(`🎉 Welcome to ${res.team_name}! 🌿`);
    };

    document.getElementById("footer").innerHTML = renderFooter("Stronger together for a greener world.");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: games.html — Eco Trivia Quiz
═══════════════════════════════════════════════════════════════════════════ */
async function initGames() {
    await renderNav("games");
    const questions = await api("/games/questions");
    let answers = {};

    function renderQuiz() {
        document.getElementById("quiz-section").style.display = "block";
        document.getElementById("results-section").style.display = "none";
        answers = {};
        document.getElementById("quiz-list").innerHTML = questions.map((q, i) => `
      <div class="quiz-card">
        <div class="quiz-q">Q${i + 1}. ${q.q}</div>
        <div class="quiz-options" id="opts-${i}">
          ${q.options.map(opt => `
            <label class="quiz-option" id="opt-${i}-${opt.replace(/\s/g, '_')}">
              <input type="radio" name="q${i}" value="${opt}" onchange="selectOpt(${i}, '${opt.replace(/'/g, "\\'")}', this)">
              ${opt}
            </label>
          `).join("")}
        </div>
      </div>
    `).join("");
    }

    window.selectOpt = (qi, val, input) => {
        answers[qi] = val;
        document.querySelectorAll(`#opts-${qi} .quiz-option`).forEach(el => el.classList.remove("selected"));
        input.closest(".quiz-option").classList.add("selected");
    };

    window.submitQuiz = async () => {
        if (Object.keys(answers).length < questions.length) {
            showToast("⚠️ Please answer all questions before submitting!");
            return;
        }
        const payload = {};
        for (const [k, v] of Object.entries(answers)) payload[String(k)] = v;
        const res = await api("/games/submit", "POST", { answers: payload });
        updateNavPts(res.eco_points);
        showResults(res);
    };

    function showResults(res) {
        document.getElementById("quiz-section").style.display = "none";
        const rs = document.getElementById("results-section");
        rs.style.display = "block";
        rs.style.scrollMarginTop = "100px";
        rs.scrollIntoView({ behavior: "smooth" });

        document.getElementById("score-box").innerHTML = `
      <div class="score-box">
        <div class="grade">${res.grade}</div>
        <div class="score" style="color:var(--green2);">${res.score} / ${res.total}</div>
        <div class="info">You scored ${res.pct}% — Earned <strong style="color:var(--green5);">+${res.pts_earned} Eco Points!</strong></div>
      </div>`;

        document.getElementById("review-list").innerHTML = res.results.map((r, i) => `
      <div class="result-card ${r.correct ? "correct" : "wrong"}">
        <div style="font-weight:700;color:var(--green6);margin-bottom:6px;">${r.correct ? "✅" : "❌"} Q${i + 1}. ${r.q}</div>
        <div style="font-size:0.87rem;margin-bottom:4px;">Your answer: <strong style="color:${r.correct ? "var(--green2)" : "#e63946"};">${r.user_answer || "Not answered"}</strong></div>
        ${!r.correct ? `<div style="font-size:0.87rem;color:var(--green4);margin-bottom:4px;">Correct answer: <strong>${r.correct_answer}</strong></div>` : ""}
        <div style="font-size:0.82rem;color:var(--green3);margin-top:6px;">💡 ${r.explanation}</div>
      </div>
    `).join("");
    }

    window.retakeQuiz = renderQuiz;

    renderQuiz();
    document.getElementById("footer").innerHTML = renderFooter("Learn while you play! 🎮");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: leaderboard.html
═══════════════════════════════════════════════════════════════════════════ */
async function initLeaderboard() {
    await renderNav("leaderboard");
    const lb = await api("/leaderboard");
    const top3 = lb.slice(0, 3);

    // Podium: 2nd, 1st, 3rd
    const podiumOrder = [
        { player: top3[1], size: "1.7rem", color: "#C0C0C0", bg: "linear-gradient(135deg,#2a2a2a,#3a3a3a)", border: "#C0C0C0", medal: "🥈" },
        { player: top3[0], size: "2rem", color: "#FFD700", bg: "linear-gradient(135deg,#3a3000,#4d4000)", border: "#FFD700", medal: "🥇" },
        { player: top3[2], size: "1.5rem", color: "#CD7F32", bg: "linear-gradient(135deg,#2a1500,#3a2000)", border: "#CD7F32", medal: "🥉" },
    ];

    document.getElementById("podium").innerHTML = podiumOrder.map(p => `
    <div class="podium-card" style="background:${p.bg};border-color:${p.border};">
      <div class="medal">${p.medal}</div>
      <div class="name" style="font-size:${p.size};color:${p.color};">${p.player.name}</div>
      <div class="school">${p.player.school}</div>
      <div style="font-size:0.85rem;color:${p.color};margin:4px 0;">${p.player.badge}</div>
      <div class="pts" style="color:${p.color};">🌱 ${p.player.pts} pts</div>
    </div>
  `).join("");

    document.getElementById("lb-list").innerHTML = lb.map(p => `
    <div class="lb-row${p.is_me ? " me" : ""}" style="border-color:${p.is_me ? "var(--green2)" : p.color};">
      <div class="lb-rank" style="color:${p.color};">${p.rank}</div>
      <img class="lb-avatar" src="https://api.dicebear.com/7.x/adventurer/svg?seed=${p.name.replace(/ /g, "")}&backgroundColor=2d6a4f" style="border:2px solid ${p.color};" />
      <div style="flex:1;">
        <div class="lb-name">${p.name}${p.is_me ? `<span class="you-badge">YOU</span>` : ""}</div>
        <div class="lb-school">🏫 ${p.school} &nbsp;|&nbsp; ${p.badge}</div>
      </div>
      <div class="lb-pts" style="color:${p.color};">🌱 ${p.pts}</div>
    </div>
  `).join("");

    document.getElementById("footer").innerHTML = renderFooter("Rise through the ranks, save the planet! 🌍");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: learning.html
═══════════════════════════════════════════════════════════════════════════ */
async function initLearning() {
    await renderNav("learning");

    const paths = await api("/learning-paths");
    const sel = document.getElementById("path-select");
    sel.innerHTML = paths.map(p => `<option value="${p.key}">${p.icon} ${p.title}</option>`).join("");

    // Check URL param
    const urlParams = new URLSearchParams(window.location.search);
    const preselect = urlParams.get("path");
    if (preselect) sel.value = preselect;

    async function loadPath(key) {
        const path = await api(`/learning-paths/${key}`);

        // Header
        const basePath = paths.find(p => p.key === key);
        document.getElementById("path-header").innerHTML = `
      <div class="path-header">
        <div style="font-size:1.8rem;font-weight:800;color:var(--green6);margin-bottom:6px;">${path.label}</div>
        <div style="color:var(--green4);margin-bottom:16px;">${path.desc}</div>
        <div>
          <span style="background:rgba(0,0,0,0.2);border:1px solid var(--green2);border-radius:8px;padding:4px 12px;font-size:0.83rem;color:var(--green5);margin-right:8px;">🎥 ${path.videos.length} Videos</span>
          <span style="background:rgba(0,0,0,0.2);border:1px solid var(--green2);border-radius:8px;padding:4px 12px;font-size:0.83rem;color:var(--green5);margin-right:8px;">📘 ${path.lessons.length} Lessons</span>
          <span style="background:rgba(0,0,0,0.2);border:1px solid var(--green2);border-radius:8px;padding:4px 12px;font-size:0.83rem;color:var(--green5);">✅ ${path.progress}% Complete</span>
        </div>
      </div>
      ${pbar(path.progress, `Overall Progress: ${path.progress}%`)}
    `;

        // Next video
        const nextVid = path.videos.find(v => !v.watched) || path.videos[0];
        const vidId = extractYTId(nextVid.url);
        document.getElementById("video-player").innerHTML = `
      <div style="font-weight:700;color:var(--green5);margin-bottom:8px;">▶️ Now Playing: ${nextVid.title}</div>
      <div style="position:relative;padding-bottom:56.25%;height:0;border-radius:12px;overflow:hidden;">
        <iframe src="https://www.youtube.com/embed/${vidId}" frameborder="0" allowfullscreen
          style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;"></iframe>
      </div>
    `;

        // All videos
        document.getElementById("all-videos").innerHTML = path.videos.map(v => `
      <div class="video-card">
        <span style="color:${v.watched ? "var(--green2)" : "var(--green5)"};font-weight:700;">${v.watched ? "✅" : "▶️"} ${v.title}</span>
        <span style="color:${v.watched ? "var(--green2)" : "var(--blue5)"};font-size:0.8rem;">${v.watched ? "Watched" : "Up next"}</span>
      </div>
    `).join("");

        // Lessons
        document.getElementById("lessons-list").innerHTML = path.lessons.map((l, i) => `
      <div class="lesson-card ${l.done ? "done" : "todo"}">
        <span>${l.done ? "✅" : "📄"} &nbsp;${i + 1}. ${l.title}</span>
        <span style="font-size:0.78rem;color:${l.done ? "var(--green2)" : "#555"};">${l.done ? "Done" : ""}</span>
      </div>
    `).join("");

        // Continue button
        const next = path.lessons.find(l => !l.done);
        const contBtn = document.getElementById("continue-btn");
        if (next) {
            contBtn.innerHTML = `<button class="btn" onclick="showToast('Opening: ${next.title}...')">▶️ Continue: ${next.title}</button>`;
        } else {
            contBtn.innerHTML = `<div style="color:var(--green2);font-weight:700;">🎉 You've completed all lessons in this path!</div>`;
        }
    }

    sel.addEventListener("change", () => loadPath(sel.value));
    loadPath(sel.value);

    document.getElementById("footer").innerHTML = renderFooter("Learn. Act. Inspire.");
}

function extractYTId(url) {
    const m = url.match(/[?&]v=([^&]+)/);
    return m ? m[1] : url.split("/").pop();
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: language.html
═══════════════════════════════════════════════════════════════════════════ */
async function initLanguage() {
    await renderNav("language");
    let langData = await api("/language");

    function renderLanguages() {
        const grid = document.getElementById("lang-grid");
        const langs = langData.languages;
        grid.innerHTML = langs.map(l => `
      <div class="lang-card${l.selected ? " active" : ""}" id="lc-${l.name}">
        <div class="lang-flag">${l.flag}</div>
        <div class="lang-name">${l.selected ? "✅ " : ""}${l.name}</div>
        <div class="lang-native">${l.native}</div>
        <div class="lang-sup">${l.support}</div>
        ${!l.selected ? `<button class="btn sm full" style="margin-top:10px;" onclick="selectLang('${l.name}')">Select</button>` : ""}
      </div>
    `).join("");

        document.getElementById("current-lang").textContent = langData.current;
    }

    window.selectLang = async (name) => {
        await api("/language", "POST", { language: name });
        langData = await api("/language");
        renderLanguages();
        showToast(`🌐 Language set to ${name}!`);
    };

    renderLanguages();
    document.getElementById("footer").innerHTML = renderFooter("Learning eco concepts in your language. 🌍");
}

/* ═══════════════════════════════════════════════════════════════════════════
   PAGE: dashboard.html
═══════════════════════════════════════════════════════════════════════════ */
async function initDashboard() {
    await renderNav("dashboard");
    const user = await api("/user");
    const paths = await api("/learning-paths");

    // Profile card
    document.getElementById("profile-card").innerHTML = `
    <div class="profile-card">
      <img class="profile-avatar" src="https://api.dicebear.com/7.x/adventurer/svg?seed=EcoKid&backgroundColor=2d6a4f" />
      <div>
        <div class="profile-name">${user.name}</div>
        <div class="profile-school">🏫 ${user.school}</div>
        <div>
          <span class="stat-pill">🌱 ${user.eco_points} Eco Points</span>
          <span class="stat-pill">🔥 ${user.streak}-Day Streak</span>
          <span class="stat-pill">🏅 Level ${user.level} — ${user.level_title}</span>
          <span class="stat-pill">📅 Member since ${user.member_since}</span>
        </div>
        <div style="margin-top:10px;font-size:0.85rem;color:var(--green3);">
          🎯 ${user.next_level_pts} more points to reach <strong style="color:var(--green5);">Level ${user.level + 1} — Eco Champion</strong>
        </div>
      </div>
    </div>
  `;

    // Overview stats
    const stats = [
        { icon: "🌱", label: "Eco Points", val: user.eco_points },
        { icon: "🔥", label: "Day Streak", val: user.streak },
        { icon: "📘", label: "Lessons Done", val: 34 },
        { icon: "🏆", label: "Challenges", val: 6 },
    ];
    document.getElementById("overview-stats").innerHTML = stats.map(s => `
    <div class="achievement-card">
      <div style="font-size:2rem;">${s.icon}</div>
      <div class="big">${s.val}</div>
      <div class="label">${s.label}</div>
    </div>
  `).join("");

    // Recent activity
    const activities = [
        { icon: "🎥", desc: "Watched: Climate Change — Greenhouse Effect", time: "2 hours ago", pts: "+5 pts" },
        { icon: "✅", desc: "Completed: Waste Segregation Week Challenge", time: "Yesterday", pts: "+40 pts" },
        { icon: "🔥", desc: "Maintained 7-day learning streak!", time: "Yesterday", pts: "+15 pts" },
        { icon: "📘", desc: "Finished: Biodiversity Lesson 3", time: "2 days ago", pts: "+8 pts" },
        { icon: "👥", desc: "Joined Team: Green Guardians", time: "3 days ago", pts: "+10 pts" },
    ];
    document.getElementById("recent-activity").innerHTML = activities.map(a => `
    <div class="activity-row">
      <div><span style="margin-right:8px;">${a.icon}</span><span class="desc">${a.desc}</span></div>
      <div><span class="time">${a.time}</span>&nbsp;&nbsp;<span class="pts">${a.pts}</span></div>
    </div>
  `).join("");

    // Streaks tab
    const streakBoxes = [
        { icon: "🔥", val: 7, label: "Current Streak", color: "#f4a261", bg: "linear-gradient(135deg,#3d1e00,#6b3300)", border: "#e36414" },
        { icon: "⚡", val: 21, label: "Longest Streak", color: "#90c7f4", bg: "linear-gradient(135deg,#1a2744,#1e3a5f)", border: "#457b9d" },
        { icon: "📅", val: 42, label: "Total Active Days", color: "#95d5b2", bg: "linear-gradient(135deg,#1b3320,#2d5a3d)", border: "#52b788" },
    ];
    document.getElementById("streak-boxes").innerHTML = streakBoxes.map(s => `
    <div class="streak-box" style="background:${s.bg};border:1px solid ${s.border};">
      <div style="font-size:3rem;">${s.icon}</div>
      <div class="big" style="color:${s.color};">${s.val}</div>
      <div class="label" style="color:${s.color};">${s.label}</div>
    </div>
  `).join("");

    const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    const done = [true, true, true, true, true, true, true];
    document.getElementById("week-grid").innerHTML = days.map((d, i) => `
    <div class="day-cell" style="background:${done[i] ? "var(--green2)" : "var(--bg2)"};">
      <div class="day-icon">${done[i] ? "🔥" : "⬜"}</div>
      <div class="day-name" style="color:${done[i] ? "var(--green6)" : "#888"};">${d}</div>
    </div>
  `).join("");

    // Progress tab
    document.getElementById("progress-list").innerHTML = paths.map(p => {
        const doneL = Math.round(p.lessons * p.progress / 100);
        return `
      <div style="padding:14px 18px;background:var(--bg2);border-radius:12px;border:1px solid var(--bg4);margin-bottom:10px;">
        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
          <span style="font-weight:700;color:var(--green6);">${p.icon} ${p.title}</span>
          <span style="color:var(--green2);font-weight:700;">${p.progress}%</span>
        </div>
        <div style="color:var(--green3);font-size:0.8rem;margin-bottom:8px;">${doneL} / ${p.lessons} lessons completed</div>
        ${pbar(p.progress, "")}
      </div>`;
    }).join("");

    // Achievements tab
    const badges = [
        { icon: "🌱", name: "First Step", desc: "Completed your first lesson", earned: true },
        { icon: "🔥", name: "7-Day Warrior", desc: "Maintained a 7-day streak", earned: true },
        { icon: "♻️", name: "Recycler Pro", desc: "Completed Waste Management path", earned: true },
        { icon: "🌍", name: "Climate Aware", desc: "Finished Climate Change module", earned: true },
        { icon: "👥", name: "Team Player", desc: "Joined an eco team", earned: true },
        { icon: "🏆", name: "Challenge Champ", desc: "Won 3 challenges", earned: false },
        { icon: "💧", name: "Water Guardian", desc: "Completed Water Conservation", earned: false },
        { icon: "🌳", name: "Tree Hugger", desc: "Planted 5 trees", earned: false },
    ];
    document.getElementById("badges-grid").innerHTML = badges.map(b => `
    <div class="badge-card ${b.earned ? "earned" : "locked"}">
      <div class="b-icon">${b.icon}</div>
      <div class="b-name">${b.name}</div>
      <div class="b-desc">${b.desc}</div>
      <div class="b-status" style="color:${b.earned ? "var(--green2)" : "#555"};">${b.earned ? "✅ Earned" : "🔒 Locked"}</div>
    </div>
  `).join("");

    // Impact tab
    const impacts = [
        { icon: "🌳", val: "5", label: "Trees Planted" },
        { icon: "♻️", val: "20 kg", label: "Waste Recycled" },
        { icon: "💧", val: "200 L", label: "Water Saved" },
        { icon: "🚲", val: "18 km", label: "Car Trips Replaced" },
    ];
    document.getElementById("impact-stats").innerHTML = impacts.map(i => `
    <div class="achievement-card" style="padding:24px;">
      <div style="font-size:2.2rem;">${i.icon}</div>
      <div class="big">${i.val}</div>
      <div class="label">${i.label}</div>
    </div>
  `).join("");

    // Goals tab
    const goals = [
        { title: "🌱 Reach 300 Eco Points", curr: user.eco_points, target: 300 },
        { title: "📘 Complete Climate Change Path", curr: 60, target: 100 },
        { title: "🔥 Achieve 21-Day Streak", curr: user.streak, target: 21 },
        { title: "🏆 Win 5 Challenges", curr: 3, target: 5 },
        { title: "🌳 Plant 10 Trees", curr: 5, target: 10 },
    ];
    document.getElementById("goals-list").innerHTML = goals.map(g => {
        const pct = Math.round(Math.min(g.curr / g.target * 100, 100));
        return `
      <div class="goal-card">
        <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
          <span style="font-weight:700;color:var(--blue6);">${g.title}</span>
          <span style="color:var(--green2);font-weight:700;">${g.curr} / ${g.target}</span>
        </div>
      </div>
      ${pbar(pct, `${pct}% complete`)}`;
    }).join("");

    initTabs();
    document.getElementById("footer").innerHTML = renderFooter("Your personal eco journey dashboard");
}
