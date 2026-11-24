import streamlit as st

st.set_page_config(
  page_title="Rifle Sign-Out"
)

st.title("Rifle Sign-Out Log")
st.write("Sign-Out whatever rifle you grabbed!")

if "saved_rifle" not in st.session_state:
  st.session_state.saved_rifle = ""


def handle_submit():
  st.session_state.saved_rifle = st.session_state.rifle
  st.session_state.rifle = ""


st.text_input(
    "What # rifle(s) did you get?", key="rifle", on_change=handle_submit
)
rifle = st.session_state.saved_rifle
st.write(rifle)
