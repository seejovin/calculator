import streamlit as st

st.title("Lazada Points to Ringgit")

import streamlit as st

points = st.number_input("Enter points:")

coins = points / 1.125
coins_ringgit = coins / 100

st.write(f"Your points are worth RM{coins_ringgit:.2f}")
