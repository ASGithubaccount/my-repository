# List
homogenic=[1,2,3,4,5]
heterogenic=[1,6.7,True,"String",None]
matrix=[[1,2,3,4,5],[],["String",None]]
print(matrix[2][0])
matrix[0]=123
print(matrix[0])

# Tuple
matrix=(6,7,8,9)
matrix[0]=987

# Set
unique_values={1,2,3,1}
print(unique_values)

# Dictionary
dict0={"sokol":32,'maj':30}
print(dict0['sokol'])

# Sequence operator
print(123 not in matrix)
heterogenic*3

# List comprehension
long=[val for val in range(10)]
long
long[::-1]

# slice[start:stop:step]

len(long)
min(long)
max(long)
