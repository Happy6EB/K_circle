import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 데이터 로드 (테스트용 더미 데이터)
# -------------------------------
# 실제로는 results.csv, news_samples.csv와 연동 가능
df = pd.DataFrame({
    "company": ["Samsung", "SK Hynix", "LG Chem", "Hyundai", "Kakao"],
    "industry": ["IT", "IT", "Chem", "Auto", "Platform"],
    "esg_score": [92, 61, 88, 77, 70],
    "financial": [85, 65, 75, 80, 68],
    "growth": [88, 70, 83, 76, 72],
    "year": [2020, 2020, 2020, 2020, 2020]
})

# -------------------------------
# 레이아웃
# -------------------------------
st.title("📊 ESG 기업 분석 대시보드 (PRO 버전)")

# 1. Filters + Top5 ESG Companies
st.sidebar.header("Filters")
industry = st.sidebar.selectbox("Industry", df["industry"].unique())
top5 = df.nlargest(5, "esg_score")[["company", "esg_score"]]
st.subheader("Top 5 ESG Companies")
st.bar_chart(top5.set_index("company"))

# 2. Company Details
company = st.selectbox("Select Company", df["company"].unique())
st.subheader(f"Company Details: {company}")
st.metric("Market Cap", "342.6B")
st.metric("Debt to Equity", "0.93")

trend = df[df["company"] == company].groupby("year")["esg_score"].mean()
st.line_chart(trend)

# 3. Comparison (Radar Chart)
st.subheader("Comparison between companies")
categories = ["Financial", "ESG", "Growth"]
df_radar = pd.DataFrame({
    "Category": categories,
    "Company A": [80, 75, 90],
    "Company B": [60, 85, 70]
})

fig = px.line_polar(df_radar, r="Company A", theta="Category", line_close=True)
st.plotly_chart(fig)

# 4. Recommendations
st.subheader("Recommendations")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Samsung", 92, "ESG Score")

with col2:
    st.metric("SK Hynix", 61, "ESG Score")

with col3:
    st.metric("LG Chem", 88, "ESG Score")


#================================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 파일 경로
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
results_path = os.path.join(base_path, "results.csv")

# CSV 불러오기
df = pd.read_csv(results_path, encoding="utf-8-sig")

st.title("📊 ESG + 주가 분석 대시보드")

# 회사 선택
company = st.selectbox("기업 선택", df["company"].unique())

# ESG 점수 차트
st.subheader(f"{company} ESG 점수 추세")
esg_trend = df[df["company"] == company].groupby("year")["esg_last"].mean()
st.line_chart(esg_trend)

# 주가 차트
st.subheader(f"{company} 주가 추이")
stock_trend = df[df["company"] == company].groupby("year")["stock_price"].mean()
st.line_chart(stock_trend)
