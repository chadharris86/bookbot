def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase_text = text.lower()
    char_counts = {}

    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_one(dict):
    return dict["num"]

def counting_items(char_counts):
    items_list = []
   
    

    for char, count in char_counts.items():
        char_dict = {"char": char, "num": count}
        items_list.append(char_dict)
        
    items_list.sort(reverse=True, key=sort_one)
    return items_list
       


        
