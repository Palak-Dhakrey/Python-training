def accumulate_word_lengths(words):
    length_dict = {}  
    for word in words:
        word_length = len(word)
        if word_length in length_dict:
            length_dict[word_length].append(word)
        else:
            length_dict[word_length] = [word]
    return length_dict
words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
result = accumulate_word_lengths(words)
print(result)
