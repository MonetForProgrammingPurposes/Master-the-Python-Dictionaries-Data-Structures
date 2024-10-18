# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Print the dictionary
print(person)

# Accessing the 'name' value
print(person["name"])  # Output: Alice

# Accessing the 'age' value
print(person["age"])  # Output: 25

print(person.get("name"))
print(person.get("country", "Not Found"))

# Update dictionary values
person["age"] = 26
print(person["age"])

# Add new key-value pair
person["email"] = "alice@example.com"
print(person)

# Remove 'age' and 'city'
age = person.pop("age")
print(age)
del person["city"]
print(person)

# Check if 'name' exists in the dictionary
if "name" in person:
    print("Key 'name' exists in the dictionary")

# Iterating over dictionary keys
for key in person:
    print(key)  # I-print ang bawat key

# Iterating over dictionary values
for value in person.values():
    print(value)  # I-print ang bawat value

# Iterating over key-value pairs
for key, value in person.items():
    print(key, value)  # I-print ang bawat key kasama ang value

# Example of word count using dictionary
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Fibonacci with memoization using dictionary
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result

print(fibonacci(10))  # Output: 55

# Nested dictionary example
school = {
    "students": {
        1: {"name": "Alice", "grade": "A"},
        2: {"name": "Bob", "grade": "B"}
    },
    "teachers": {
        101: {"name": "Mr. Smith", "subject": "Math"},
        102: {"name": "Ms. Johnson", "subject": "English"}
    }
}

print(school["students"][1]["name"])

# JSON example
import json

# Example JSON data (as a string)
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

# Convert JSON to dictionary
data = json.loads(json_data)
print(data["name"])

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)

# Using pipe operator for merging dictionaries
merged_dict = dict1 | dict2
print(merged_dict)

# Sorting a dictionary by keys
sorted_by_keys = dict(sorted(person.items()))
print(sorted_by_keys)

# Sorting by values (strings only)
sorted_by_values = dict(sorted(person.items(), key=lambda item: str(item[1])))
print(sorted_by_values)
