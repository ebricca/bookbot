
def main():
    book_path = "./books/frankenstein.txt"
    book_contents = read_book_contents(book_path)
    letter_count = count_letters(book_contents)
    print(letter_count)

def read_book_contents(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(string):
    word_array = string.split()
    return len(word_array)

def count_letters(string):
    letter_dict = {}
    word_array = string.split()
    for word in word_array:
        new_word = word.lower()
        for letter in new_word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict



main()