# A pronic number is a number which is the product of two consecutive integers.
import math
def is_pronic(n):
    number = int(math.sqrt(n))
    return n == number * (number + 1)

print(is_pronic(11))    