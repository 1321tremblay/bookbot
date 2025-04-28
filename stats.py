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


def count_char(file_path):
    book_content = get_book_text(file_path)
    letters = {}
    for letter in book_content:
        lowercase = letter.lower()
        letters.setdefault(lowercase, 0)
        if letters[lowercase] >= 0:
            letters[lowercase] += 1
    return letters


def format_count(character_dictionaries, word_count):
    def sort_on(dict):
        return dict["num"]

    formatted_list = [
        {"char": key, "num": value} for key, value in character_dictionaries.items()
    ]
    formatted_list.sort(reverse=True, key=sort_on)
    count = word_count

    return formatted_list, count


# def format_count(count_char, word_count):
#     seperated_list = [{"char": key, "num": value} for key, value in count_char.items()]
#     count = word_count
