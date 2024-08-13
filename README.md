# test1
this is my homework
# 1. create a class called person with attributes name and age. Create an object of the cass and print its attributes.
# class person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
# ali=person('ali',20)
# print(ali.name)
# print(ali.age)

# 2. add a method called greet to the person class that prents a greeting message including the person's name.


# class greeitng:
#     def __init__(self,name, hal):
#         self.name=name
#         self.hal= hal
# salaam= greeitng('ali','how are you?')
# print(salaam.hal)

#3. create a class called car with attributes make, model, and year.Inclode a method to print out the car's details.
# class car:
#     def __init__(self, model , year):
#         self.model= model
#         self.year=year
#     def detail(self):
#         return f'its model is {self.model} and its year is {self.year}'
# coroll=car(2000,2020)
# print(coroll.detail())

#4.create a class circle with a method to compute the area. intialize the class with the readius.

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# # Example usage:
# circle = Circle(5)
# print(f"The area of the circle with radius {circle.radius} is {circle.area()}.")

#5.create a class rectangle with methods to compute the area of perimeter. Intiaoize the class with the lenght and width.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # Example usage:
# rect = Rectangle(5, 3)
# print("Area:", rect.area()) 


# Inheritance and polymorphism exercises
#6. create a base cass animal with a method speak. create tow derived classes Dog and cat that ovrride the speak method.

#Here’s a Python implementation of a base class `Animal` with a method `speak`, along with two derived classes `Dog` and `Cat` that override the `speak` method:


# class Animal:
#     def speak(self):
#         # raise NotImplementedError("Subclasses must implement this method")
#         return 'haywanat'

# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # Example usage:
# dog = Dog()
# cat = Cat()

# print("Dog:", dog.speak())  # Output: Dog: Woof!
# print("Cat:", cat.speak())  # Output: Cat: Meow!
# # ```

# In this example:
# - The `Animal` class is the base class with a `speak` method that raises a `NotImplementedError`, enforcing that derived classes must provide their own implementation.
# - The `Dog` and `Cat` classes override the `speak` method to return their respective sounds.
# 6.create a base class shape with a metod area. create derived classes square and tringle that implement the area method.

# class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# # استفاده نمونه:
# square = Square(4)
# print(f"مساحت مربع: {square.area()}")

# triangle = Triangle(3, 6)
# print(f"مساحت مثلث: {triangle.area()}")



# 7. create a base class employee with attributes name and salary. creatre a derived class amnager with an additional attribute department.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display_info(self):
#         super().display_info()
#         print(f"Department: {self.department}")


# # Example usage
# emp = Employee("John Doe", 50000)
# emp.display_info()

# mgr = Manager("Jane Smith", 75000, "HR")
# mgr.display_info()

# 8.create a base class vehicle with a method drive create derived classes bike and truck that override the drive method
# class vehicle:
#     def drive(self):
#         print('riding a vehicle')



# class bike(vehicle):
#     def drive(self):
#         print('riding a bike')

# class truck(vehicle):
#     def derive(self):
#         print('riding a truck')

# v=vehicle()
# v.drive()

# bi=bike()
# bi.drive()

# tr=truck()
# tr.derive()

#     10.create a base class bird with a method fly.create derived class eagle and penguin .override the fly method in penguin to indicate that penguins cannot fly.
# class bird:
#     def fly(self):
#         print('some birds can flying')

# class eagle(bird):
#     def fly(self):
#         print('eagle can fly')

# class penguin(bird):
#     def fly(self):
#         print('penguin can not flying')

# b=bird()
# b.fly()

# eag = eagle()
# eag.fly()

# pen=penguin()
# pen.fly()


# Encapsulation and Abstraction Exercises
# 11. Create a class Account with private attributes balance. Provide public methods to deposit and 

# class Account:
#     def __init__(self, balance):
#         self.__balance = balance  # متغیر خصوصی برای نگهداری موجودی حساب

#     # متد برای واریز به حساب
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"${amount} واریز شد. موجودی فعلی: ${self.__balance}")
#         else:
#             print("مبلغ واریزی باید بیشتر از صفر باشد.")

#     # متد برای برداشت از حساب
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"${amount} برداشت شد. موجودی فعلی: ${self.__balance}")
#         else:
#             print("مبلغ برداشت نامعتبر است یا موجودی کافی نیست.")

