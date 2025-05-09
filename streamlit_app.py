import streamlit as st

st.title("🎈 고양이는 너무 귀여워")
st.info(
    "30221 이유나입니다"
)

# 페이지 구조용 제목 출력
st.title("지금부터")
st.header("귀여운 고양이가 등장합니당")



st.warning("⚠️ 귀여움 주의")
st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGIxeTV0ZW9nMnFxdXppZm1kMXpudjc0aWozYmV1MHl6dHkyZ2dxaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5i7umUqAOYYEw/giphy.gif")


# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("고양이")  # 첫 번째 열에 내용 작성
with col2:
    st.write("냥냥냥")  # 두 번째 열에 내용 작성

# st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 강아지는?"):
    st.write("멍멍멍")

choice = st.text_input("고양이와 강아지 중 더 귀여운 것은?")

if choice == "고양이":
    st.success(choice+"는 너무 귀여웡")
else :
    st.error("더 귀여운게 있긴해...")


# 여러 옵션 중 하나 선택
food = st.radio("먹고 싶은 음식을 선택하세요", ["엽떡", "순두부열라면", "뿌링클"])
st.write("오늘 저녁 메뉴 :"+ food)
