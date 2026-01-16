"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 제목 표시
st.title("🎉 나의 첫 Streamlit 앱")

# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit에 오신 것을 환영합니다.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 김도연")
st.write("직업: 데이터 분석가")
st.write("관심사: 데이터 시각화, 머신러닝")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
    st.success("반갑습니다! 🎊")

# 구분선
st.divider()

import streamlit as st

st.title("밥 먹기 체크")

# 서브헤더 추가
st.subheader("버튼을 눌러보세요!")

status = st.selectbox(
    "지금 상태를 선택하세요",
    ["선택 안 함", "밥을 아직 안 먹었어요", "밥을 너무 많이 먹었어요", "적당히 잘 먹었어요"]
)

# 버튼 만들기
if st.button("확인"):
    if status == "밥을 아직 안 먹었어요":
        st.warning("아직 밥을 안 먹었어요! 빨리 밥을 먹어야 해요.")
    elif status == "밥을 너무 많이 먹었어요":
        st.error("밥을 너무 많이 먹었어요... 조금 줄이는 게 좋겠어요.")
    elif status == "적당히 잘 먹었어요":
        st.success("아주 좋아요! 적당히 잘 먹었습니다.")
    else:
        st.info("상태를 먼저 선택해 주세요.")


# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