# # استفاده از کلاس:
# acc = Account(1000)
# acc.deposit(500)  # واریز 500 دلار
# acc.withdraw(200) # برداشت 200 دلار


# 12. Create a class Book with private attributes title, author, and pages. Provide public methods to get 
# and set these attributes.
# class Book:
#     def __init__(self, title, author, pages):
#         self.__title = title
#         self.__author = author
#         self.__pages = pages


#     def get_title(self):
#         return self.__title

#     def get_author(self):
#         return self.__author

#     def get_pages(self):
#         return self.__pages

 
#     def set_title(self, title):
#         self.__title = title

#     def set_author(self, author):
#         self.__author = author

#     def set_pages(self, pages):
#         self.__pages = pages


# book = Book("afghanistan", "ahmad", 328)

# print(book.get_title())  
# print(book.get_author()) 
# print(book.get_pages())  

# book.set_title("Animal")
# book.set_author("tmas")
# print(book.set_pages(112))

# print(book.get_title())  
# print(book.get_pages())  

# 13. Create a class Laptop with private attributes brand, model, and price. Provide a method to apply 
# a discount and a method to display laptop details.
# class laptop:
#     def __init__(self,brand,model,price):
#         self.__brand=brand
#         self.__model=model
#         self.__price=price
#     def discount(self):
#         if self.__price >=10000:
#             self.__price -=1000
#             print()
#         else:
#             print('yout laptop dont hane any discount')
#     def dis_laptop(self):
#         print(f'brand{self.__brand} ,model {self.__model} and with price { self.__price}')


# lap= laptop(2000,'dell',12000)
# lap.dis_laptop()
# lap.discount() 
# 14. Create a class Bankammount with private attributes account_number and balance. Provide 
# methods to deposit, withdraw, and check the balance.
# class BankAccount:
#     def __init__(self, account_number, initial_balance=0):
#         self.__account_number = account_number
#         self.__balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance is {self.__balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance is {self.__balance}.")
#         else:
#             print("Withdrawal amount must be positive and no more than the current balance.")

#     def check_balance(self):
#         return self.__balance

# # Example usage
# account = BankAccount("123456789", 100)
# account.deposit(50)
# account.withdraw(30)
# print("Current balance:", account.check_balance())

# 15. Create a class Student with private attributes name, grade, and age. Provide methods to get and 
# set these attributes and a method to display the student's details
# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age

#     # Getter methods
#     def get_name(self):
#         return self.__name

#     def get_grade(self):
#         return self.__grade

#     def get_age(self):
#         return self.__age

#     # Setter methods
#     def set_name(self, name):
#         self.__name = name

#     def set_grade(self, grade):
#         self.__grade = grade

#     def set_age(self, age):
#         self.__age = age

#     # Method to display student details
#     def display_details(self):
#         print(f"Student Name: {self.__name}")
#         print(f"Grade: {self.__grade}")
#         print(f"Age: {self.__age}")

# # Example usage
# student = Student("John Doe", "A", 15)
# student.display_details()

# student.set_name("Jane Doe")
# student.set_grade("B")
# student.set_age(16)
# student.display_details()

# 16. Create a class Library with attributes name and books (a list of Book objects). Provide methods 
# to add and remove books.
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book)
#             print(f"Added {book} to the library.")
#         else:
#             print("Only Book objects can be added.")

#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print(f"Removed {book} from the library.")
#         else:
#             print("Book not found in the library.")

#     def display_books(self):
#         if self.books:
#             print(f"Books in {self.name}:")
#             for book in self.books:
#                 print(f" - {book}")
#         else:
#             print("No books in the library.")

# # Example usage
# library = Library("City Library")
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")

# library.add_book(book1)
# library.add_book(book2)
# library.display_books()

# library.remove_book(book1)
# library.display_books()
# 17. Create a class School with attributes name and students (a list of Student objects). Provide 
# methods to add and remove students.
# class Student:
#     def __init__(self, name, grade, age):
#         self.__name = name
#         self.__grade = grade
#         self.__age = age

#     # Getter methods
#     def get_name(self):
#         return self.__name

#     def get_grade(self):
#         return self.__grade

#     def get_age(self):
#         return self.__age

#     # Setter methods
#     def set_name(self, name):
#         self.__name = name

#     def set_grade(self, grade):
#         self.__grade = grade

#     def set_age(self, age):
#         self.__age = age

