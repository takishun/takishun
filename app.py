"""Takishun — Modern Portfolio Site (Streamlit, bilingual EN / JA).

Run locally with:  streamlit run app.py
"""

import base64
from pathlib import Path

import streamlit as st

import site_content as content

BASE_DIR = Path(__file__).parent

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Takishun · Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------
def load_css() -> None:
    css_path = BASE_DIR / "styles" / "style.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def section_title(text: str) -> None:
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)


def spacer(size: str = "md") -> None:
    st.markdown(f'<div class="spacer-{size}"></div>', unsafe_allow_html=True)


load_css()

# --------------------------------------------------------------------------
# Language selection (persisted in session state)
# --------------------------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = content.DEFAULT_LANG

C = content.CONTENT[st.session_state.lang]
ui = C["ui"]
profile = C["profile"]


# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------
with st.sidebar:
    # Language toggle
    lang_keys = list(content.LANGUAGES.keys())
    st.radio(
        ui["lang_label"],
        options=lang_keys,
        index=lang_keys.index(st.session_state.lang),
        format_func=lambda k: content.LANGUAGES[k],
        horizontal=True,
        key="lang",
    )
    # Re-read content in case the language just changed
    C = content.CONTENT[st.session_state.lang]
    ui = C["ui"]
    profile = C["profile"]

    st.divider()
    st.markdown(f"## {profile['name']}")
    st.caption(profile["role"])
    st.divider()
    nav = ui["nav"]
    st.markdown(
        f"""
        **{ui['navigate']}**
        - [{nav['home']}](#home)
        - [{nav['about']}](#about)
        - [{nav['skills']}](#skills)
        - [{nav['projects']}](#projects)
        - [{nav['services']}](#services)
        - [{nav['contact']}](#contact)
        """
    )
    st.divider()
    st.markdown(f"📍 {profile['location']}")
    st.markdown(f"✉️ {profile['email']}")
    st.link_button(ui["view_github"], profile["github"], use_container_width=True)


# --------------------------------------------------------------------------
# Hero  (with note QR card)
# --------------------------------------------------------------------------
st.markdown('<a name="home"></a>', unsafe_allow_html=True)

hero_col, qr_col = st.columns([2.3, 1], gap="large")

with hero_col:
    st.markdown(
        f"""
        <div class="hero">
            <span class="hero-eyebrow">{profile['handle']}</span>
            <div class="hero-title">Hi, I'm <span class="grad">{profile['name']}</span></div>
            <div class="hero-sub">{profile['tagline']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with qr_col:
    qr_path = BASE_DIR / content.NOTE_QR_IMAGE
    if qr_path.exists():
        qr_b64 = img_to_base64(qr_path)
        st.markdown(
            f"""
            <a class="qr-card" href="{content.NOTE_URL}" target="_blank">
                <img src="data:image/png;base64,{qr_b64}" alt="note QR" />
                <span class="qr-caption">{ui['note_caption']}</span>
            </a>
            """,
            unsafe_allow_html=True,
        )

spacer("md")

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
section_title(ui["about_title"])
st.markdown(f'<div class="card"><p>{C["about"]}</p></div>', unsafe_allow_html=True)

spacer("md")

# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
section_title(ui["skills_title"])
spacer("sm")

skill_cols = st.columns(2)
for idx, (group, items) in enumerate(C["skills"].items()):
    pills = "".join(f'<span class="pill">{item}</span>' for item in items)
    skill_cols[idx % 2].markdown(
        f"""
        <div class="card" style="margin-bottom: 1rem;">
            <h3>{group}</h3>
            <div>{pills}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

spacer("md")

# --------------------------------------------------------------------------
# Projects
# --------------------------------------------------------------------------
st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
section_title(ui["projects_title"])
spacer("sm")

proj_cols = st.columns(len(C["projects"]))
for col, proj in zip(proj_cols, C["projects"]):
    tags = "".join(f'<span class="project-tag">{t}</span>' for t in proj["tags"])
    col.markdown(
        f"""
        <div class="card">
            <h3>{proj['title']}</h3>
            <p>{proj['desc']}</p>
            <div style="margin-top:0.7rem;">{tags}</div>
            <a class="card-link" href="{proj['url']}" target="_blank">{ui['open_app']}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

spacer("md")

# --------------------------------------------------------------------------
# Services / What I Can Help With
# --------------------------------------------------------------------------
st.markdown('<a name="services"></a>', unsafe_allow_html=True)
section_title(ui["services_title"])
spacer("sm")

service_cols = st.columns(2)
for idx, svc in enumerate(C["services"]):
    service_cols[idx % 2].markdown(
        f"""
        <div class="card" style="margin-bottom: 1rem;">
            <h3>{svc['icon']} {svc['title']}</h3>
            <p>{svc['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

spacer("md")

# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
section_title(ui["contact_title"])
st.markdown(
    f'<p style="color:#9aa0ad; max-width:600px;">{ui["contact_intro"]}</p>',
    unsafe_allow_html=True,
)
spacer("sm")

contact_cols = st.columns(len(C["contacts"]))
for col, c in zip(contact_cols, C["contacts"]):
    col.markdown(
        f"""
        <a class="contact-btn" href="{c['url']}" target="_blank">
            <span style="font-size:1.2rem;">{c['icon']}</span>
            <span>{c['label']}</span>
        </a>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------------------------------
# Footer
# --------------------------------------------------------------------------
st.markdown(f'<div class="footer-note">{ui["footer"]}</div>', unsafe_allow_html=True)
