import streamlit as st
import pandas as pd

# --- 1) 세션에 인증 상태 저장 ---------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False  # 처음엔 잠금

PASSWORD = "9999"   # 원하는 비밀번호로 수정

# --- 2) 아직 로그인 안 했으면 비밀번호 입력 --------------------
if not st.session_state.authenticated:
    pwd = st.text_input("🔒 비밀번호를 입력하세요", type="password")
    if pwd == PASSWORD:
        st.session_state.authenticated = True   # 통과!
        st.experimental_rerun()                 # 한 번 새로고침
    elif pwd:                                   # 틀린 경우 (빈칸 제외)
        st.warning("❌ 비밀번호가 틀렸습니다.")
    st.stop()                                   # 잠금 상태에선 아래 코드 실행 안 함

# --- 3) 여기부터는 로그인 성공한 사람만 볼 수 있음 -------------
st.title("🎬 구타바리 작품선정 검색기")

# 엑셀 불러오기 (파일은 같은 폴더에 있어야 합니다)
df = pd.read_excel("구타바리_작품선정.xlsx")

query = st.text_input("영화 제목을 입력하세요")

if query:
    result = df[df['영화명'].str.contains(query, case=False, na=False)]
    if not result.empty:
        st.success("✅  검색 결과")
        st.dataframe(result, use_container_width=True)
    else:
        st.markdown("### 자! **드가자~** 😎")