#     # Method to display student details
#     def display_details(self):
#         print(f"Student Name: {self.__name}")
#         print(f"Grade: {self.__grade}")
#         print(f"Age: {self.__age}")

#     def __str__(self):
#         return f"{self.__name}, Grade: {self.__grade}, Age: {self.__age}"
# class School:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.students.append(student)
#             print(f"Added {student.get_name()} to the school.")
#         else:
#             print("Only Student objects can be added.")

#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
#             print(f"Removed {student.get_name()} from the school.")
#         else:
#             print("Student not found in the school.")

#     def display_students(self):
#         if self.students:
#             print(f"Students in {self.name}:")
#             for student in self.students:
#                 print(f" - {student}")
#         else:
#             print("No students in the school.")

# # Example usage
# school = School("Green Valley High")
# student1 = Student("John Doe", "A", 15)
# student2 = Student("Jane Doe", "B", 16)

# school.add_student(student1)
# school.add_student(student2)
# school.display_students()

# school.remove_student(student1)
# school.display_students()


# 18. Create a class Team with attributes name and members (a list of Person objects). Provide 
# methods to add and remove members.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, Age: {self.age}"
# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.members = []

#     def add_member(self, person):
#         if isinstance(person, Person):
#             self.members.append(person)
#             print(f"Added {person.name} to the team.")
#         else:
#             print("Only Person objects can be added.")

#     def remove_member(self, person):
#         if person in self.members:
#             self.members.remove(person)
#             print(f"Removed {person.name} from the team.")
#         else:
#             print("Person not found in the team.")

#     def display_members(self):
#         if self.members:
#             print(f"Members of {self.name}:")
#             for member in self.members:
#                 print(f" - {member}")
#         else:
#             print("No members in the team.")

# # Example usage
# team = Team("Developers")
# person1 = Person("Alice Smith", 30)
# person2 = Person("Bob Johnson", 25)

# team.add_member(person1)
# team.add_member(person2)
# team.display_members()

# team.remove_member(person1)
# team.display_members()






# 19. Create a class Company with attributes name and employees (a list of Employee objects). 
# Provide methods to add and remove employees.
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def __str__(self):
#         return f"{self.name}, Position: {self.position}"
# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []

#     def add_employee(self, employee):
#         if isinstance(employee, Employee):
#             self.employees.append(employee)
#             print(f"Added {employee.name} to the company.")
#         else:
#             print("Only Employee objects can be added.")

#     def remove_employee(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             print(f"Removed {employee.name} from the company.")
#         else:
#             print("Employee not found in the company.")

#     def display_employees(self):
#         if self.employees:
#             print(f"Employees of {self.name}:")
#             for employee in self.employees:
#                 print(f" - {employee}")
#         else:
#             print("No employees in the company.")

# # Example usage
# company = Company("Tech Innovators")
# employee1 = Employee("Alice Smith", "Software Engineer")
# employee2 = Employee("Bob Johnson", "Data Scientist")

# company.add_employee(employee1)
# company.add_employee(employee2)
# company.display_employees()

# company.remove_employee(employee1)
# company.display_employees()




# 20. Create a class Zoo with attributes name and animals (a list of Animal objects). Provide methods 
# to add and remove animals
# class Animal:
#     def __init__(self, species, name):
#         self.species = species
#         self.name = name

#     def __str__(self):
#         return f"{self.name} ({self.species})"
# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []

#     def add_animal(self, animal):
#         if isinstance(animal, Animal):
#             self.animals.append(animal)
#             print(f"Added {animal.name} to the zoo.")
#         else:
#             print("Only Animal objects can be added.")

#     def remove_animal(self, animal):
#         if animal in self.animals:
#             self.animals.remove(animal)
#             print(f"Removed {animal.name} from the zoo.")
#         else:
#             print("Animal not found in the zoo.")

#     def display_animals(self):
#         if self.animals:
#             print(f"Animals in {self.name}:")
#             for animal in self.animals:
#                 print(f" - {animal}")
#         else:
#             print("No animals in the zoo.")

# # Example usage
# zoo = Zoo("City Zoo")
# animal1 = Animal("Lion", "Leo")
# animal2 = Animal("Elephant", "Dumbo")

# zoo.add_animal(animal1)
# zoo.add_animal(animal2)
# zoo.display_animals()

