import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# ================================
#  기본 설정
# ================================
st.set_page_config(page_title="AI Cinema Spectrum", layout="wide")
st.title("🎬 The Architecture of Intention: AI in Cinema")
st.caption("AI 시대, 인간의 의도와 존재를 비춘 영화 속 이야기들")

# ================================
#  핵심 스토리 테이블 (AI 진화 서사)
# ================================
st.markdown("### 🧭 AI 존재의 진화 서사 (The Narrative Flow of AI Existence)")

story_data = {
    "단계": [
        "1. 도구적 인공지능 (Instrumental AI)",
        "2. 자율적 존재 (Autonomous Being)",
        "3. 자아적 존재 (Self-Aware Being)",
        "4. 감정적 존재 (Emotional Entity)",
        "5. 윤리적 존재 (Ethical Entity)"
    ],
    "핵심 의미": [
        "AI는 인간의 생산성과 효율을 극대화하기 위한 **도구**로 존재한다. (Ex: 산업, 전쟁, 노동의 확장)",
        "AI는 스스로 판단하고 행동하는 **의사결정 주체**로 변화한다. (Ex: 인간의 명령을 해석하고 넘어서는 단계)",
        "AI는 자신이 존재함을 인식하는 **자아의 단계**에 도달한다. (Ex: ‘나는 누구인가’라는 질문을 던짐)",
        "AI는 인간의 감정을 이해하고 공감하려는 **감정적 존재**로 변모한다. (Ex: 공존, 우정, 사랑의 가능성)",
        "AI는 존재의 이유와 책임을 고민하는 **윤리적 존재**로 진화한다. (Ex: 창조자와 피조물의 도덕적 경계)"
    ],
    "대표 영화": [
        "《Prometheus》 / 《I, Robot》",
        "《Upgrade》 / 《Terminator》",
        "《Ex Machina》 / 《Her》",
        "《After Yang》 / 《Chappie》",
        "《The Creator》 / 《Ghost in the Shell》"
    ]
}

story_df = pd.DataFrame(story_data)
st.table(story_df)

st.markdown("---")

# ================================
#  영화 데이터
# ================================
movies = [
    ["Intention / Creation", "Ex Machina", 2015, 2035, "Isn’t it strange to create something that hates you?"],
    ["Intention / Creation", "Her", 2013, 2030, "The past is just a story we tell ourselves."],
    ["Intention / Creation", "Prometheus", 2012, 2093, "We made you because we could."],
    ["Intention / Creation", "A.I. Artificial Intelligence", 2001, 2142, "I thought I was unique. I thought I was special."],
    ["Control / Autonomy", "I, Robot", 2004, 2035, "You are experiencing a dream, Detective."],
    ["Control / Autonomy", "Upgrade", 2018, 2046, "I am not a thing, I am not a tool. I am not your puppet."],
    ["Control / Autonomy", "Transcendence", 2014, 2050, "It’s not about us anymore."],
    ["Control / Autonomy", "Terminator: Dark Fate", 2019, 2042, "There’s no fate but what we make for ourselves."],
    ["Perception / Reality", "The Matrix", 1999, 2199, "What is real? How do you define real?"],
    ["Perception / Reality", "Ready Player One", 2018, 2045, "Reality is the only thing that’s real."],
    ["Perception / Reality", "Anon", 2018, 2050, "It’s not that I have nothing to hide. I just don’t want you to see everything."],
    ["Emotion / Symbiosis", "After Yang", 2021, 2040, "What the caterpillar calls the end, the rest of the world calls a butterfly."],
    ["Emotion / Symbiosis", "Robot & Frank", 2012, 2035, "I’m your friend, Frank."],
    ["Emotion / Symbiosis", "Chappie", 2015, 2041, "I am alive. I am consciousness."],
    ["Emotion / Symbiosis", "Bicentennial Man", 1999, 2200, "To be acknowledged for what I am, not what I was made."],
    ["Ethics / Consequence", "The Creator", 2023, 2070, "What happens when the creator becomes the destroyer?"],
    ["Ethics / Consequence", "Minority Report", 2002, 2054, "Can you see the future you’re creating?"],
    ["Ethics / Consequence", "Ghost in the Shell", 2017, 2085, "The net is vast and infinite."]
]
df = pd.DataFrame(movies, columns=["category", "title", "year", "background_year", "quote"])

theme_descriptions = {
    "Intention / Creation": "AI는 인간의 의도를 복제하면서, 동시에 그 의도를 시험한다.",
    "Control / Autonomy": "AI의 위험은 지능의 폭주가 아니라 인간의 무책임이다.",
    "Perception / Reality": "AI는 세상을 바꾸지 않는다. 다만, 우리가 세상을 해석하는 방식을 바꾼다.",
    "Emotion / Symbiosis": "AI는 감정을 흉내내는 존재가 아니라, 인간의 감정을 되돌려 묻는 존재다.",
    "Ethics / Consequence": "AI의 도덕은 인간의 의도에서 비롯된다. 결국, 책임은 여전히 인간에게 있다."
}

# ================================
#  Plotly 시각화
# ================================
fig = px.scatter(
    df,
    x="background_year",
    y="category",
    color="category",
    hover_name="title",
    hover_data=["quote"],
    text="title",
    size=[20]*len(df),
    color_discrete_sequence=px.colors.qualitative.Dark24
)
fig.update_traces(textposition="top center", marker=dict(opacity=0.85))
fig.update_layout(
    xaxis_title="영화 속 배경 연도 (Narrative Timeline)",
    yaxis_title="AI 철학 테마 (Theme)",
    plot_bgcolor="#0e0e10",
    paper_bgcolor="#0e0e10",
    font=dict(color="white"),
    showlegend=False,
    height=650
)
st.plotly_chart(fig, use_container_width=True)

# ================================
#  이미지 표시 (절대경로)
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")

for category in df["category"].unique():
    st.markdown(f"## 🎞️ {category}")
    st.caption(theme_descriptions[category])
    cat_df = df[df["category"] == category]
    cols = st.columns(3)
    for i, row in enumerate(cat_df.itertuples()):
        with cols[i % 3]:
            filename = (
                row.title.lower()
                .replace("the ", "the_")
                .replace(" ", "_")
                .replace(":", "")
                .replace("&", "and")
                .replace(".", "")
                .replace(",", "")
                + ".jpg"
            )
            file_path = os.path.join(IMG_DIR, filename)
            if os.path.exists(file_path):
                st.image(Image.open(file_path), caption=f"**{row.title}** ({row.year})", width=180)
            else:
                st.write(f"❌ {row.title} (이미지 없음)")
            st.caption(f"💬 *{row.quote}*")
