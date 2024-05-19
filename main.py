
def main():
    book_path = "books/frankenstein.txt"
    book_contents = read_book_contents(book_path)
    word_count = get_num_words(book_contents)
    chars_dict = get_chars_dict(book_contents)
    chars_array = get_alpha_chars_array(chars_dict)
    chars_array.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in chars_array:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print(f"--- End report ---")


def read_book_contents(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    word_array = text.split()
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

def get_alpha_chars_array(chars_dict):
    chars_array = []
    for k in chars_dict:
        if k.isalpha():
            element = {'char': k, 'num': chars_dict[k]}
            chars_array.append(element)
    return chars_array

def sort_on(dict):
    return dict["num"]
    

main()