# zoo.remove_animal(animal1)
# zoo.display_animals()
# File Handling and Exceptions Exercises
# 21. Create a class FileManager with methods to read from and write to a file.
# class FileManager:
#     def __init__(self, filename):
#         self.filename = filename

#     def write_to_file(self, content):
#         try:
#             with open(self.filename, 'w') as file:
#                 file.write(content)
#                 print(f"Successfully wrote to {self.filename}.")
#         except Exception as e:
#             print(f"An error occurred while writing to the file: {e}")

#     def read_from_file(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 content = file.read()
#                 print(f"Successfully read from {self.filename}.")
#                 return content
#         except FileNotFoundError:
#             print(f"The file {self.filename} does not exist.")
#             return None
#         except Exception as e:
#             print(f"An error occurred while reading from the file: {e}")
#             return None

# Example usage
# file_manager = FileManager("example.txt")

# # Writing to the file
# file_manager.write_to_file("Hello, World!")

# # Reading from the file
# content = file_manager.read_from_file()
# if content:
#     print("File content:")
#     print(content)

# 22. Create a class Log with methods to write error messages to a log file.

# class Log:
#     def __init__(self, log_filename):
#         self.log_filename = log_filename

#     def write_error(self, error_message):
#         try:
#             with open(self.log_filename, 'a') as log_file:
#                 log_file.write(f"ERROR: {error_message}\n")
#                 print(f"Successfully wrote error to {self.log_filename}.")
#         except Exception as e:
#             print(f"An error occurred while writing to the log file: {e}")

# # Example usage
# log = Log("error_log.txt")

# # Writing an error message to the log file
# log.write_error("This is an error message.")
# log.write_error("Another error occurred.")



# 23. Create a class Config that reads configuration settings from a file and provides methods to access 
# these settings.
# import json

# class Config:
#     def __init__(self, config_filename):
#         self.config_filename = config_filename
#         self.settings = {}
#         self.load_config()

#     def load_config(self):
#         try:
#             with open(self.config_filename, 'r') as config_file:
#                 self.settings = json.load(config_file)
#                 print(f"Successfully loaded configuration from {self.config_filename}.")
#         except FileNotFoundError:
#             print(f"The file {self.config_filename} does not exist.")
#         except json.JSONDecodeError:
#             print(f"Error decoding JSON from the file {self.config_filename}.")
#         except Exception as e:
#             print(f"An error occurred while loading the configuration: {e}")

#     def get_setting(self, key):
#         return self.settings.get(key, None)

# # Example usage
# config = Config("config.json")

# # Accessing a setting
# database_url = config.get_setting("database_url")
# if database_url:
#     print(f"Database URL: {database_url}")
# else:
#     print("Database URL not found in configuration.")



# 24. Create a class Database that connects to a database and provides methods to execute queries. 
# Handle exceptions if the connection fails.
# import sqlite3

# class Database:
#     def __init__(self, db_filename):
#         self.db_filename = db_filename
#         self.connection = None
#         self.cursor = None
#         self.connect()

#     def connect(self):
#         try:
#             self.connection = sqlite3.connect(self.db_filename)
#             self.cursor = self.connection.cursor()
#             print(f"Successfully connected to the database {self.db_filename}.")
#         except sqlite3.Error as e:
#             print(f"An error occurred while connecting to the database: {e}")

#     def execute_query(self, query, parameters=()):
#         try:
#             self.cursor.execute(query, parameters)
#             self.connection.commit()
#             print("Query executed successfully.")
#         except sqlite3.Error as e:
#             print(f"An error occurred while executing the query: {e}")

#     def fetch_results(self):
#         try:
#             return self.cursor.fetchall()
#         except sqlite3.Error as e:
#             print(f"An error occurred while fetching results: {e}")
#             return None

#     def close(self):
#         if self.connection:
#             self.connection.close()
#             print("Database connection closed.")

# # Example usage
# db = Database("example.db")

# # Create a table
# db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# # Insert a record
# db.execute_query("INSERT INTO users (name) VALUES (?)", ("Alice",))

# # Query the table
# db.execute_query("SELECT * FROM users")
# results = db.fetch_results()
# if results:
#     print("Query results:")
#     for row in results:
#         print(row)

# # Close the connection
# db.close()

# 25. Create a class Report that generates a report from data in a file. Provide methods to handle 
# exceptions if the file does not exist or cannot be read.
# class Report:
#     def __init__(self, data_filename):
#         self.data_filename = data_filename
#         self.data = None
#         self.load_data()

