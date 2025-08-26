def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def get_letter_count(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():    
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

def sort_on(item):
    return item["num"]

def sorted_dict_list(letter_count):
    list_to_sort = []
    for letter in letter_count:
        list_to_sort.append({"char": letter, "num": letter_count[letter]})

    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort

    