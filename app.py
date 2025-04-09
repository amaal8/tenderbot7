
import streamlit as st

st.set_page_config(page_title="TenderBot", layout="wide")

st.title("🤖 TenderBot")
st.write("مرحبًا بك في TenderBot، الشات بوت الذكي للمناقصات!")

user_input = st.text_input("💬 اكتب استفسارك:")

if user_input:
    st.success(f"✅ رد تجريبي على استفسارك: {user_input}")

# عنصر تفاعلي علشان التطبيق يظل شغال
st.button("إعادة")
