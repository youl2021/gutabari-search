import streamlit as st
import pandas as pd

# ── 0) 엑셀 경로 ──────────────────────────────────────────────
DATA_FILE = "구타바리_작품선정.xlsx"      # 같은 폴더에 두었을 때

# ── 1) 비밀번호 설정  ─────────────────────────────────────────
PASSWORD = "9999"                        # 필요하면 변경

# 세션에 로그인 여부 저장
if "auth_ok" not in st.session_state:
    st.session_state["auth_ok"] = False

if not st.session_state["auth_ok"]:
    st.title("🔒 구타바리 작품선정 (보안접속)")
    pwd = st.text_input("비밀번호를 입력하세요", type="password")
    if pwd == PASSWORD:
        st.session_state["auth_ok"] = True
        st.experimental_rerun()
    elif pwd:                             # 뭔가 입력했고 틀렸을 때
        st.warning("❌ 비밀번호가 틀렸습니다.")
    st.stop()                             # 비번 맞을 때까지 아래 코드 실행 안 됨

# ── 2) 검색기 본문  ────────────────────────────────────────────
st.title("🎬 구타바리 작품선정")

# 엑셀 읽기
df = pd.read_excel(DATA_FILE)

query = st.text_input("영화 제목을 입력하세요")

if query:
    # 제목 컬럼에 입력어가 포함된 행 추출
    result = df[df["영화명"].str.contains(query, case=False, na=False)]

    if not result.empty:
        st.markdown("### ✅ 검색 결과:")
        # 검색된 각 행을 “카드” 형태로 출력
        for _, row in result.iterrows():
            st.markdown(
f"""
---
📽 **영화제목** : {row['영화명']}  
📂 **분야** : {row['분야']}  
🎞 **장르** : {row['장르']}  
🗓 **제작연도** : {row['제작연도']} / **제작국가** : {row['제작국가']}  
🌐 **영화명(영문)** : {row['영화명(영문)']}
"""
            )
    else:
        st.markdown("### 자! **드가자~** 😎")
