import streamlit as st
import random
from time import sleep

# Configure page settings
st.set_page_config(
    page_title="🔢 Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>
    .header {
        color: #FF4B4B;
        text-align: center;
        font-size: 2.5rem;
    }
    .result-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    .attempts-left {
        font-weight: bold;
        color: #FF4B4B;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def initialize_game():
    """Initialize or reset game state"""
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = 7
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

def number_guessing_game():
    """Main game function"""
    st.markdown('<div class="header">🔢 Number Guessing Game</div>', unsafe_allow_html=True)
    st.write("### Can you guess the secret number between 1 and 100?")
    
    # Initialize game state
    initialize_game()
    
    # Display game info
    st.write(f"You have **{st.session_state.max_attempts} attempts** to guess the number!")
    
    # Game controls
    col1, col2 = st.columns(2)
    with col1:
        guess = st.number_input("Your guess:", min_value=1, max_value=100, step=1)
    with col2:
        st.write("")  # Spacer
        submit_guess = st.button("Submit Guess")
    
    # Handle guess submission
    if submit_guess and not st.session_state.game_over:
        st.session_state.attempts += 1
        
        # Check the guess
        if guess == st.session_state.secret_number:
            st.session_state.game_over = True
            with st.spinner('Checking...'):
                sleep(1)  # Small delay for suspense
            st.balloons()
            st.markdown(f"""
            <div class="result-box">
                <h3>🎉 Congratulations! 🎉</h3>
                <p>You guessed the correct number <strong>{st.session_state.secret_number}</strong> in {st.session_state.attempts} attempts!</p>
            </div>
            """, unsafe_allow_html=True)
        elif guess < st.session_state.secret_number:
            st.warning("Too low! Try a higher number.")
        else:
            st.warning("Too high! Try a lower number.")
        
        # Check if attempts are exhausted
        if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
            st.session_state.game_over = True
            st.error(f"😢 Game Over! The secret number was {st.session_state.secret_number}")
        
        # Display attempts left
        attempts_left = st.session_state.max_attempts - st.session_state.attempts
        if attempts_left > 0 and not st.session_state.game_over:
            st.markdown(f'<p class="attempts-left">Attempts left: {attempts_left}</p>', unsafe_allow_html=True)
    
    # Reset button
    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.clear()
            st.experimental_rerun()

    # Add game instructions
    with st.expander("ℹ️ How to Play"):
        st.write("""
        1. The computer has selected a random number between 1 and 100
        2. You have 7 attempts to guess the number
        3. After each guess, you'll get feedback if your guess was too high or too low
        4. Try to guess the number in the fewest attempts possible!
        """)

# Run the game
if __name__ == "__main__":
    number_guessing_game()