import streamlit as st

st.title("Rifle Sign-Out Log")
st.write("Sign-Out whatever rifle you grabbed!")

rifle = st.text_input("What # rifle did you get?")
st.write(rifle)
