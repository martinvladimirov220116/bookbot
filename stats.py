def get_book_text(book_path):
    """
    Extracts text from a book file.
    """
    with open(book_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def get_word_count(text):
    """
    Counts the number of words in the given text.
    """
    words = text.split()
    return len(words)

def get_character_frequency(text):
    """
    Counts the frequency of each character in the given text.
    """
    text = text.lower()
    frequency = {}
    # Remove non-alphabetic characters
    text = ''.join(filter(str.isalpha, text))
    # Count character frequency
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sorted_characters(dict):
    """
    Sorts the character frequency dictionary in descending order.
    """
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)