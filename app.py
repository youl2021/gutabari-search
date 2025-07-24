import streamlit as st
import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel("구타바리_작품선정.xlsx")

st.title("구타바리 작품선정")
query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]

    if not result.empty:
        st.write("✅ 검색 결과:")
        st.dataframe(result)
    else:
        st.markdown("### 자! **드가자~** 😎")

