class Human :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print(self.name)



John = Human('Name', 54)
John.print_name()

