import streamlit as st

st.title("Rifle Sign-Out Log")
st.write("Sign-Out whatever rifle you grabbed!")

rifle = st.text_input("What # rifle(s) did you get?", key="rifle")
st.write(rifle)
rifle = ""
