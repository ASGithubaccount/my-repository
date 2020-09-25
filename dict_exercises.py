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

print(x)

