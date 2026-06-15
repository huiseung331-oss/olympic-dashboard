import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="종목/선수 분석", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("olympic_small.csv")

df = load_data()

st.title("📊 종목 / 선수 분석")

# --- 1. 종목별 선수 신체 데이터 ---
st.subheader("🏃 종목별 선수 신체 데이터")

sport_list = sorted(df['Sport'].unique())
selected_sport = st.selectbox("종목을 선택하세요", sport_list)

df_sport = df[df['Sport'] == selected_sport]

col1, col2 = st.columns(2)
with col1:
    avg_height = df_sport['Height'].mean()
    st.metric("평균 키", f"{avg_height:.1f} cm" if pd.notna(avg_height) else "데이터 없음")
with col2:
    avg_weight = df_sport['Weight'].mean()
    st.metric("평균 몸무게", f"{avg_weight:.1f} kg" if pd.notna(avg_weight) else "데이터 없음")

# 키 분포 히스토그램
fig = px.histogram(df_sport, x='Height', nbins=30,
                   title=f"{selected_sport} 선수들의 키 분포")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- 2. 종목별 인기 변화 ---
st.subheader("📈 종목별 참가 선수 수 변화")

sport_trend = df[df['Sport'] == selected_sport].groupby('Year').size().reset_index(name='선수수')
fig2 = px.line(sport_trend, x='Year', y='선수수', markers=True,
               title=f"{selected_sport} 연도별 참가 선수 수")
st.plotly_chart(fig2, use_container_width=True)
