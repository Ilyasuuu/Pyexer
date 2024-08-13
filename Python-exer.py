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
#def manipulate(x, y):
#    # concatenate two strings
#    def inner_fun(x, y):
#        return x + y

#    z = inner_fun(x, y)
#    return z + 'Developers'

#result = manipulate('Emma', 'Kelly')
#print(result)

"""
Exercise 9: Modify the element of a nested list inside the following list
Change the element 35 to 3500

Given:

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
Expected Output: -

[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]
"""
#list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# modify item
#list1[1][2][2][1]= 3500
# print final result
#print(list1)
"""
Exercise 2: Capitalize the First and Last Character of Each Word
Given:
str = 'hello world from python'
Expected Output:
HellO WorlD FroM PythoN
"""

#str = 'hello world from python'
#words = str.split(" ")
#capitalized_words = [word.capitalize() if len(word) == 1 else word[0].upper() + word[1:-1] + word[-1].upper() for word in words]
#print(" ".join(capitalized_words))

"""
Exercise 3: Remove Duplicate Characters from Each Word
Given:
str = 'programming is fun'
Expected Output:
progamin is fun
"""
#sentence = 'programming is fun'

#def remove_duplicates(word):
#    seen = set()
#    result = []
#    for char in word:
#        if char not in seen:
#            result.append(char)
#            seen.add(char)
#    return "".join(result)

#words = sentence.split()
#nique_words = [remove_duplicates(word) for word in words]
#word_input = " ".join(unique_words)
#print(word_input)

"""
Exercise 4: Sort Characters of Each Word Alphabetically
str = 'python coding is awesome'
Expected Output:
hnopty cdgino is aeemosw

"""
#str = 'python coding is awesome'
#str_splt = str.split()
#sorted_str = [''.join(sorted(word)) for word in str_splt]
#new_str = " ".join(sorted_str)
#print(new_str) 

"""
Exercise 5: Replace Vowels with the Next Vowel in Each Word
Given:
str = 'hello world from python'
Expected Output:
hillu wurld frum pythun

"""
#str = 'hello world from python'

#def next_vowel(char):
#    vowels = 'aeioua'
#    if char in vowels:
#        return vowels[vowels.index(char) + 1]
#    return char


#def replace_vowels(word):
#    return ''.join(next_vowel(char) for char in word)

#words = str.split()
#replaced_words = [replace_vowels(word) for word in words]
#final_str = ' '.join(replaced_words)

#print(final_str)

"""
Exercise 6: Reverse the Order of Words in a Sentence
"""
#sentence = "My name is Ilyas"
#split_words = sentence.split()
#reversed_words = split_words[::-1]
#print(" ".join(reversed_words))  

"""
Exercise 7: Count the Number of Each Vowel in a String
"""
#sentence = 'Count the number of each vowel in this sentence'
#vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
#for vowel in sentence.lower():
#    if vowel in vowel_counts:
#        vowel_counts[vowel] += 1
#print(vowel_counts)

"""
Exercise 8: Check if Two Strings are Anagrams
"""
#def Are_Anagrams(str1, str2): return sorted(str1.lower()) == sorted(str2.lower())    
#ord1 = 'ilyas'
#ord2 = 'sayli'
#print(Are_Anagrams(word1, word2))    

"""
Exercise 9: Find all subsrtings of a string
"""
#def find_substrings(sub):
#    substrings = []
#    for i in range(len(sub)):
#        for j in range(i + 1, len(sub) + 1):
#            substrings.append(s[i:j])
#    return substrings

#s = "abcde"
#print(find_substrings(s))

"""
EX 10: Convert a String to Snake Case
"""
#def to_snake_case(s):
#    snake_case_str = ''
#    for char in s:
#        if char.isupper():
#            if snake_case_str:# this condition prevents adding an _ at the beginning
 #               snake_case_str += '_'
#            snake_case_str += char.lower()
#        else:
#            snake_case_str += char
#    return snake_case_str

#input_str = 'ConvertThisStringToSnakeCase'
#print(to_snake_case(input_str))

"""
ex18: Rotate a Matrix by 90 Degrees Clockwise
"""
#def rotate_matrix(matrix):
#    n = len(matrix)
#    for row in range(n):
#        for col in range(row, n):
#            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
#    for row in range(n):
#        matrix[row].reverse()

#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#rotate_matrix(matrix)
#print(matrix)

"""
Exercise 17: Implement a Queue Using Two Stacks
Objective:
Implement a queue using two stacks.
Description:
A queue follows the First-In-First-Out (FIFO) principle. You need to implement the following operations using two stacks:
enqueue(x): Add an element x to the end of the queue.
dequeue(): Remove the element from the front of the queue.
"""
'''
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())   
print(queue.dequeue())   
queue.enqueue(4)
print(queue.dequeue())   
print(queue.dequeue())   '''

'''
Exercise 18: Implement a Simple Caesar Cipher
Objective:
Implement a function that encodes a string using a Caesar cipher. The Caesar cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet.

Description:
You need to implement a function that takes a string and an integer shift value and returns the encoded string.'''
#def caesar_cipher(s, shift):
#    encoded_str = ''
#    for char in s:
#        if char.isalpha():
#            shift_base = ord('A') if char.isupper() else ord('a')
#            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
#            encoded_str += encoded_char
#        else:            encoded_str += char
#    return encoded_str

#input_str = 'See you later'
#shift_value = 2
#print(caesar_cipher(input_str, shift_value))  

import itertools as its
def fizz_buzz(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, its.count(1)))
    for i in its.islice(result, 100):
        print(i)

fizz_buzz(101)