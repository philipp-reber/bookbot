def main():
    path = "books/Frankenstein.txt"
    book = get_book_text(path)
    num_words = count_words(book)
    dic = count_characters(book)
    dic_sorted_list = sort_dic(dic)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    for i in dic_sorted_list:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")

def count_words(book):
    words = book.split()
    return len(words)
    
def count_characters(book):
    characters = {}
    book = book.lower()
    for letter in book:
        if letter.isalpha():
            if letter in characters:
                characters[letter] += 1
            else: characters[letter] = 1
    return characters
    
def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book

def sort_dic(dic):
    sorted = []
    for char in dic:
        sorted.append({"char": char, "num": dic[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

main()