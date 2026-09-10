import streamlit as st

st.title("Points to Ringgit Calculator")

st.write("45 points = 40 coins")
st.write("100 coins = RM1.00")

points = st.number_input(
    "Enter points:",
    min_value=0,
    step=1
)

coins = points / 1.125
ringgit = coins / 100

st.success(f"RM{ringgit:.2f}")
