def get_num_words(book_string):
    num_words = len(book_string.split())
    return num_words
   

def char_counter(book_string):
    char_count_dict = {}
    book_string_lower = book_string.lower()
    for char in book_string_lower:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1 
        """
        try:
           char_count_dict[char] += 1
        except:
            char_count_dict[char] = 1
        """
                 
    return char_count_dict

def sort_on(items):
    return items["num"]

def list_dict(dict):
    list_of_dict = list(dict.items())

    for i in range(len(list_of_dict)):
        list_of_dict[i] = {"char": list_of_dict[i][0], "num" : list_of_dict[i][1]}

    list_of_dict.sort(reverse=True, key=sort_on)
        
    return list_of_dict

    

