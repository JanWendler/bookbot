from stats import get_num_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(book_path):
    text = ""
    with open(book_path) as b:
        text = b.read()
    return text


def print_report(path, words, count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dic in count:
        char = dic["char"]
        num = dic["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_characters(character_count)
    print_report(book_path, num_words, sorted_characters)
    

main()