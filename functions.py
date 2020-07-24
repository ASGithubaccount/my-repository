def _print_hello():
    print('hello')

print_hello()



def _print_name(name: str):
    print('hello %s'%(name))

print_name(5)

def _print_keywords(**kwargs):
    print("i'm %s and i'm %d"%(kwargs['name'],kwargs['age']))

Marek = {'name' : 'Marek', 'age' : 54}

print_keywords(**Marek)

def reverse_name(name: str) -> str:

    return name[::-1] 

print(reverse_name('Janusz'))

x=0
def outer():
    _x = 10
    def inner():
        x=100
        print('INNER: ',x)
    inner()
    print('OUTER: ',x)

outer()


moj_dict = {'a': 5}
x = 10

def change_x(x):
    x['b'] = 10
    x['a'] = 100

print(moj_dict)
change_x(moj_dict)
print(moj_dict)