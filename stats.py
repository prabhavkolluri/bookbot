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