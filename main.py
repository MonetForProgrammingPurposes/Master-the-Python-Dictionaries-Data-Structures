# --Define the Classes
# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Employee class
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

# Books class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# University class
class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Restaurant class
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


# --Create and Populate Dictionaries

# Create a list of Product objects
products = [
    Product("Laptop", 1200),
    Product("Smartphone", 800),
    Product("Tablet", 400),
    Product("Headphones", 150),
    Product("Smartwatch", 250),
]

# Create a list of Employee objects
employees = [
    Employee("Alice", "Manager"),
    Employee("Bob", "Developer"),
    Employee("Charlie", "Designer"),
    Employee("Diana", "HR"),
    Employee("Eve", "Sales"),
]

# Create a list of Book objects
books = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
    Book("Moby Dick", "Herman Melville"),
    Book("War and Peace", "Leo Tolstoy"),
]

# Create a list of University objects
universities = [
    University("Harvard University", "Cambridge, MA"),
    University("Stanford University", "Stanford, CA"),
    University("MIT", "Cambridge, MA"),
    University("Oxford University", "Oxford, UK"),
    University("Cambridge University", "Cambridge, UK"),
]

# Create a list of Restaurant objects
restaurants = [
    Restaurant("Italian Bistro", "Italian"),
    Restaurant("Sushi Place", "Japanese"),
    Restaurant("Burger Joint", "American"),
    Restaurant("Curry House", "Indian"),
    Restaurant("Taco Stand", "Mexican"),
]


#  --Access and Print the Details

def print_products(products):
    print("Products:")
    for product in products:
        print(f"Name: {product.name}, Price: ${product.price}")

def print_employees(employees):
    print("\nEmployees:")
    for employee in employees:
        print(f"Name: {employee.name}, Job Title: {employee.job_title}")

def print_books(books):
    print("\nBooks:")
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}")

def print_universities(universities):
    print("\nUniversities:")
    for university in universities:
        print(f"Name: {university.name}, Location: {university.location}")

def print_restaurants(restaurants):
    print("\nRestaurants:")
    for restaurant in restaurants:
        print(f"Name: {restaurant.name}, Cuisine Type: {restaurant.cuisine_type}")

# Call the functions to print details
print_products(products)
print_employees(employees)
print_books(books)
print_universities(universities)
print_restaurants(restaurants)
