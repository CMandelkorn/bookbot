#Word count function, takes string counts words.
def word_count(text):
    words = text.split()
    word_total = 0
    for word in words:
        word_total += 1
    return word_total

#Char count
def char_count(text):
    char_string = list(text.lower())
    letters = {} 
    for c in char_string:
        letters[c] = letters.get(c,0)+1
    return(letters)

#Sorts data from char_count makes two dictionaries only if key value is alphabetic
def sort_data(num_letters):
    dict_list = []
    for key, value in num_letters.items():
        if key.isalpha():
            dict_list += [{"alph":[key], "num":[value]}]
    return(dict_list)

#used to return key to sort by
def value_sort(dict_list):
    return dict_list["num"]
    