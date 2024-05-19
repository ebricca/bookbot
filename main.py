
def main():
    book_path = "./books/frankenstein.txt"
    book_contents = read_book_contents(book_path)
    word_count = count_words(book_contents)
    print(f"{word_count} words found in the document")

def read_book_contents(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(string):
    word_array = string.split()
    return len(word_array)

main()