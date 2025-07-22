from stats import word_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text("books/frankenstein.txt")
    count = word_counter(words)
    return print(f"{count} words found in the document")


main()
