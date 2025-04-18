def create_inverted_index(sentences):
    inverted_index = {}
    for index, sentence in enumerate(sentences):
        words = sentence.split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            if index not in inverted_index[word]:
                inverted_index[word].append(index)
    return inverted_index
sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
result = create_inverted_index(sentences)
print(result)
