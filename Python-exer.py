"""
Exercise 1: Reverse each word of a string
Given:

str = 'My Name is Jessa'
Expected Output

yM emaN si asseJ  

"""
#def reverse_words(str):
#    words = str.split(" ")
#    new_words_list = [word[::-1] for word in words]
#    return " ".join(new_words_list)

#str1 = "My name is ilyas"
#print(reverse_words(str1))

"""
Exercise 2: Read text file into a variable and replace all newlines with space
Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5

Expected Output:
Line1 line2 line3 line4 line5

"""
#with open('sample.txt', 'r') as file:
#    data = file.read().replace('\n', ' ')
#    print(data)

"""
Exercise 3: Remove items from a list while iterating
Description:

In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50

Given:

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected Output: -

[10, 20, 30, 40, 50]
"""
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(number_list) - 1, -1, -1):
    if number_list[i] > 50:
        del number_list[i]
print(number_list)