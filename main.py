from stats import word_counter, num_of_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    words = get_book_text("books/frankenstein.txt")
    word_count = word_counter(words)
    character_count = num_of_chars(words)
    
    return print(f"{word_count} words found in the document"), print(character_count)


main()
