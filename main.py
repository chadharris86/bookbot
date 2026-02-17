import sys
from stats import get_num_words
from stats import count_characters
from stats import counting_items

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ==============")
    print(f"I am reading the file at {book_path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count ---------")
    char_counts = count_characters(text)
    sorted_chars = counting_items(char_counts)
   
    for item in sorted_chars:
        character = item["char"]
        count = item["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    
    print("============= END ==================")
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
