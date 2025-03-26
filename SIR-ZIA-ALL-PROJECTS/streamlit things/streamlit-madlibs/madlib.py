import streamlit as st

# Set page config
st.set_page_config(
    page_title="Funny Mad Libs Generator",
    page_icon="😂",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stTextInput input {
        background-color: #f0f2f6;
    }
    .title {
        color: #ff4b4b;
        text-align: center;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown('<h1 class="title">😂 Funny Mad Libs Generator</h1>', unsafe_allow_html=True)
st.write("Fill in the blanks below to create your funny story!")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Input fields
    adjective = st.text_input("Enter a funny adjective", "crazy", help="e.g., silly, hilarious")
    verb1 = st.text_input("Enter a silly action", "dancing", help="e.g., singing, jumping")

with col2:
    verb2 = st.text_input("Enter another funny action", "laughing", help="e.g., sleeping, running")
    celebrity = st.text_input("Your favorite celebrity/cartoon", "SpongeBob", help="e.g., Doraemon, SRK")

# Generate story button
if st.button("Generate My Funny Story!", type="primary"):
    if adjective and verb1 and verb2 and celebrity:
        # Create the story
        funny_story = f"""
        Today was totally {adjective}! I spent the whole day {verb1} and then started {verb2}. 
        My friend said, 'Dude! You've turned into {celebrity}!' 😂
        """
        
        # Display the result in a nice box
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Your Funny Story:")
        st.write(funny_story)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Add a surprise element
        st.balloons()
    else:
        st.warning("Please fill in all the fields!")

# Add some extra features
with st.expander("💡 How to play"):
    st.write("""
    1. Fill in all the fields with funny words
    2. Click the 'Generate' button
    3. Read your hilarious story!
    4. Try different combinations for more fun!
    """)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Try different words for more fun!")
