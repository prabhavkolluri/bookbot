from stats import get_num_words,get_letter_count

def get_book_text(filepath):
    book_text = ""
    num_words = 0

    with open(filepath) as file:
        book_text = file.read()
        num_words = get_num_words(book_text)
        print(f"{num_words} words found in the document")
        letter_count = get_letter_count(book_text)
        for letter in letter_count:
            print(f"'{letter}': {letter_count[letter]}")
    # return book_text

def main():
    get_book_text("./books/frankenstein.txt")

main()