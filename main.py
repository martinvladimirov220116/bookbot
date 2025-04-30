from stats import get_word_count
from stats import get_book_text
from stats import get_character_frequency
from stats import sorted_characters
import sys

def main():
    """
    Main function to run the book text extraction.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    
    # Path to the book file
    print(f"Analyzing book found at {book_path}...")
    # Extract text from the book
    main_book_text = get_book_text(book_path)
    print("----------- Word Count ----------")
    num_words = get_word_count(main_book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    # Get character frequency
    char_frequency = get_character_frequency(main_book_text)
    sorted_chars = sorted_characters(char_frequency)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    main()