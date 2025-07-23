from stats import word_counter, num_of_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
book_dir = "books/frankenstein.txt"

def main():
    words = get_book_text(book_dir)
    word_count = word_counter(words)
    character_count = num_of_chars(words)
    sorted =  sort_chars(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_dir}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")
    return

main()
