def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_word(text)
    character_count = get_character_count(text)
    dict_sort = get_dict_sort(character_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for item in dict_sort:
        if item["name"].isalpha():
            print(f"The '{item["name"]}' character was found {item["num"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_word(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] =1
    return chars

def get_dict_sort(dict_list):
    sorted_list = []
    def sort_on(dict):
        return dict["num"]
    for char in dict_list:
        sorted_list.append({"name": char, "num": dict_list[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
