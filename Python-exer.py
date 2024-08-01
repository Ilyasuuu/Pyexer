"""
Exercise 1: Reverse each word of a string
Given:

str = 'My Name is Jessa'
Expected Output

yM emaN si asseJ  

"""
def reverse_words(str):
    words = str.split(" ")
    new_words_list = [word[::-1] for word in words]
    return " ".join(new_words_list)

str1 = "My name is ilyas"
print(reverse_words(str1))
