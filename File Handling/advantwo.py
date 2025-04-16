#2.----Word Frequency Counter
#Read st.txt and create a dictionary of word frequency (how many times each word appears), and write it to frequency.txt.
from collections import Counter
import re
with open("story.txt", "r") as file:
    text = file.read().lower()
words = re.findall(r'\b\w+\b', text)
frequency = Counter(words)
with open("frequency.txt", "w") as outfile:
    for word, count in frequency.items():
        outfile.write(f"{word}: {count}\n")