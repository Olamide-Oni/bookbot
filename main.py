from stats import get_num_words, char_counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    char_count = char_counter(file_contents)
    print(f"{char_count}")



main()
