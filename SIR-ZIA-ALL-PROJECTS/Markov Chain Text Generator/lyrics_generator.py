import streamlit as st
import random
from collections import defaultdict

def train_markov_chain(text, chain_length=2):
    """Train Markov chain model from the input text."""
    words = text.split()
    markov_chain = defaultdict(list)
    
    for i in range(len(words) - chain_length):
        current_state = ' '.join(words[i:i+chain_length])
        next_word = words[i+chain_length]
        markov_chain[current_state].append(next_word)
    
    return markov_chain

def generate_lyrics(markov_chain, length=50, chain_length=2):
    """Generate lyrics using trained Markov chain."""
    if not markov_chain:
        return "Please train first with some lyrics"
        
    current_state = random.choice(list(markov_chain.keys()))
    lyrics = current_state.split()
    
    for _ in range(length - chain_length):
        possible_next_words = markov_chain.get(current_state, [])
        
        if not possible_next_words:
            break
            
        next_word = random.choice(possible_next_words)
        lyrics.append(next_word)
        current_state = ' '.join(lyrics[-chain_length:])
    
    return ' '.join(lyrics)

# Streamlit app
st.title("🎵 Advanced Lyrics Generator")

# File upload section
uploaded_file = st.file_uploader("Upload a text file with lyrics", type=['txt'])

# Text area for input lyrics (will be pre-filled if file is uploaded)
input_lyrics = st.text_area(
    "Or paste lyrics here:",
    help="You can use either file upload or paste text directly"
)

# If file is uploaded, read its contents
if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    input_lyrics = st.text_area(
        "Edit the uploaded lyrics if needed:",
        value=file_contents,
        height=300
    )

# Sidebar controls
with st.sidebar:
    st.header("Settings")
    chain_length = st.slider("Markov chain length", 1, 4, 2,
                           help="Higher values make output more similar to input")
    output_length = st.slider("Output length (words)", 10, 100, 30)
    generate_btn = st.button("Generate Lyrics")

# When generate button is clicked
if generate_btn:
    if not input_lyrics.strip():
        st.warning("Please provide some lyrics first (upload file or paste text)")
    else:
        with st.spinner("Training model and generating lyrics..."):
            try:
                model = train_markov_chain(input_lyrics, chain_length)
                generated = generate_lyrics(model, output_length, chain_length)
                
                st.subheader("Generated Lyrics")
                st.text_area("Your generated lyrics", 
                           value=generated, 
                           height=200,
                           label_visibility="collapsed")
                
                # Add download button
                st.download_button(
                    label="Download Lyrics",
                    data=generated,
                    file_name="generated_lyrics.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Add some instructions
st.markdown("""
### How to use:
1. Either upload a text file with lyrics OR paste lyrics in the text box
2. Adjust settings in the sidebar
3. Click "Generate Lyrics"
4. Enjoy your new song and download it if you like!

### Tips:
- Try different chain lengths to get different styles
- The more text you provide, the better the results
- You can edit uploaded lyrics before generating
""")