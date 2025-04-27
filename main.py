def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content


def count_words(file_path):
    book_content = get_book_text(file_path)
    book_letter = book_content.split()
    counter = 0
    for char in book_letter:
        counter += 1
    return counter


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    num_words = count_words("./books/frankenstein.txt")
    print(f"{num_words} words found in the document")


main()
