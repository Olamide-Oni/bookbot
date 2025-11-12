import sys
from stats import get_num_words, char_counter, list_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1] 

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    char_count = char_counter(file_contents)

    new_list = list_dict(char_count)

    for item in new_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")


main()
