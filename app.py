import streamlit as st
import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel("구타바리_작품선정.xlsx")

st.title("구타바리 작품선정")
query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]

    if not result.empty:
        st.markdown("### ✅ 검색 결과:")

        # 텍스트로 보기 좋게 출력
        for idx, row in result.iterrows():
            st.markdown(f"""
---
🎬 **영화제목**: {row['영화명']}  
📁 **분야**: {row['분야']}  
🎞 **장르**: {row['장르']}  
🛠 **제작년도**: {row['제작연도']} / **제작국가**: {row['제작국가']}  
🌐 **영화명(영문)**: {row['영화명(영문)']}
            """)

    else:
        st.markdown("### 자! **드가자~** 😎")

