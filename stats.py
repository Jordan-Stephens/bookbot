def word_counter(words):
    word_count = 0
    text = words.split()
    for word in text:
        word_count += 1
    return word_count