#     def load_data(self):
#         try:
#             with open(self.data_filename, 'r') as file:
#                 self.data = file.read()
#                 print(f"Successfully loaded data from {self.data_filename}.")
#         except FileNotFoundError:
#             print(f"The file {self.data_filename} does not exist.")
#         except IOError as e:
#             print(f"An error occurred while reading the file {self.data_filename}: {e}")

#     def generate_report(self):
#         if self.data is None:
#             print("No data available to generate the report.")
#             return

#         # Example report generation
#         print("Generating report...")
#         # Here you can process the data and create the report as needed
#         print("Report content:")
#         print(self.data)

# # Example usage
# report = Report("data.txt")
# report.generate_report()

# Real-world Application Exercises
# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price. 
# Provide methods to display ticket details and apply discounts.
# class Ticket:
#     def __init__(self, movie_name, seat_number, price):
#         self.movie_name = movie_name
#         self.seat_number = seat_number
#         self.price = price

#     def display_details(self):
#         print(f"Movie Name: {self.movie_name}")
#         print(f"Seat Number: {self.seat_number}")
#         print(f"Price: ${self.price:.2f}")

#     def apply_discount(self, discount_percentage):
#         if 0 <= discount_percentage <= 100:
#             discount_amount = (self.price * discount_percentage) / 100
#             self.price -= discount_amount
#             print(f"Discount applied: {discount_percentage}%")
#             print(f"New Price: ${self.price:.2f}")
#         else:
#             print("Invalid discount percentage. It must be between 0 and 100.")

# # Example usage
# ticket = Ticket("Inception", "A12", 12.00)

# # Display ticket details
# ticket.display_details()

# # Apply a discount
# ticket.apply_discount(10)  # Apply a 10% discount

# # Display updated ticket details
# ticket.display_details()



# 27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should 
# be an object of a class Item with attributes name and price.

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}"
# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         if isinstance(item, Item):
#             self.items.append(item)
#             print(f"Added {item} to the cart.")
#         else:
#             print("Only Item objects can be added.")

#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"Removed {item} from the cart.")
#         else:
#             print("Item not found in the cart.")

#     def display_items(self):
#         if self.items:
#             print("Items in the cart:")
#             for item in self.items:
#                 print(f" - {item}")
#         else:
#             print("The cart is empty.")

# # Example usage
# item1 = Item("Laptop", 999.99)
# item2 = Item("Headphones", 199.99)
# item3 = Item("Mouse", 25.00)

# cart = ShoppingCart()
# cart.add_item(item1)
# cart.add_item(item2)
# cart.add_item(item3)
# cart.display_items()

# cart.remove_item(item2)
# cart.display_items()




# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide 
# methods to add and remove items from the menu.

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}"
# class Restaurant:
#     def __init__(self, name):
#         self.name = name
#         self.menu = []

#     def add_item(self, item):
#         if isinstance(item, Item):
#             self.menu.append(item)
#             print(f"Added {item} to the menu.")
#         else:
#             print("Only Item objects can be added.")

#     def remove_item(self, item):
#         if item in self.menu:
#             self.menu.remove(item)
#             print(f"Removed {item} from the menu.")
#         else:
#             print("Item not found in the menu.")

#     def display_menu(self):
#         if self.menu:
#             print(f"Menu for {self.name}:")
#             for item in self.menu:
#                 print(f" - {item}")
#         else:
#             print("The menu is currently empty.")

# # Example usage
# item1 = Item("Burger", 8.99)
# item2 = Item("Fries", 2.99)
# item3 = Item("Soda", 1.50)

# restaurant = Restaurant("Gourmet Eats")
# restaurant.add_item(item1)
# restaurant.add_item(item2)
# restaurant.add_item(item3)
# restaurant.display_menu()

# restaurant.remove_item(item2)
# restaurant.display_menu()



# 29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person
# objects). Provide methods to add and remove passengers.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, Age: {self.age}"
# class Flight:
#     def __init__(self, flight_number, destination):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.passengers = []

#     def add_passenger(self, person):
#         if isinstance(person, Person):
#             self.passengers.append(person)
#             print(f"Added {person} to flight {self.flight_number}.")
#         else:
#             print("Only Person objects can be added as passengers.")

