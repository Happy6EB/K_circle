import os
import pandas as pd
import streamlit as st

st.title("ESG 기업 분석 대시보드")



# ------------------------------------------------
# 경로 세팅
# ------------------------------------------------
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # K_circle 폴더 기준
results_path = os.path.join(base_path, "results.csv")
news_path = os.path.join(base_path, "esg_data", "news_samples.csv")

# ------------------------------------------------
# 데이터 불러오기
# ------------------------------------------------
df_results = pd.read_csv(results_path, encoding="utf-8-sig")      # 결과 데이터
df_news = pd.read_csv(news_path, encoding="utf-8-sig")            # 원본 뉴스 데이터


# 데이터 미리보기 (항상 보이도록)
st.subheader("결과 데이터 미리보기 (results.csv)")
st.dataframe(df_results.head())


# ------------------------------------------------
# 데이터 불러오기
# ------------------------------------------------
df_results = pd.read_csv(results_path, encoding="utf-8-sig")      # 결과 데이터
df_news = pd.read_csv(news_path, encoding="utf-8-sig")            # 원본 뉴스 데이터

# ------------------------------------------------
# 1. results.csv 기반 기업별 ESG 점수
# ------------------------------------------------
st.subheader("기업별 ESG 점수 현황 (results.csv 기반)")

st.bar_chart(df_results.set_index("company")["esg_avg"])
st.line_chart(df_results.set_index("company")["esg_last"])

# ------------------------------------------------
# 2. news_samples.csv 기반 기업별 추세
# ------------------------------------------------
st.subheader("기업별 ESG 관련 뉴스/공시 추이 (news_samples.csv 기반)")

# 기업 선택
choice = st.selectbox("기업 선택", df_news["company"].unique())

# 기업별 날짜별 문서 수
trend = df_news[df_news["company"] == choice].groupby("date")["content"].count()

st.line_chart(trend)

# ------------------------------------------------
st.subheader("원본 뉴스/공시 데이터 미리보기")
st.dataframe(df_news.head())
