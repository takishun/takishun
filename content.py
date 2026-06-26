"""Central content/config for the portfolio site.

Edit the values here to update the site — no need to touch app.py.
"""

PROFILE = {
    "name": "Takishun",
    "handle": "@takishun",
    "role": "Developer · Data Science & AI Enthusiast",
    "tagline": (
        "I build interactive web apps and explore the space where "
        "game programming, data science and AI meet."
    ),
    "location": "Japan",
    "email": "shun.takinami.cr@gmail.com",
    "github": "https://github.com/takishun",
}

# Hero call-to-action stats
STATS = [
    {"num": "3+", "label": "Live Streamlit Apps"},
    {"num": "4", "label": "Focus Domains"},
    {"num": "∞", "label": "Curiosity"},
]

ABOUT = (
    "Hi, I'm Takishun 👋 — a developer who enjoys turning ideas into "
    "interactive tools people can actually use. My interests span game "
    "programming, data science and AI, and I'm currently diving deep into "
    "cyber security. I love shipping small, focused web apps that make a "
    "concept tangible — from horse-racing expected value calculators to "
    "educational games."
)

# Skill groups
SKILLS = {
    "Languages": ["Python", "JavaScript", "SQL", "C / C++"],
    "Data & AI": ["pandas", "NumPy", "scikit-learn", "Machine Learning", "Data Viz"],
    "Web & Apps": ["Streamlit", "HTML / CSS", "REST APIs", "Git"],
    "Interests": ["Game Programming", "Cyber Security", "Reinforcement Learning"],
}

# Featured projects
PROJECTS = [
    {
        "title": "Uma Expected Value",
        "desc": (
            "A horse-racing analytics tool that computes expected value to "
            "support smarter betting decisions."
        ),
        "tags": ["Streamlit", "Data Science", "Analytics"],
        "url": "https://uma-expected-val.streamlit.app/",
    },
    {
        "title": "Baseball Apps",
        "desc": (
            "A collection of baseball data utilities and visualizations for "
            "exploring stats and game insights."
        ),
        "tags": ["Streamlit", "Sports Data", "Visualization"],
        "url": "https://baseballapps.streamlit.app/",
    },
    {
        "title": "Reversi Education",
        "desc": (
            "An interactive Reversi (Othello) app designed to teach strategy "
            "and game logic in an approachable way."
        ),
        "tags": ["Streamlit", "Game", "Education"],
        "url": "https://reversi-education.streamlit.app/",
    },
]

# Journey / timeline
TIMELINE = [
    {
        "when": "Now",
        "title": "Learning Cyber Security",
        "desc": "Studying security fundamentals, CTF-style challenges and defensive techniques.",
    },
    {
        "when": "Ongoing",
        "title": "Building & Shipping Web Apps",
        "desc": "Developing and deploying interactive Streamlit apps across data, sports and games.",
    },
    {
        "when": "Foundation",
        "title": "Data Science & AI",
        "desc": "Hands-on work with Python data tooling, machine learning and applied analytics.",
    },
    {
        "when": "Origins",
        "title": "Game Programming",
        "desc": "Where the passion started — building game logic and interactive experiences.",
    },
]

CONTACTS = [
    {"icon": "✉️", "label": "Email", "url": "mailto:shun.takinami.cr@gmail.com"},
    {"icon": "💻", "label": "GitHub", "url": "https://github.com/takishun"},
    {"icon": "🚀", "label": "Streamlit Apps", "url": "https://share.streamlit.io/user/takishun"},
]
