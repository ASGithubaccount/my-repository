# 1. Write a Python script to sort (ascending and descending) a dictionary by value
dict1 = {3: "dupa", 6: "dskal", 2: "g34"}
asc_dict = sorted(dict1.items(), key=lambda item: item[1], reverse=True)

print(asc_dict)

# 2. Write a Python script to add a key to a dictionary
dict2 = {'0': 10, 1: 20}
dict2[3] = 30

# 3. Write a Python script to concatenate following dictionaries to create a new one

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
print({**dic1, **dic2, **dic3})
sum_dic = {**dic1, **dic2, **dic3}

# 4. Write a Python script to check whether a given key already exists in a dictionary

key1 = "dupa"
key2 = 2

dict4 = {7: "dupa", 2: "21312", 9: "sadfas"}
print(key2 in dict4.values())

# 5. Write a Python program to iterate over dictionaries using for loops
# 3 różne list comprehensions printujące : keys, values and items
dict5 = {3: "dupa", 6: "dskal", 2: "g34"}

for key, val in dict5.items():
    print(key, '=', val)

dict5 = [print(key, '=', val) for key, val in dict5.items()]

# 6. Write a Python script to generate and print a dictionary that contains 
# a number (between 1 and n) in the form (x, x*x)
# Sample input ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def func6(n):
    result = {}
    for x in range(1, n+1):
        result[x] = x*x
    print(result)
    print({x:x**2 for x in range(1, n+1)})

func6(5)



# 7. Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of keys

func6(15)


# 8. Write a Python script to merge two Python dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = {**d1, **d2}
print(d1)

# 9. Write a Python program to iterate over dictionaries using for loops

# 10. Write a Python program to sum all the items in a dictionary

# 11. Write a Python program to multiply all the values in a dictionary
dict11 = {'data1':3,'data2':4,'data3':10}
import functools as ft


result = ft.reduce(lambda x,y : x*y, dict11.values())
print(result)

# 12. Write a Python program to remove a key from a dictionary
dict12 = {'data1':3,'data2':4,'data3':10}

del dict12['data1']
print(dict12)

# 13. Write a Python program to map two lists into a dictionary
l1 = ['a', 'c', 'b', 'd']
l2 = [100, 300, 400, 200]
print(list(zip(l1, l2)))

dict13 = {}
for key, val in list(zip(l1, l2)):
    dict13[key] = val
print(dict13)

dict13 = {key: val for key, val in list(zip(l1, l2))}
print(dict13)

# 14. Write a Python program to sort a dictionary by key
dict14 = {3: "dupa", 6: "dskal", 2: "g34"}
sorted_dict14 = sorted(dict14.items(), key=lambda item: item[0])
print(sorted_dict14)

# 15. Write a Python program to get the maximum and minimum value in a dictionary
dict15 = {'data1':3,'data2':4,'data3':10}
print(min(list(dict15.values())))

# 16. Write a Python program to get a dictionary from an object's fields


# 17. Write a Python program to remove duplicates from Dictionary
dict17 = {'data1':3,'data2':4,'data3':10, 'data4':4}
new_dict17 = {}
for key, val in dict17.items():
    if val in new_dict17.values():
        continue
    new_dict17[key] = val
print(new_dict17)