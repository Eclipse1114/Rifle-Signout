import streamlit as st

st.title("Rifle Sign-Out Log")
st.write("Sign-Out whatever rifle you grabbed!")

if "rifle" not in st.session_state:
  st.session_state["rifle"] = ""

rifle = st.text_input("What # rifle(s) did you get?", key="rifle")
st.write(rifle)
st.session_state["rifle"] = ""
