import streamlit as st
import pandas as pd

# 페이지 기본 설정
st.set_page_config(page_title="올림픽 120년 역사", page_icon="🏅", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("olympic_small.csv")
    return df

df = load_data()

# 제목
st.title("🏅 올림픽 120년 역사 대시보드")
st.markdown("### 1896년 아테네 ~ 2016년 리우 올림픽 데이터 분석")

# 프로젝트 소개
st.markdown("""
이 프로젝트는 **근대 올림픽 120년의 역사**를 데이터로 분석합니다.
- 📍 데이터 출처: sports-reference.com (Kaggle)
- 📅 기간: 1896년 ~ 2016년 (하계 올림픽)
- 👥 전 세계 선수들의 정보와 메달 결과를 담고 있습니다.
""")

st.divider()

# 전체 통계 요약
st.subheader("📊 전체 통계 요약")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("전체 선수 수", f"{df['Name'].nunique():,}명")
with col2:
    st.metric("참가 국가 수", f"{df['NOC'].nunique()}개국")
with col3:
    st.metric("종목 수", f"{df['Sport'].nunique()}개")
with col4:
    st.metric("개최 연도 수", f"{df['Year'].nunique()}회")

st.divider()

# 데이터 미리보기
st.subheader("🔍 데이터 미리보기")
st.dataframe(df.head(20))

# 안내
st.info("👈 왼쪽 사이드바에서 다른 페이지로 이동해보세요!")
