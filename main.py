from stats import get_num_words,get_letter_count,sorted_dict_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():

    # Exit program if program command is executed incorrectly
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Run as normal if command is executed correctly
    else:
        text = get_book_text(sys.argv[1])

        num_words = get_num_words(text)
        letter_count = get_letter_count(text)
        sorted_letter_list = sorted_dict_list(letter_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for letter_dict in sorted_letter_list:
            print(f"{letter_dict["char"]}: {letter_dict["num"]}")
        print("============= END ===============")

main()