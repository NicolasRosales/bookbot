from stats import *
import sys

def sort_on():
    return

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #print(get_book_text("./books/frankenstein.txt"))
    file_path = sys.argv[1]
    file_text = get_book_text(file_path)
    words_count = count_words(file_text)
    caracters_count = count_caracters(file_text)
    sorted_by_char = dict(sorted(caracters_count.items(), key=lambda item: item[1], reverse=True))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    
    for k, v in list(sorted_by_char.items()):
        print(f"'{k}: {v}'")

    print("============= END ===============")



main()