# import streamlit as st

# st.title("🎈 고양이는 너무 귀여워")
# st.info(
#     "30221 이유나입니다"
# )

# st.write("")
# st.write("")

# # 페이지 구조용 제목 출력
# st.title("지금부터")
# st.header("귀여운 고양이가 등장합니당")



# st.warning("⚠️ 귀여움 주의")
# st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg", )
# st.write("")

# st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGIxeTV0ZW9nMnFxdXppZm1kMXpudjc0aWozYmV1MHl6dHkyZ2dxaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5i7umUqAOYYEw/giphy.gif")


# # st.columns(n): 화면을 n개의 수직 열로 나눕니다
# col1, col2 = st.columns(2)  # 2개의 열 생성

# with col1:
#     st.write("고양이")  # 첫 번째 열에 내용 작성
# with col2:
#     st.write("냥냥냥")  # 두 번째 열에 내용 작성

# # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
# with st.expander("ℹ️ 강아지는?"):
#     st.write("멍멍멍")

# choice = st.text_input("고양이와 강아지 중 더 귀여운 것은?")

# if choice == "고양이":
#     st.success(choice+"는 너무 귀여웡")
# else :
#     st.error("더 귀여운게 있긴해...")
# st.write("---")

# # 여러 옵션 중 하나 선택
# food = st.radio("먹고 싶은 음식을 선택하세요", ["엽떡", "순두부열라면", "뿌링클"])
# st.write("오늘 저녁 메뉴 :"+ food)

# st.write("---")

# import openai

# user_api_key = st.text_input("키를 입력해주세요.")
# if user_api_key: 
#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)
#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

# import streamlit as st
# import openai

# # 🎈 앱 제목과 기본 정보
# st.title("🎈 고양이는 너무 귀여워")
# st.info("30221 이유나입니다")

# st.write("")
# st.write("")

# # 🐱 페이지 소개
# st.title("지금부터")
# st.header("귀여운 고양이가 등장합니당")
# st.warning("⚠️ 귀여움 주의")

# # 🖼️ 고양이 이미지 출력
# st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
# st.write("")
# st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGIxeTV0ZW9nMnFxdXppZm1kMXpudjc0aWozYmV1MHl6dHkyZ2dxaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5i7umUqAOYYEw/giphy.gif")

# # 📦 두 개의 열로 나누기
# col1, col2 = st.columns(2)
# with col1:
#     st.write("고양이")
# with col2:
#     st.write("냥냥냥")

# # ℹ️ 접었다 펼 수 있는 컨테이너
# with st.expander("ℹ️ 강아지는?"):
#     st.write("멍멍멍")

# # 💬 사용자 입력
# choice = st.text_input("고양이와 강아지 중 더 귀여운 것은?")
# if choice == "고양이":
#     st.success(f"{choice}는 너무 귀여웡")
# else:
#     st.error("더 귀여운게 있긴해...")

# st.write("---")

# # 🍽️ 음식 선택
# food = st.radio("먹고 싶은 음식을 선택하세요", ["엽떡", "순두부열라면", "뿌링클"])
# st.write(f"오늘 저녁 메뉴 : {food}")

# st.write("---")

# # 🤖 OpenAI GPT-4o와 대화
# user_api_key = st.secrets["openai"]["api_key"]

# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key=user_api_key)
#     prompt = st.text_input("✍️ 프롬프트를 입력해주세요.")

#     if prompt:
#         completion = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         st.markdown("### 💡 GPT의 답변:")
#         st.wimport streamlit as st

import streamlit as st
import openai

# 🎈 앱 제목과 기본 정보
st.set_page_config(page_title="고양이 귀여움 앱", layout="wide")
st.title("🎈 고양이는 너무 귀여워")
st.info("30221 이유나입니다")

# 🔖 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["🐱 고양이 소개", "🧡 질문 & 입력", "🍽️ 오늘의 메뉴", "🤖 GPT와 대화"])

# 🐱 첫 번째 탭 - 고양이 소개
with tab1:
    st.header("귀여운 고양이가 등장합니당")
    st.warning("⚠️ 귀여움 주의")
    st.image("https://cdn.animaltoc.com/news/photo/202410/1409_6515_3838.jpg")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGIxeTV0ZW9nMnFxdXppZm1kMXpudjc0aWozYmV1MHl6dHkyZ2dxaCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5i7umUqAOYYEw/giphy.gif")

    col1, col2 = st.columns(2)
    with col1:
        st.write("고양이")
    with col2:
        st.write("냥냥냥")

    with st.expander("ℹ️ 강아지는?"):
        st.write("멍멍멍")

# 💬 두 번째 탭 - 질문 & 입력
with tab2:
    st.subheader("누가 더 귀여울까요?")
    choice = st.text_input("고양이와 강아지 중 더 귀여운 것은?")
    if choice == "고양이":
        st.success(f"{choice}는 너무 귀여웡")
    elif choice:
        st.error("더 귀여운게 있긴해...")

# 🍽️ 세 번째 탭 - 음식 선택
with tab3:
    st.subheader("🍽️ 오늘의 메뉴를 골라봐요")
    food = st.radio("먹고 싶은 음식을 선택하세요", ["엽떡", "순두부열라면", "뿌링클"])
    st.write(f"오늘 저녁 메뉴 : {food}")

# 🤖 네 번째 탭 - GPT와 대화
with tab4:
    st.subheader("🤖 GPT-4o와 대화하기")
    user_api_key = st.secrets["openai"]["api_key"]

    if user_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=user_api_key)

        prompt = st.text_input("✍️ 프롬프트를 입력해주세요.")
        if prompt:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
   