import streamlit as st

st.title("Rifle Sign-Out Log")
st.write("Sign-Out whatever rifle you grabbed!")


def clear_input():
  x = rifle
  st.write(x)
  st.session_state.rifle = ""


rifle = st.text_input(
    "What # rifle(s) did you get?", key="rifle", on_change=clear_input
)
