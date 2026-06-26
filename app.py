"""Takishun — Modern Portfolio Site (Streamlit).

Run locally with:  streamlit run app.py
"""

from pathlib import Path

import streamlit as st

import content

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{content.PROFILE['name']} · Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------------------------------
# Styling
# --------------------------------------------------------------------------
def load_css() -> None:
    css_path = Path(__file__).parent / "styles" / "style.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


load_css()


def section_title(text: str) -> None:
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)


def spacer(size: str = "md") -> None:
    st.markdown(f'<div class="spacer-{size}"></div>', unsafe_allow_html=True)


# --------------------------------------------------------------------------
# Sidebar navigation
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"## {content.PROFILE['name']}")
    st.caption(content.PROFILE["role"])
    st.divider()
    st.markdown(
        """
        **Navigate**
        - [Home](#home)
        - [About](#about)
        - [Skills](#skills)
        - [Projects](#projects)
        - [Journey](#journey)
        - [Contact](#contact)
        """
    )
    st.divider()
    st.markdown(f"📍 {content.PROFILE['location']}")
    st.markdown(f"✉️ {content.PROFILE['email']}")
    st.link_button("View GitHub", content.PROFILE["github"], use_container_width=True)


# --------------------------------------------------------------------------
# Hero
# --------------------------------------------------------------------------
st.markdown('<a name="home"></a>', unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="hero">
        <span class="hero-eyebrow">{content.PROFILE['handle']}</span>
        <div class="hero-title">Hi, I'm <span class="grad">{content.PROFILE['name']}</span></div>
        <div class="hero-sub">{content.PROFILE['tagline']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

spacer("sm")

# Stats row
stat_cols = st.columns(len(content.STATS))
for col, stat in zip(stat_cols, content.STATS):
    col.markdown(
        f"""
        <div class="stat">
            <div class="stat-num">{stat['num']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

spacer("md")

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
section_title("About")
st.markdown(
    f'<div class="card"><p>{content.ABOUT}</p></div>',
    unsafe_allow_html=True,
)

spacer("md")

# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
section_title("Skills & Toolbox")
spacer("sm")

skill_cols = st.columns(2)
for idx, (group, items) in enumerate(content.SKILLS.items()):
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
section_title("Featured Projects")
spacer("sm")

proj_cols = st.columns(len(content.PROJECTS))
for col, proj in zip(proj_cols, content.PROJECTS):
    tags = "".join(f'<span class="project-tag">{t}</span>' for t in proj["tags"])
    col.markdown(
        f"""
        <div class="card">
            <h3>{proj['title']}</h3>
            <p>{proj['desc']}</p>
            <div style="margin-top:0.7rem;">{tags}</div>
            <a class="card-link" href="{proj['url']}" target="_blank">Open app ↗</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

spacer("md")

# --------------------------------------------------------------------------
# Journey / Timeline
# --------------------------------------------------------------------------
st.markdown('<a name="journey"></a>', unsafe_allow_html=True)
section_title("My Journey")
spacer("sm")

timeline_html = ""
for item in content.TIMELINE:
    timeline_html += f"""
    <div class="timeline-item">
        <div class="timeline-when">{item['when']}</div>
        <div class="timeline-title">{item['title']}</div>
        <div class="timeline-desc">{item['desc']}</div>
    </div>
    """
st.markdown(timeline_html, unsafe_allow_html=True)

spacer("md")

# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
section_title("Get in Touch")
st.markdown(
    '<p style="color:#9aa0ad; max-width:600px;">'
    "Open to collaboration, project ideas and a good conversation about "
    "data, games and security. Reach out through any of these:</p>",
    unsafe_allow_html=True,
)
spacer("sm")

contact_cols = st.columns(len(content.CONTACTS))
for col, c in zip(contact_cols, content.CONTACTS):
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
st.markdown(
    f'<div class="footer-note">Built with ❤️ &amp; Streamlit · © 2026 {content.PROFILE["name"]}</div>',
    unsafe_allow_html=True,
)
