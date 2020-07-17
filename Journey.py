# Dynamic typing
x = 5
print(type(x))

# Strong typing
try:
    "String" + 5
except Exception as ex:
    print(ex)

# Eveything is an object
type(1)
type("String")

# Variable assignement
variable = 'assigned value'
print(variable)

# Data types
a = 3
b = 7.3
c = "String"
d = True
e = None

# Expressions, statements literals
expressions = "produces" + "value" 
statements = print("does something")
literals = ['numeric', 'string', 'boolean', 'special', 'collections']

# Typecasting
x = 3
y = 'string'
str(x) + y

# Arithmetic operators (+, -, /, //, *, **, %)
x * y
27 % 5

# Arithmetic assignement operators (+=, -=, /=, //=, *=, **=, %=)
x += 6
print(x)

# Arithmetic operation precedence (PEMDAS)
PEMDAS = ['parenthesis, exponentiation, multiplication, division, addition, substraction']
7 * 5*(2 + 5**3- 18/9)

# Basic comparison operators (<, >, <=, >=, ==, !=)
17 != 56
a = 17
b = 9
c = 'correct'
d = 'incorrect'
if a <= b:
    print(c)
else:
    print(d)
    
# Logical operators (not, and, or)
w = (1,2,3)
x = 1
y = ()
bool(x)
"not returns true if operand is false"
not y
"and returns true if both operands are true"
x and w
"or returns true if one operand is true"
y and x
"see also: short circuits"

# Implicit boolean typecasting (Truthy and Falsy values)
Truthy = [1, 1.1, ' ', [1], {1}, (1)]
Falsy = [0, 0.0, '', [], {}, ()]

# Basic control flow (if, elif, else)
a = 17
b = 9
c = 'correct'
d = 'incorrect'
if a <= b:
    print(c)
elif c < d:
    print('dupa')
else:
    print(d)

# Iteration 
i = 0
while i < 10:
    if i % 2 == 0:
    
        print(i)
    i += 1
    
y = [3, 8, 17, 3, 12, 28]
len(y) == len(set(y))

for el in y:
    print(el + 1)

z = [val * 10 * i for i, val in enumerate(y)]
print(z)

list(enumerate(y))
tup = (6, 4)
x, y = tup
print(x, y)

dict0 = {
    'Jan' : 55,
    'Marian' : 99
}
for name in dict0.keys():
    print(name)

for age in dict0.values():
    print(age)

for name, age in dict0.items():
    print('%s ma %d lat' %(name, age))

dict1 = {}
dict1['Grzegorz'] = 21
dict1['Tomek'] = 30

dict2 = {
    'Jan': {
        'age': 20,
        'city': 'Warsaw',
        'hobby': 'Chess'
    }
}