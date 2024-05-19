
def main():
    book_path = "./books/frankenstein.txt"
    book_contents = read_book_contents(book_path)
    letter_count = get_chars_dict(book_contents)
    print(letter_count)

def read_book_contents(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(string):
    word_array = string.split()
    return len(word_array)

def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict



main()