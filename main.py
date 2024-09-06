def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_word(text)
    print(f"words: {num_words}")



    lower_text = get_lower_words(text)
    character_count = get_character_count(lower_text)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_word(text):
    words = text.split()
    return len(words)

def get_lower_words(text):
    lowered_text = text.lower()
    return lowered_text

def get_character_count(lower_text):
    lower_string = lower_text.split() 
    character_count = {}
    for word in lower_string:
        for char in word:
            if char in character_count:
                character_count[char] +=1
            else:
                character_count[char] = 1
    return character_count
main()




