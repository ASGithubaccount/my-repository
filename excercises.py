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

medium point = len / 2 ?
palindrome = something [medium point:] == something [:medium point][::-1]

   


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
casting, intersection of two sets

# 12. Write a Python program to print a specified list 
# after removing the 0th, 4th and 5th elements



