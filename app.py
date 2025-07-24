import streamlit as st
import pandas as pd

PASSWORD = "9999"
st.title("🔒 구타바리 작품선정 (보안접속)")
pwd = st.text_input("비밀번호를 입력하세요", type="password")
if pwd != PASSWORD:
    st.warning("❌ 접근하려면 올바른 비밀번호를 입력하세요.")
    st.stop()

df = pd.read_excel("구타바리_작품선정.xlsx")
st.title("🎬 구타바리 작품선정 검색기")
query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]
    if not result.empty:
        for _, row in result.iterrows():
            st.markdown(f"""
🎬 **영화제목**: {row['영화명']}  
📽️ <span style="color:red; font-weight:bold;">영화사</span>: {row['영화사'☠️]}  
📁 **분야**: {row['분야']}  
🎞 **장르**: {row['장르']}  
🗓 **제작년도**: {row['제작연도']}  
🌍 **제작국가**: {row['제작국가']}  
🌐 **영화명(영문)**: {row['영화명(영문)']}
""", unsafe_allow_html=True)
    else:
        st.markdown("### 자! **드가자~** 😎")
