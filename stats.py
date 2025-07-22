def word_counter(words):
    word_count = 0
    text = words.split()
    for word in text:
        word_count += 1
    return word_count

def num_of_chars(words):
    words = words.lower()
    counts = {}
    for character in words:
        if character not in counts:
            counts[f"{character}"] = 1
        else:
            counts[f"{character}"] += 1
    return counts

