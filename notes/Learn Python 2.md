### Step 11: More on Data Structures

#### Lists
1. **List Operations**:
    ```python
    numbers = [1, 2, 3, 4, 5]
    print(numbers[1:3])  # Slicing
    numbers.append(6)
    print(numbers)
    numbers.remove(3)
    print(numbers)
    numbers.reverse()
    print(numbers)
    ```

2. **List Comprehensions**:
    ```python
    squares = [x ** 2 for x in range(10)]
    print(squares)
    ```

#### Dictionaries
1. **Dictionary Operations**:
    ```python
    person = {"name": "Alice", "age": 25}
    person["age"] = 26
    print(person)
    del person["age"]
    print(person)
    ```

2. **Dictionary Comprehensions**:
    ```python
    square_dict = {x: x ** 2 for x in range(10)}
    print(square_dict)
    ```

### Step 12: Advanced Functions

#### Lambda Functions
1. **Using Lambda Functions**:
    ```python
    add = lambda x, y: x + y
    print(add(2, 3))
    ```

2. **Lambda with Map, Filter, and Reduce**:
    ```python
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    # Map
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)

    # Filter
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(even)

    # Reduce
    sum_all = reduce(lambda x, y: x + y, numbers)
    print(sum_all)
    ```

### Step 13: File Handling in Depth

1. **Reading and Writing JSON Files**:
    ```python
    import json

    # Writing JSON to a file
    data = {"name": "Alice", "age": 25}
    with open('data.json', 'w') as file:
        json.dump(data, file)

    # Reading JSON from a file
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    ```

2. **CSV Files**:
    ```python
    import csv

    # Writing to a CSV file
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", 25])
        writer.writerow(["Bob", 30])

    # Reading from a CSV file
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    ```

### Step 14: Object-Oriented Programming (OOP)

1. **Inheritance**:
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    dog = Dog("Rex")
    cat = Cat("Whiskers")

    print(dog.speak())
    print(cat.speak())
    ```

2. **Polymorphism**:
    ```python
    class Bird(Animal):
        def speak(self):
            return "Tweet!"

    animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]
    for animal in animals:
        print(f"{animal.name} says {animal.speak()}")
    ```

### Step 15: Error Handling in Depth

1. **Custom Exceptions**:
    ```python
    class CustomError(Exception):
        pass

    def risky_function():
        raise CustomError("Something went wrong!")

    try:
        risky_function()
    except CustomError as e:
        print(e)
    ```

### Step 16: Working with External Libraries

1. **Requests Library**:
    ```python
    import requests

    response = requests.get('https://api.github.com')
    print(response.status_code)
    print(response.json())
    ```

2. **Pandas for Data Analysis**:
    ```python
    import pandas as pd

    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    }
    df = pd.DataFrame(data)
    print(df)
    ```

### Step 17: Introduction to Web Development with Flask

1. **Simple Flask App**:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)
    ```

### Step 18: Introduction to Testing in Python

1. **Unit Testing with unittest**:
    ```python
    import unittest

    def add(a, b):
        return a + b

    class TestMathFunctions(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)

    if __name__ == "__main__":
        unittest.main()
    ```

---

