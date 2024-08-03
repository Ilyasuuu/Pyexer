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
#number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#for i in range(len(number_list) - 1, -1, -1):
#    if number_list[i] > 50:
#        del number_list[i]
#print(number_list)

"""
Exercise 4: Reverse Dictionary mapping
Given:

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
Expected Output:

{65: 'A', 66: 'B', 67: 'C', 68: 'D'}
"""
#ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Reverse mapping
#new_dict = {value: key for key, value in ascii_dict.items()}
#print(new_dict)

"""
Exercise 5: Display all duplicate items from a list
Given:

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
Expected Output: -

[20, 60, 30]
"""
#import collections

#sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

#duplicates = []
#for item, count in collections.Counter(sample_list).items():
#    if count > 1:
#       duplicates.append(item)
#print(duplicates)

"""
Exercise 7: Print the following number pattern
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""
#rows = 5
#x = 0
#for i in range(rows, 0, -1):
#    x += 1
#    for j in range(1, i + 1):
#        print(x, end=' ')
#    print('\r')

"""
Exercise 8: Create an inner function
Question description: -

Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.
Expected Output: -

EmmaKellyDevelopers
"""
def manipulate(x, y):
    # concatenate two strings
    def inner_fun(x, y):
        return x + y

    z = inner_fun(x, y)
    return z + 'Developers'

result = manipulate('Emma', 'Kelly')
print(result)