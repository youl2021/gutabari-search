import streamlit as st
import pandas as pd

# ── 1) 비밀번호 설정 ──────────────────────────
PASSWORD = "9999"                       # 원할 때 바꿔 주세요

if "auth" not in st.session_state:      # 세션에 로그인 여부 저장
    st.session_state["auth"] = False

if not st.session_state["auth"]:
    st.title("🔒 구타바리 작품선정 (보안접속)")
    pwd = st.text_input("비밀번호를 입력하세요", type="password")
    if pwd == PASSWORD:
        st.session_state["auth"] = True
        st.experimental_rerun()         # ↩ 검색기 화면으로 전환
    elif pwd:                           # 뭔가 입력했고 틀렸을 때
        st.warning("접근하려면 올바른 비밀번호를 입력하세요.")
    st.stop()                           # 여기서 코드 종료

# ── 2) 검색기 본문 ─────────────────────────────
st.title("🎬 구타바리 작품선정 검색기")

df = pd.read_excel("구타바리_작품선정.xlsx")      # 엑셀은 같은 폴더

query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]

    if not result.empty:
        st.markdown("### ✅ 검색 결과:")
        for _, row in result.iterrows():          # 텍스트 형태로 깔끔 출력
            st.markdown(
f"""
---
🎬 **영화제목**  : {row['영화명']}  
📁 **분야**     : {row['분야']}  
🎞 **장르**     : {row['장르']}  
🛠 **제작년도** : {row['제작연도']}   /   **제작국가** : {row['제작국가']}  
🌐 **영화명(영문)** : {row['영화명(영문)']}
"""
            )
    else:
        st.markdown("### 자! **드가자~** 😎")
