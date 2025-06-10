# save this as app.py
import streamlit as st
import random

st.title("🎮 Number Guessing Game")

# Session state to store the random number and attempts
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("Guess a number between 1 and 100")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.info("🔽 Too low!")
    elif guess > st.session_state.number:
        st.info("🔼 Too high!")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
