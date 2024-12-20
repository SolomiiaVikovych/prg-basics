# Paragraph input
paragraph = "cat dog mouse cat rat cat mouse"

# Initialize an empty dictionary to store word counts
word_counts = {}

# Split the paragraph into words
words = paragraph.split()

# Iterate over each word
for word in words:
    # Check if the word is already in the dictionary
    if word in word_counts:
        # Increment the count for the word
        word_counts[word] += 1
    else:
        # Add the word to the dictionary with a count of 1
        word_counts[word] = 1

# Print the word counts
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
