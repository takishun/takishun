# 👋 Hi, I'm @takishun

- 👀 I'm interested in **game programming, data science, AI** and more
- 🌱 I'm currently learning **cyber security**
- 📫 Reach me via SNS, e-mail, or message

### 🚀 My Web Apps
- https://uma-expected-val.streamlit.app/
- https://baseballapps.streamlit.app/
- https://reversi-education.streamlit.app/

### 📒 Articles
- note (Data Science): https://note.com/data_science/m/m49e5bdcc3788

---

## 🖥️ Portfolio Site (Streamlit)

A modern, single-page portfolio built with [Streamlit](https://streamlit.io/).

### Features
- 🌐 Bilingual — Japanese / English with a language toggle in the sidebar
- 🎨 Modern dark UI with gradient hero, glassmorphism cards & hover effects
- 📒 note QR code in the hero linking to my articles
- 🧭 Sidebar navigation (Home · About · Skills · Projects · Services · Contact)
- 🧩 Skill toolbox, featured projects and a "what I can help with" section
- ✏️ Content-driven — edit everything in `site_content.py`, no markup needed

### Project structure
```
.
├── app.py              # Main Streamlit app
├── site_content.py     # Bilingual content (EN/JA): profile, skills, projects…
├── requirements.txt    # Python dependencies
├── assets/
│   └── note_qr.png     # QR code linking to my note articles
├── styles/
│   └── style.css       # Custom modern theme
└── .streamlit/
    └── config.toml     # Streamlit theme config
```

### Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open http://localhost:8501.

### Customize
Open `site_content.py` and edit the `CONTENT["en"]` / `CONTENT["ja"]` dictionaries
(profile, skills, projects, services, contacts and UI labels). The layout and
both languages update automatically.

<!---
takishun/takishun is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
