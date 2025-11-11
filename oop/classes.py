'''
Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. 
Include a method to display student information.
'''

class Student:
    def __init__(self, firstname, lastname, age, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.grade = grade
        
    def get_descriptive_name(self):
        full_name = f"{self.firstname} {self.lastname} - is in grade {self.grade}"
        return full_name
        
new_student = Student("Jane", "Doe", 8, "three")
print(new_student.get_descriptive_name())


'''
Exercise 2: Creating a Product Catalog
Instruction:
Define a Product class with attributes like name, price, and quantity. 
Implement a method to calculate the total value of products in stock.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity 
        
    def total_products_in_stock(self):
        total = self.price * self.quantity
        return  f"The total value of {self.name} is {total}"
    
new_product = Product("Milk", 20, 10)
print(new_product.total_products_in_stock())