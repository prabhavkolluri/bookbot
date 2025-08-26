from stats import get_num_words,get_letter_count,sorted_dict_list

def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():
    text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    sorted_letter_list = sorted_dict_list(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter_dict in sorted_letter_list:
        print(f"{letter_dict["char"]}: {letter_dict["num"]}")
    print("============= END ===============")

main()