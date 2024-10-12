class MyClass:
    def __init__(self, name, age, address):
        self.name = name 
        self.age = age
        self.address = address

    def info(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\n"
    
obj1 = MyClass('Bob', 18, "London")
obj2 = MyClass("Anna", 18, 'Russia')
obj3 = MyClass('Safia', 17, 'Germany')

print(obj1.info())
print(obj2.info())
print(obj3.info())