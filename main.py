from stats import get_num_words
from stats import count_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("DEBUG: length of text =", len(text))  # add this line
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    print(char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