#     def remove_passenger(self, person):
#         if person in self.passengers:
#             self.passengers.remove(person)
#             print(f"Removed {person} from flight {self.flight_number}.")
#         else:
#             print("Passenger not found on the flight.")

#     def display_passengers(self):
#         if self.passengers:
#             print(f"Passengers on flight {self.flight_number} to {self.destination}:")
#             for passenger in self.passengers:
#                 print(f" - {passenger}")
#         else:
#             print("No passengers on this flight.")

# # Example usage
# person1 = Person("Alice Smith", 30)
# person2 = Person("Bob Johnson", 25)
# person3 = Person("Charlie Brown", 40)

# flight = Flight("AA123", "New York")
# flight.add_passenger(person1)
# flight.add_passenger(person2)
# flight.add_passenger(person3)
# flight.display_passengers()

# flight.remove_passenger(person2)
# flight.display_passengers()



# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and checkout rooms.
# class Room:
#     def __init__(self, room_number):
#         self.room_number = room_number
#         self.is_occupied = False

#     def __str__(self):
#         status = "Occupied" if self.is_occupied else "Available"
#         return f"Room {self.room_number}: {status}"
# class Hotel:
#     def __init__(self, name):
#         self.name = name
    #     self.rooms = []

    # def add_room(self, room):
    #     if isinstance(room, Room):
    #         self.rooms.append(room)
    #         print(f"Added {room} to the hotel.")
    #     else:
    #         print("Only Room objects can be added.")

    # def book_room(self, room_number):
    #     room = self.find_room(room_number)
    #     if room:
    #         if not room.is_occupied:
    #             room.is_occupied = True
    #             print(f"Room {room_number} has been booked.")
    #         else:
    #             print(f"Room {room_number} is already occupied.")
    #     else:
    #         print(f"Room {room_number} does not exist.")

    # def check_out_room(self, room_number):
    #     room = self.find_room(room_number)
    #     if room:
    #         if room.is_occupied:
    #             room.is_occupied = False
    #             print(f"Room {room_number} is now available.")
    #         else:
    #             print(f"Room {room_number} is already available.")
    #     else:
    #         print(f"Room {room_number} does not exist.")

#     def find_room(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 return room
#         return None

#     def display_rooms(self):
#         if self.rooms:
#             print(f"Rooms in {self.name}:")
#             for room in self.rooms:
#                 print(f" - {room}")
#         else:
#             print("No rooms in the hotel.")

# # Example usage
# hotel = Hotel("Grand Hotel")
# room1 = Room(101)
# room2 = Room(102)
# room3 = Room(103)

# hotel.add_room(room1)
# hotel.add_room(room2)
# hotel.add_room(room3)
# hotel.display_rooms()

# hotel.book_room(101)
# hotel.book_room(102)
# hotel.display_rooms()

# hotel.check_out_room(101)
# hotel.display_rooms()



# GUI Application Exercises
# 36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and 
# decrement buttons.
# import tkinter as tk

# class CounterApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Counter App")
        
#         # Initialize counter value
#         self.counter = 0
        
#         # Create and place widgets
#         self.counter_label = tk.Label(root, text=str(self.counter), font=('Helvetica', 48))
#         self.counter_label.pack(pady=20)
        
#         self.increment_button = tk.Button(root, text="Increment", command=self.increment_counter)
#         self.increment_button.pack(side=tk.LEFT, padx=20)
        
#         self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement_counter)
#         self.decrement_button.pack(side=tk.RIGHT, padx=20)
    
#     def increment_counter(self):
#         self.counter += 1
#         self.update_label()
    
#     def decrement_counter(self):
#         self.counter -= 1
#         self.update_label()
    
#     def update_label(self):
#         self.counter_label.config(text=str(self.counter))

# # Create the main window
# root = tk.Tk()

# # Initialize the CounterApp
# app = CounterApp(root)

# # Run the application
# root.mainloop()
# 37. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and 
# remove tasks.

# import tkinter as tk
# from tkinter import messagebox

# class ToDoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List App")
        
#         # Create and place widgets
#         self.task_entry = tk.Entry(root, width=50)
#         self.task_entry.pack(pady=10)
        
#         self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
#         self.add_button.pack(pady=5)
        
#         self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
#         self.task_listbox.pack(pady=10)
        
#         self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
#         self.remove_button.pack(pady=5)
    
