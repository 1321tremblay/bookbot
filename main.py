import sys

from stats import count_char, count_words, format_count


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num_words = count_words(f"{sys.argv[1]}")
        letter = count_char(f"{sys.argv[1]}")
        formatted, count = format_count(letter, num_words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in formatted:
        values = list(item.values())
        first_value = values[0]
        if (
            isinstance(first_value, str)
            and len(first_value) == 1
            and first_value.isalpha()
        ):
            print(f"{values[0]}: {values[1]}")
    print("============= END ===============")


main()
