import streamlit as st
import pandas as pd

# 비밀번호 설정
PASSWORD = "gutabari2025"  # 원하는 비밀번호로 바꾸세요

# 비밀번호 입력창
st.title("🔒 구타바리 작품선정 (보안접속)")
password_input = st.text_input("비밀번호를 입력하세요", type="password")

if password_input != PASSWORD:
    st.warning("접근하려면 올바른 비밀번호를 입력하세요.")
    st.stop()  # 비밀번호가 맞지 않으면 종료

# 비밀번호 통과 시 아래 내용 표시
df = pd.read_excel("구타바리_작품선정.xlsx")

st.title("🎬 구타바리 작품선정 검색기")
query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]