#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.task_listbox.insert(tk.END, task)
#             self.task_entry.delete(0, tk.END)
#         else:
#             messagebox.showwarning("Warning", "You must enter a task.")
    
#     def remove_task(self):
#         try:
#             selected_index = self.task_listbox.curselection()[0]
#             self.task_listbox.delete(selected_index)
#         except IndexError:
#             messagebox.showwarning("Warning", "You must select a task to remove.")

# # Create the main window
# root = tk.Tk()

# # Initialize the ToDoApp
# app = ToDoApp(root)

# # Run the application
# root.mainloop()

# 38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.

# import tkinter as tk

# class CalculatorApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Simple Calculator")
        
#         # Initialize the calculator state
#         self.current_input = ""
#         self.result_var = tk.StringVar()
        
#         # Create and place widgets
#         self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 24), bd=10, relief=tk.SUNKEN, justify='right')
#         self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # buttons = [
        #     '7', '8', '9', '/',
        #     '4', '5', '6', '*',
        #     '1', '2', '3', '-',
        #     '0', '.', '=', '+'
        # ]
        
        # # Create and place buttons
        # row = 1
        # col = 0
        # for button in buttons:
        #     tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
        #     col += 1
        #     if col > 3:
    #             col = 0
    #             row += 1
    
    # def on_button_click(self, button):
    #     if button in '0123456789.':
    #         self.current_input += button
    #         self.result_var.set(self.current_input)
    #     elif button in '+-*/':
    #         self.current_input += f' {button} '
    #         self.result_var.set(self.current_input)
    #     elif button == '=':
    #         try:
    #             # Evaluate the expression and display the result
    #             expression = self.current_input
    #             result = eval(expression)
                # self.result_var.set(result)
#                 self.current_input = str(result)
#             except Exception as e:
#                 self.result_var.set("Error")
#                 self.current_input = ""
#         else:
#             self.current_input = ""
#             self.result_var.set("")

# # Create the main window
# root = tk.Tk()

# # Initialize the CalculatorApp
# app = CalculatorApp(root)

# # Run the application
# root.mainloop()


# 39. Create a class LoginApp that uses tkinter to create a login form GUI.

# import tkinter as tk
# from tkinter import messagebox

# class LoginApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Login Form")
        
#         # Create and place widgets
#         self.username_label = tk.Label(root, text="Username:")
#         self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        
#         self.username_entry = tk.Entry(root)
#         self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        
#         self.password_label = tk.Label(root, text="Password:")
#         self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        
#         self.password_entry = tk.Entry(root, show='*')
#         self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
#         self.login_button = tk.Button(root, text="Login", command=self.login)
#         self.login_button.grid(row=2, column=0, columnspan=2, pady=20)
    
#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
        
#         # Placeholder logic for authentication
#         if username == "admin" and password == "password":
#             messagebox.showinfo("Login Success", "Welcome, Admin!")
#         else:
#             messagebox.showerror("Login Failed", "Invalid username or password.")

# # Create the main window
# root = tk.Tk()

# # Initialize the LoginApp
# app = LoginApp(root)

# # Run the application
# root.mainloop()







# 40. Create a class WeatherApp that uses tkinter to create a weather information GUI.

# import tkinter as tk
# from tkinter import messagebox

# class WeatherApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Weather Information")
        
#         # Create and place widgets
#         self.city_label = tk.Label(root, text="Enter City:")
#         self.city_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        
#         self.city_entry = tk.Entry(root)
#         self.city_entry.grid(row=0, column=1, padx=10, pady=10)
        
#         self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
#         self.get_weather_button.grid(row=1, column=0, columnspan=2, pady=20)
        
#         self.weather_info_label = tk.Label(root, text="", font=('Helvetica', 16))
#         self.weather_info_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
#     def get_weather(self):
#         city = self.city_entry.get()
        
#         if city:
#             # Placeholder weather information
#             # In a real application, replace this with actual weather data from an API
#             weather_info = f"Weather in {city}:\nTemperature: 25°C\nCondition: Sunny"
#             self.weather_info_label.config(text=weather_info)
#         else:
#             messagebox.showwarning("Input Error", "Please enter a city name.")

# # Create the main window
# root = tk.Tk()

# # Initialize the WeatherApp
# app = WeatherApp(root)

# # Run the application
# root.mainloop()


# Create and place widgets

   

            
            


    

   

    




























