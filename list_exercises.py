# 1. Write a Python program to sum all the items in a list

l = [2, 5, 7, 4, 9]
list_sum = sum(l)
print(list_sum)

list_sum = 0
for i in l:
    list_sum += i
list_sum

# 2. Write a Python program to multiplies all the items in a list

l = [2, 5, 7, 4, 9]
list_multi = 1
for i in l:
    list_multi *= i
list_multi

# 3. Write a Python program to get the largest number from a list

l = [2, 5, 7, 4, 9]
list_max = max(l)
list_max

# 4. Write a Python program to get the smallest number from a list

l = [2, 5, 7, 4, 9]
list_min = min(l)
list_min

# Write a Python program to count the number of strings where the
# string length is 2 or more and the first and last character are
# same from a given list of string
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2 

sample_list = ['abc', 'xyz', 'aba', '1221']

def func5(sample_list):
  counter = 0

  for x in sample_list:
    if len(x) > 1 and x[0] == x[-1]:
      counter += 1
  return counter

print(func5(sample_list))


counter = 0
for x in sample_list:
    if len(x) > 1 and x == x[::-1]:
        counter += 1

    



# 6. Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def func(tup):
    return tup[-1]     

result = sorted(sample_list, key=lambda tup: tup[-1])
print(result)

# 7. Write a Python program to remove duplicates from a list

l = [2, 5, 7, 2, 9]
set(l)

# 8. Write a Python program to check a list is empty or not

l = [2, 5, 7, 4, 9]
empty_list = []
bool(l)
bool(empty_list)

# 9. Write a Python program to clone or copy a list
# from copy import deepcopy
# list_copy = deepcopy(l)

l = [2, 5, 7, 4, 9]
list_copy = l[:]
id([2, 5, 7, 4, 9])
id(l)
id(list_copy)

# 10. Write a Python program to find the list of words that
# are longer than n from a given list of words

def func10(n, word_list):
    return [ word for word in word_list if len(word) > n]

    

# 11. Write a Python function that takes two lists and 
# returns True if they have at least one common member

x = [1,2,3,4,5]
y = [0,6,7,8,9]
x + y != set(x + y)

x = ["apple", "banana", "cherry"]
y = ["google", "microsoft", "apple"]

print(bool(set(x).intersection(set(y))))

a = set(x)
b = set(y)

have_common_member = a.intersection(b)

print(bool(have_common_member))

# 12. Write a Python program to print a specified list 
# after removing the 0th, 4th and 5th elements

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list.pop()
sample_list.pop()
sample_list.pop(0)
print(sample_list)

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del sample_list[4:]
del sample_list[0]
print(sample_list)

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample_list = [x for (i,x) in enumerate(sample_list) if i not in (0,4,5)]
print(sample_list)

# 13. Write a Python program to generate a 3*4*6 3D array
# whose each element is *

array = [[ ['*' for column in range(6)] for column in range(4)] for row in range(3)]
print(array)

# 14. Write a Python program to print the numbers of a 
# specified list after removing even numbers from it

sample_list = [1, 4, 8, 3, 7, 1, 5, 6]
odd_list = [n for n in sample_list if n % 2 != 0]

print(odd_list)

# 15. Write a Python program to shuffle and print a specified list

list15 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
from random import shuffle
shuffle(list15)

print(list15)

# 16. Write a Python program to generate and print a list of first 
# and last 5 elements where the values are square of numbers between 
# 1 and 30 (both included)

num_range = (1,30)
square_list1 = [x*x for x in range(1,num_range)[:5]]
square_list2 = [x*x for x in range(1,num_range)[-5:]]
final_square_list = [square_list1 + square_list2]
print(final_square_list)

# 17. Write a Python program to generate and print a list except for 
# the first 5 elements, where the values are square of numbers between 
# 1 and 30 (both included)

square_list = [x*x for x in range(6,31)]
print(square_list)

# 18. Write a Python program to generate all permutations of a list
# in Python

import itertools
itertools.permutations([1,2,3])
print(list(itertools.permutations([1,2,3])))

# 19. Write a Python program to get the difference between the two lists

x = ["apple", "banana", "cherry"]
y = ["google", "microsoft", "apple"]

a = set(x)
b = set(y)

c = a.intersection(b)
d = set(x + y) - c

print(d)

# 20. Write a Python program access the index of a list

list20 = [7, 86, 12, 3, 687, 13, 236]
x = [print('%d: %d' % (x, i)) for i, x in enumerate(list20)]
print(list(enumerate(list20)))

# 21. Write a Python program to convert a list of characters into a string

list_21 = ['s', 't', 'r', 'i', 'n', 'g']
string_from_list = "".join(list_21)
print(string_from_list)

# 22. Write a Python program to find the index of an item in a specified list

list22 = [7, 86, 12, 3, 687, 13, 236]
print(list22.index(86))

# 23. Write a Python program to flatten a shallow list

list23 = [[2,4,3],[1,5,6], [9], [7,9,0]]
print(sum(list23,[]))

from itertools import chain
print(list(itertools.chain(*list23)))


# 24. Write a Python program to append a list to the second list

list24a = [7, 86, 12, 3, 687, 13, 236]
list24b = ['s', 't', 'r', 'i', 'n', 'g']
list24c = list24a + list24b

print(list24c)

# 25. Write a Python program to select an item randomly from a list

import random

list25 = [7, 86, 12, 3, 687, 13, 236]
print(random.choice(list25))

# 26. Write a python program to check whether two lists are circularly identical

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# 27. Write a Python program to find the second smallest number in a list

list27 = [7, 86, 12, 3, 687, 13, 236]

list27.sort()
print(list27[1])

# 28. Write a Python program to find the second largest number in a list

list28 = [7, 86, 12, 3, 687, 13, 236]

list28.sort(reverse=True)
print(list28[1])

# 29. Write a Python program to get unique values from a list

list29 = [7, 86, 7, 3, 687, 13, 236, 687]
print(set(list29))

# 30. Write a Python program to get the frequency of the elements in a list



# 31. Write a Python program to count the number of elements in a list within a specified range

