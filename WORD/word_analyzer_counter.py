# Word Counter & Analyzer
def word_counter(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text.replace(" ", ""))  # Exclude spaces
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    print("\n📊 Text Analysis Results:")
    print(f"📚 Total Words: {word_count}")
    print(f"📚 Total Characters (no spaces): {char_count}")
    print(f"📚 Average Word Length: {avg_word_length:.2f} letters")

    # Bonus: Most common words
    from collections import Counter
    common_words = Counter(words).most_common(3)
    print("\n📝 Top 3 Frequent Words:")
    for word, count in common_words:
        print(f"'{word}': {count} times")

# Get user input
user_text = input("🚀 Enter your text: ")
word_counter(user_text)