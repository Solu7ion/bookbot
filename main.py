def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_word(text)
    character_count = get_character_count(text)
    print(character_count)

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
main()




