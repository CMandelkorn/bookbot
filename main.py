from stats import word_count,char_count,sort_data,value_sort
import sys

#Open file read to string.
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#Main
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    text = get_book_text(filepath)
    count_words = word_count(text)
    num_letters = char_count(text)
    sorted_dict = sort_data(num_letters)
    sorted_dict.sort(reverse=True,key = value_sort)
    text_cleaner = {ord('['): None, ord(']'): None}
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/{sys.argv[1]}...\n----------- Word Count ---------- \nFound {count_words} total words \n--------- Character Count -------")
    for dict in sorted_dict:
        print(f"{dict['alph']} {dict['num']}".translate(text_cleaner).strip("'").replace("'",":"))
    print("============= END ===============")
        
main()