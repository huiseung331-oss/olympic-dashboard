import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="시대별 변화", page_icon="📈", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("olympic_small.csv")

df = load_data()

st.title("📈 올림픽의 시대별 변화")

# --- 1. 연도별 참가국 수 변화 ---
st.subheader("🌍 연도별 참가 국가 수")
country_trend = df.groupby('Year')['NOC'].nunique().reset_index(name='참가국수')
fig1 = px.line(country_trend, x='Year', y='참가국수', markers=True,
               title="연도별 참가 국가 수 변화")
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# --- 2. 여성 참가 비율 변화 ---
st.subheader("👩 여성 참가 비율 변화")

# 연도별, 성별 선수 수 계산
sex_trend = df.groupby(['Year', 'Sex']).size().reset_index(name='선수수')
# 연도별 전체 선수 수
total_per_year = df.groupby('Year').size().reset_index(name='전체')
# 여성만 추출
female = sex_trend[sex_trend['Sex'] == 'F'].merge(total_per_year, on='Year')
female['여성비율'] = female['선수수'] / female['전체'] * 100

fig2 = px.line(female, x='Year', y='여성비율', markers=True,
               title="연도별 여성 참가 비율 (%)")
st.plotly_chart(fig2, use_container_width=True)

st.info("초기 올림픽에는 여성 참가가 거의 없었지만, 점점 늘어난 것을 볼 수 있어요!")
