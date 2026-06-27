"""Central content/config for the portfolio site (bilingual: EN / JA).

Edit the values here to update the site — no need to touch app.py.
All UI text and content lives under CONTENT[lang].
"""

# Shared links
GITHUB_URL = "https://github.com/takishun"
EMAIL = "shun.takinami.cr@gmail.com"
STREAMLIT_PROFILE = "https://share.streamlit.io/user/takishun"
NOTE_URL = "https://note.com/data_science/m/m49e5bdcc3788"
NOTE_QR_IMAGE = "assets/note_qr.png"

# Live apps (URLs shared across languages)
APP_UMA = "https://uma-expected-val.streamlit.app/"
APP_BASEBALL = "https://baseballapps.streamlit.app/"
APP_REVERSI = "https://reversi-education.streamlit.app/"

# Languages available for the toggle: value -> display label
LANGUAGES = {
    "ja": "🇯🇵 日本語",
    "en": "🇬🇧 English",
}
DEFAULT_LANG = "ja"


CONTENT = {
    # ===================================================================
    # English
    # ===================================================================
    "en": {
        "ui": {
            "navigate": "Navigate",
            "nav": {
                "home": "Home",
                "about": "About",
                "skills": "Skills",
                "projects": "Projects",
                "services": "Services",
                "contact": "Contact",
            },
            "view_github": "View GitHub",
            "lang_label": "Language",
            "about_title": "About",
            "skills_title": "Skills & Toolbox",
            "projects_title": "Featured Projects",
            "services_title": "What I Can Help With",
            "contact_title": "Get in Touch",
            "contact_intro": (
                "Open to collaboration, project ideas and a good conversation "
                "about data, games and security. Reach out through any of these:"
            ),
            "open_app": "Open app ↗",
            "note_caption": "📒 Read my articles on note",
            "footer": "Built with ❤️ &amp; Streamlit · © 2026 Takishun",
        },
        "profile": {
            "name": "Takishun",
            "handle": "@takishun",
            "role": "Developer · Data Science & AI Enthusiast",
            "tagline": (
                "I build interactive web apps and explore the space where "
                "game programming, data science and AI meet."
            ),
            "location": "Japan",
            "email": EMAIL,
            "github": GITHUB_URL,
        },
        "about": (
            "Hi, I'm Takishun 👋 — a developer who enjoys turning ideas into "
            "interactive tools people can actually use. My interests span game "
            "programming, data science and AI, and I'm currently diving deep into "
            "cyber security. I love shipping small, focused web apps that make a "
            "concept tangible — from horse-racing expected value calculators to "
            "educational games."
        ),
        "skills": {
            "Languages": ["Python", "JavaScript", "SQL", "C / C++"],
            "Data & AI": ["pandas", "NumPy", "scikit-learn", "Machine Learning", "Data Viz"],
            "Web & Apps": ["Streamlit", "HTML / CSS", "REST APIs", "Git"],
            "Interests": ["Game Programming", "Cyber Security", "Reinforcement Learning"],
        },
        "projects": [
            {
                "title": "Uma Expected Value",
                "desc": (
                    "A horse-racing analytics tool that computes expected value "
                    "to support smarter betting decisions."
                ),
                "tags": ["Streamlit", "Data Science", "Analytics"],
                "url": APP_UMA,
            },
            {
                "title": "Baseball Apps",
                "desc": (
                    "A collection of baseball data utilities and visualizations "
                    "for exploring stats and game insights."
                ),
                "tags": ["Streamlit", "Sports Data", "Visualization"],
                "url": APP_BASEBALL,
            },
            {
                "title": "Reversi Education",
                "desc": (
                    "An interactive Reversi (Othello) app designed to teach "
                    "strategy and game logic in an approachable way."
                ),
                "tags": ["Streamlit", "Game", "Education"],
                "url": APP_REVERSI,
            },
        ],
        "services": [
            {
                "icon": "📊",
                "title": "Data Analysis & Visualization",
                "desc": (
                    "Turning raw data into clear, actionable insights with pandas, "
                    "scikit-learn and intuitive visualizations to support better decisions."
                ),
            },
            {
                "icon": "🛠️",
                "title": "Interactive Web Apps",
                "desc": (
                    "Designing and shipping focused Streamlit apps that make a concept "
                    "tangible and usable — quickly, from idea to live deployment."
                ),
            },
            {
                "icon": "🎮",
                "title": "Game & Educational Content",
                "desc": (
                    "Building game logic and interactive learning experiences that make "
                    "complex ideas approachable and fun to explore."
                ),
            },
            {
                "icon": "🔐",
                "title": "Security-aware Development",
                "desc": (
                    "Applying security fundamentals and a defensive mindset to build "
                    "tools that are mindful of safety and robustness."
                ),
            },
        ],
        "contacts": [
            {"icon": "✉️", "label": "Email", "url": f"mailto:{EMAIL}"},
            {"icon": "💻", "label": "GitHub", "url": GITHUB_URL},
            {"icon": "📒", "label": "note", "url": NOTE_URL},
            {"icon": "🚀", "label": "Streamlit Apps", "url": STREAMLIT_PROFILE},
        ],
    },

    # ===================================================================
    # 日本語
    # ===================================================================
    "ja": {
        "ui": {
            "navigate": "ナビゲーション",
            "nav": {
                "home": "ホーム",
                "about": "自己紹介",
                "skills": "スキル",
                "projects": "プロジェクト",
                "services": "できること",
                "contact": "お問い合わせ",
            },
            "view_github": "GitHub を見る",
            "lang_label": "言語",
            "about_title": "自己紹介",
            "skills_title": "スキル & ツール",
            "projects_title": "主なプロジェクト",
            "services_title": "提供できること",
            "contact_title": "お問い合わせ",
            "contact_intro": (
                "コラボレーションやプロジェクトのご相談、データ・ゲーム・セキュリティ"
                "についての雑談、いつでも歓迎です。以下からお気軽にどうぞ："
            ),
            "open_app": "アプリを開く ↗",
            "note_caption": "📒 note で記事を読む",
            "footer": "Built with ❤️ &amp; Streamlit · © 2026 Takishun",
        },
        "profile": {
            "name": "Takishun",
            "handle": "@takishun",
            "role": "開発者 · データサイエンス & AI 愛好家",
            "tagline": (
                "インタラクティブな Web アプリを作りながら、ゲームプログラミング・"
                "データサイエンス・AI が交わる領域を探求しています。"
            ),
            "location": "日本",
            "email": EMAIL,
            "github": GITHUB_URL,
        },
        "about": (
            "こんにちは、Takishun です 👋 — アイデアを「実際に使えるツール」に"
            "変えることが好きな開発者です。興味の対象はゲームプログラミング・"
            "データサイエンス・AI と幅広く、現在はサイバーセキュリティを深く学んでいます。"
            "競馬の期待値計算ツールから教育用ゲームまで、コンセプトを形にする"
            "小さくて焦点の定まった Web アプリを作って届けるのが得意です。"
        ),
        "skills": {
            "言語": ["Python", "JavaScript", "SQL", "C / C++"],
            "データ & AI": ["pandas", "NumPy", "scikit-learn", "機械学習", "データ可視化"],
            "Web & アプリ": ["Streamlit", "HTML / CSS", "REST API", "Git"],
            "興味分野": ["ゲームプログラミング", "サイバーセキュリティ", "強化学習"],
        },
        "projects": [
            {
                "title": "Uma Expected Value",
                "desc": (
                    "より賢い意思決定を支援するため、期待値を計算する"
                    "競馬分析ツールです。"
                ),
                "tags": ["Streamlit", "データサイエンス", "分析"],
                "url": APP_UMA,
            },
            {
                "title": "Baseball Apps",
                "desc": (
                    "野球データのユーティリティと可視化をまとめたアプリ集。"
                    "成績や試合のインサイトを探れます。"
                ),
                "tags": ["Streamlit", "スポーツデータ", "可視化"],
                "url": APP_BASEBALL,
            },
            {
                "title": "Reversi Education",
                "desc": (
                    "リバーシ（オセロ）の戦略とゲームロジックを、"
                    "わかりやすく学べるインタラクティブなアプリです。"
                ),
                "tags": ["Streamlit", "ゲーム", "教育"],
                "url": APP_REVERSI,
            },
        ],
        "services": [
            {
                "icon": "📊",
                "title": "データ分析・可視化",
                "desc": (
                    "生のデータを pandas や scikit-learn、わかりやすい可視化で"
                    "「意思決定に使えるインサイト」へと変換します。"
                ),
            },
            {
                "icon": "🛠️",
                "title": "インタラクティブな Web アプリ開発",
                "desc": (
                    "コンセプトを素早く形にする、焦点の定まった Streamlit アプリを"
                    "アイデアから公開まで一貫して設計・実装します。"
                ),
            },
            {
                "icon": "🎮",
                "title": "ゲーム・教育コンテンツ",
                "desc": (
                    "ゲームロジックやインタラクティブな学習体験を通じて、"
                    "難しい概念を親しみやすく・楽しく学べる形にします。"
                ),
            },
            {
                "icon": "🔐",
                "title": "セキュリティを意識した開発",
                "desc": (
                    "セキュリティの基礎と防御的な視点を取り入れ、"
                    "安全性と堅牢性に配慮したツールづくりを心がけています。"
                ),
            },
        ],
        "contacts": [
            {"icon": "✉️", "label": "メール", "url": f"mailto:{EMAIL}"},
            {"icon": "💻", "label": "GitHub", "url": GITHUB_URL},
            {"icon": "📒", "label": "note", "url": NOTE_URL},
            {"icon": "🚀", "label": "Streamlit アプリ", "url": STREAMLIT_PROFILE},
        ],
    },
}
