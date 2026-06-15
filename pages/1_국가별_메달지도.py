import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="국가별 메달 지도", page_icon="🗺️", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("olympic_small.csv")

df = load_data()

st.title("🗺️ 국가별 메달 지도")
st.markdown("나라별로 획득한 메달 수를 세계지도에 표현했어요.")

# 연도 선택 슬라이더
years = sorted(df['Year'].unique())
selected_year = st.select_slider("연도를 선택하세요", options=years, value=years[-1])

# 선택한 연도의 메달 딴 기록만 필터링
df_year = df[(df['Year'] == selected_year) & (df['Medal'].notna())]

# 국가(NOC)별 메달 수 세기
medal_count = df_year.groupby('NOC').size().reset_index(name='메달수')

# 지도 그리기
fig = px.choropleth(
    medal_count,
    locations='NOC',              # 국가 코드(3글자)
    locationmode='ISO-3',          # ISO 3자리 코드 모드
    color='메달수',
    color_continuous_scale='YlOrRd',
    title=f"{selected_year}년 올림픽 국가별 메달 수"
)
st.plotly_chart(fig, use_container_width=True)

# 표로도 보여주기 (상위 10개국)
st.subheader(f"🏆 {selected_year}년 메달 상위 국가")
top10 = medal_count.sort_values('메달수', ascending=False).head(10)
st.dataframe(top10, use_container_width=True)
