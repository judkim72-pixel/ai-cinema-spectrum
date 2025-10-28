import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Cinema Spectrum", layout="wide")

st.title("🎬 The Architecture of Intention: AI in Cinema")
st.caption("AI 시대, 인간의 의도와 존재를 비춘 영화 속 이야기들")

# ================================
#  영화 데이터 세트
# ================================
movies = [
    {"category": "Intention / Creation", "title": "Ex Machina", "year": 2015, "background_year": 2035,
     "quote": "Isn’t it strange to create something that hates you?",
     "poster": "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Ex_Machina_(film)"},
    {"category": "Intention / Creation", "title": "Her", "year": 2013, "background_year": 2030,
     "quote": "The past is just a story we tell ourselves.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Her_(film)"},
    {"category": "Intention / Creation", "title": "Prometheus", "year": 2012, "background_year": 2093,
     "quote": "We made you because we could.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Prometheus_(2012_film)"},
    {"category": "Intention / Creation", "title": "A.I. Artificial Intelligence", "year": 2001, "background_year": 2142,
     "quote": "I thought I was unique. I thought I was special.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/A.I._Artificial_Intelligence"},

    {"category": "Control / Autonomy", "title": "I, Robot", "year": 2004, "background_year": 2035,
     "quote": "You are experiencing a dream, Detective.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/7/7e/Movie_poster_i_robot.jpg",
     "wiki": "https://en.wikipedia.org/wiki/I,_Robot_(film)"},
    {"category": "Control / Autonomy", "title": "Upgrade", "year": 2018, "background_year": 2046,
     "quote": "I am not a thing, I am not a tool. I am not your puppet.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/8/8b/Upgrade_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Upgrade_(film)"},
    {"category": "Control / Autonomy", "title": "Transcendence", "year": 2014, "background_year": 2050,
     "quote": "It’s not about us anymore.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/e/e3/Transcendence2014Poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Transcendence_(2014_film)"},
    {"category": "Control / Autonomy", "title": "Terminator: Dark Fate", "year": 2019, "background_year": 2042,
     "quote": "There’s no fate but what we make for ourselves.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/4/4e/Terminator_Dark_Fate_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Terminator:_Dark_Fate"},

    {"category": "Perception / Reality", "title": "The Matrix", "year": 1999, "background_year": 2199,
     "quote": "What is real? How do you define real?",
     "poster": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/The_Matrix"},
    {"category": "Perception / Reality", "title": "Ready Player One", "year": 2018, "background_year": 2045,
     "quote": "Reality is the only thing that’s real.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/4/42/Ready_Player_One_%282018%29.png",
     "wiki": "https://en.wikipedia.org/wiki/Ready_Player_One_(film)"},
    {"category": "Perception / Reality", "title": "Anon", "year": 2018, "background_year": 2050,
     "quote": "It’s not that I have nothing to hide. I just don’t want you to see everything.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/f/fd/Anon_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Anon_(film)"},

    {"category": "Emotion / Symbiosis", "title": "After Yang", "year": 2021, "background_year": 2040,
     "quote": "What the caterpillar calls the end, the rest of the world calls a butterfly.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/2/2a/After_Yang_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/After_Yang"},
    {"category": "Emotion / Symbiosis", "title": "Robot & Frank", "year": 2012, "background_year": 2035,
     "quote": "I’m your friend, Frank.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/a/ae/Robot_and_Frank.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Robot_%26_Frank"},
    {"category": "Emotion / Symbiosis", "title": "Chappie", "year": 2015, "background_year": 2041,
     "quote": "I am alive. I am consciousness.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Chappie_(film)"},
    {"category": "Emotion / Symbiosis", "title": "Bicentennial Man", "year": 1999, "background_year": 2200,
     "quote": "To be acknowledged for what I am, not what I was made.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/8/8e/Bicentennial_man_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Bicentennial_Man"},

    {"category": "Ethics / Consequence", "title": "The Creator", "year": 2023, "background_year": 2070,
     "quote": "What happens when the creator becomes the destroyer?",
     "poster": "https://upload.wikimedia.org/wikipedia/en/6/6c/The_Creator_2023_poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/The_Creator_(2023_film)"},
    {"category": "Ethics / Consequence", "title": "Minority Report", "year": 2002, "background_year": 2054,
     "quote": "Can you see the future you’re creating?",
     "poster": "https://upload.wikimedia.org/wikipedia/en/5/5d/Minority_Report_Poster.jpg",
     "wiki": "https://en.wikipedia.org/wiki/Minority_Report_(film)"},
    {"category": "Ethics / Consequence", "title": "Ghost in the Shell", "year": 2017, "background_year": 2085,
     "quote": "The net is vast and infinite.",
     "poster": "https://upload.wikimedia.org/wikipedia/en/4/4e/Ghost_in_the_Shell_%282017_film%29.png",
     "wiki": "https://en.wikipedia.org/wiki/Ghost_in_the_Shell_(2017_film)"},
]

df = pd.DataFrame(movies)

theme_descriptions = {
    "Intention / Creation": "인간이 AI를 만든 이유는 단순한 효율이 아니라 ‘의도를 구현하기 위함’이었다. 창조자는 피조물을 통해 자신을 비춘다.",
    "Control / Autonomy": "AI는 처음으로 스스로 판단하는 도구가 되었다. 통제의 경계가 흐려질수록 책임의 주체도 모호해진다.",
    "Perception / Reality": "AI는 세상을 바꾸지 않는다. 다만, 우리가 세상을 해석하는 방식을 바꾼다.",
    "Emotion / Symbiosis": "AI는 인간의 감정을 흉내내는 존재가 아니라, 인간의 감정을 되돌려 묻는 존재다.",
    "Ethics / Consequence": "AI의 도덕은 인간의 의도에서 비롯된다. 결국, 책임은 여전히 인간에게 있다."
}

# ================================
#  Plotly Timeline Visualization
# ================================
fig = px.scatter(
    df,
    x="background_year",
    y="category",
    color="category",
    hover_name="title",
    hover_data=["year", "quote"],
    text="title",
    size=[22]*len(df),
    color_discrete_sequence=px.colors.qualitative.Dark24
)

fig.update_traces(textposition="top center", marker=dict(opacity=0.85, line=dict(width=1, color="white")))
fig.update_layout(
    xaxis_title="영화 속 배경 연도 (Narrative Timeline)",
    yaxis_title="AI 철학 테마 (Theme)",
    plot_bgcolor="#0e0e10",
    paper_bgcolor="#0e0e10",
    font=dict(color="white"),
    showlegend=False,
    height=720
)
st.plotly_chart(fig, use_container_width=True)

# ================================
#  카테고리별 포스터 갤러리
# ================================
for category in df["category"].unique():
    st.markdown(f"## 🎞️ {category}")
    st.caption(theme_descriptions[category])
    cat_df = df[df["category"] == category]
    cols = st.columns(3)
    for i, row in enumerate(cat_df.itertuples()):
        with cols[i % 3]:
            st.image(row.poster, caption=f"**{row.title}** ({row.year})", width=200)
            st.caption(f"💬 *{row.quote}*")
            st.markdown(f"[🔗 Wikipedia Link]({row.wiki})")
