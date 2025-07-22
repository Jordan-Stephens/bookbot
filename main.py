def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(words):
    word_count = 0
    text = words.split()
    for word in text:
        word_count += 1
    return word_count

def main():
    words = get_book_text("books/frankenstein.txt")
    count = word_counter(words)
    return print(f"{count} words found in the document")


main()
