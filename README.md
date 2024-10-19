1: Define the Classes
First, I created a Python file called main.py and defined several classes to help organize my data. Here’s what I came up with:


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
2: Create and Populate Dictionaries
Next, I created lists to hold instances of these classes. This is how I organized the data:




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
3: Access and Print the Details
Then, I wrote some functions to print out the details of each class. Here’s how I did it:


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
4: Git Commit
Navigate to your project directory using cd


 cd C:\Users\Monet\Master the Python Dictionaries Data Structures
Initialize Git:


 git init
Add remote: Create first a new repository on you GitHub then copy your repository link.


 git remote add origin https://github.com/MonetForProgrammingPurposes/MasterPythonDictionaries.git
Add and commit:


 git add main.py
 git commit -m "Initial commit"
Push to GitHub:



git push -u origin master


5: Running the Code
To run the program, open your terminal using python “name of your file (.py)“


python main.py
This will execute the code and display the details of products, employees, books, universities, and restaurants.

Output:

Products:
Name: Laptop, Price: $1200
Name: Smartphone, Price: $800
Name: Tablet, Price: $400
Name: Headphones, Price: $150
Name: Smartwatch, Price: $250

Employees:
Name: Alice, Job Title: Manager
Name: Bob, Job Title: Developer
Name: Charlie, Job Title: Designer
Name: Diana, Job Title: HR
Name: Eve, Job Title: Sales

Books:
Title: 1984, Author: George Orwell
Title: To Kill a Mockingbird, Author: Harper Lee
Title: The Great Gatsby, Author: F. Scott Fitzgerald
Title: Moby Dick, Author: Herman Melville
Title: War and Peace, Author: Leo Tolstoy

Universities:
Name: Harvard University, Location: Cambridge, MA
Name: Stanford University, Location: Stanford, CA
Name: MIT, Location: Cambridge, MA
Name: Oxford University, Location: Oxford, UK
Name: Cambridge University, Location: Cambridge, UK

Restaurants:
Name: Italian Bistro, Cuisine Type: Italian
Name: Sushi Place, Cuisine Type: Japanese
Name: Burger Joint, Cuisine Type: American
Name: Curry House, Cuisine Type: Indian
Name: Taco Stand, Cuisine Type: Mexican
