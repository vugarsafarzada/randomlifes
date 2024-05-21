### 1. Classes and Objects

**Class**: A blueprint for creating objects (a particular data structure).
**Object**: An instance of a class.

#### Example: Creating a Simple Class and Object
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an object (instance) of the class
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!
```

### 2. Inheritance

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

#### Example: Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden in the child classes

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())  # Output: Buddy says woof!
print(cat.speak())  # Output: Kitty says meow!
```

### 3. Polymorphism

Polymorphism allows methods to do different things based on the object it is acting upon.

#### Example: Polymorphism
```python
class Bird(Animal):
    def speak(self):
        return f"{self.name} says tweet!"

animals = [Dog("Buddy"), Cat("Kitty"), Bird("Tweety")]

for animal in animals:
    print(animal.speak())
# Output:
# Buddy says woof!
# Kitty says meow!
# Tweety says tweet!
```

### 4. Encapsulation

Encapsulation restricts access to some of the object's components, which can prevent the accidental modification of data.

#### Example: Encapsulation
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

p = Person("Alice", 30)
print(p.get_age())  # Output: 30
p.set_age(35)
print(p.get_age())  # Output: 35
p.set_age(-5)       # Output: Age must be positive!
```

### 5. Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object.

#### Example: Abstraction with Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 20)
print(f"Area: {rect.area()}")        # Output: Area: 200
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 60
```

### Practice Exercise

1. **Create a Class and Objects**:
    - Define a class `Car` with attributes `make`, `model`, and `year`.
    - Add a method `description` that prints the car details.
    - Create two objects of the `Car` class and print their descriptions.

2. **Implement Inheritance**:
    - Define a parent class `Shape` with an abstract method `area`.
    - Create two child classes `Square` and `Circle` that implement the `area` method.
    - Instantiate objects of `Square` and `Circle` and print their areas.

3. **Encapsulation Practice**:
    - Define a class `BankAccount` with a private attribute `balance`.
    - Add methods to get and set the balance, ensuring the balance cannot be set to a negative value.
    - Test the class by creating an account and modifying the balance.

### Example Solutions

1. **Create a Class and Objects**:
    ```python
    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

        def description(self):
            print(f"{self.year} {self.make} {self.model}")

    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic", 2018)

    car1.description()  # Output: 2020 Toyota Corolla
    car2.description()  # Output: 2018 Honda Civic
    ```

2. **Implement Inheritance**:
    ```python
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side ** 2

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    square = Square(4)
    circle = Circle(3)

    print(f"Square Area: {square.area()}")  # Output: Square Area: 16
    print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 28.26
    ```

3. **Encapsulation Practice**:
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount!")

# Test the BankAccount class
account = BankAccount(100)
print(f"Initial balance: ${account.get_balance()}")  # Output: Initial balance: $100

account.deposit(50)
print(f"Balance after deposit: ${account.get_balance()}")  # Output: Balance after deposit: $150

account.withdraw(30)
print(f"Balance after withdrawal: ${account.get_balance()}")  # Output: Balance after withdrawal: $120

account.set_balance(200)
print(f"Balance after setting new balance: ${account.get_balance()}")  # Output: Balance after setting new balance: $200

account.set_balance(-50)  # Output: Balance cannot be negative!
```

### Additional OOP Concepts

#### 6. Class Methods and Static Methods

1. **Class Methods**:
   Class methods are methods that are bound to the class and not the instance of the class. They can modify the class state that applies across all instances of the class.
   ```python
   class MyClass:
       class_variable = 0

       def __init__(self, instance_variable):
           self.instance_variable = instance_variable

       @classmethod
       def increment_class_variable(cls):
           cls.class_variable += 1

   # Test class method
   MyClass.increment_class_variable()
   print(MyClass.class_variable)  # Output: 1
   ```

2. **Static Methods**:
   Static methods are methods that are bound to the class and not the instance of the class. They do not modify the class state or instance state and are utility functions within the class.
   ```python
   class MathOperations:
       @staticmethod
       def add(x, y):
           return x + y

   # Test static method
   result = MathOperations.add(5, 3)
   print(result)  # Output: 8
   ```

#### 7. Property Decorators (Getters and Setters)

Property decorators are used to manage the access to instance variables.

1. **Using Property Decorators**:
   ```python
   class Person:
       def __init__(self, name):
           self._name = name

       @property
       def name(self):
           return self._name

       @name.setter
       def name(self, value):
           if value:
               self._name = value
           else:
               print("Name cannot be empty!")

   # Test property decorators
   p = Person("Alice")
   print(p.name)  # Output: Alice

   p.name = "Bob"
   print(p.name)  # Output: Bob

   p.name = ""  # Output: Name cannot be empty!
   ```

### Practice Exercise 2

1. **Create a class `Library` with methods to add books, remove books, and display books. Implement this class and test it by adding, removing, and displaying books.**

2. **Create a class hierarchy with a base class `Employee` and derived classes `Manager` and `Developer`. Add relevant attributes and methods to each class, including a method to display the details of the employee.**

### Example Solutions

1. **Library Class**:
   ```python
   class Library:
       def __init__(self):
           self.books = []

       def add_book(self, book):
           self.books.append(book)

       def remove_book(self, book):
           if book in self.books:
               self.books.remove(book)
           else:
               print("Book not found!")

       def display_books(self):
           if self.books:
               print("Books in the library:")
               for book in self.books:
                   print(book)
           else:
               print("No books in the library!")

   # Test the Library class
   library = Library()
   library.add_book("To Kill a Mockingbird")
   library.add_book("1984")
   library.display_books()
   # Output:
   # Books in the library:
   # To Kill a Mockingbird
   # 1984

   library.remove_book("1984")
   library.display_books()
   # Output:
   # Books in the library:
   # To Kill a Mockingbird
   ```

2. **Employee Class Hierarchy**:
   ```python
   class Employee:
       def __init__(self, name, salary):
           self.name = name
           self.salary = salary

       def display_details(self):
           print(f"Name: {self.name}, Salary: ${self.salary}")

   class Manager(Employee):
       def __init__(self, name, salary, department):
           super().__init__(name, salary)
           self.department = department

       def display_details(self):
           super().display_details()
           print(f"Department: {self.department}")

   class Developer(Employee):
       def __init__(self, name, salary, programming_language):
           super().__init__(name, salary)
           self.programming_language = programming_language

       def display_details(self):
           super().display_details()
           print(f"Programming Language: {self.programming_language}")

   # Test the Employee class hierarchy
   manager = Manager("Alice", 90000, "HR")
   developer = Developer("Bob", 80000, "Python")

   manager.display_details()
   # Output:
   # Name: Alice, Salary: $90000
   # Department: HR

   developer.display_details()
   # Output:
   # Name: Bob, Salary: $80000
   # Programming Language: Python
   ```

---

The `@overload` decorator in Python is part of the `typing` module and is used to indicate function or method overloading for static type checking. Overloading allows you to define multiple versions of a function with different parameter types or numbers of parameters.

However, unlike languages like C++ or Java, Python does not support function overloading at runtime. Instead, the `@overload` decorator is used to provide type hints for static type checkers like `mypy`, but it does not affect the actual runtime behavior of the function. The runtime behavior must be implemented manually to handle different types or numbers of parameters.

Here’s how you can use `@overload`:

### Example of @overload

1. **Importing Required Modules**:
    ```python
    from typing import overload
    ```

2. **Using @overload**:
    ```python
    from typing import overload, Union

    class MathOperations:
        @overload
        def add(self, x: int, y: int) -> int:
            ...

        @overload
        def add(self, x: float, y: float) -> float:
            ...

        def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
            return x + y

    math_ops = MathOperations()
    print(math_ops.add(5, 3))         # Output: 8
    print(math_ops.add(5.5, 3.2))     # Output: 8.7
    ```

### Explanation:

1. **Importing `overload` and `Union` from `typing`**:
    ```python
    from typing import overload, Union
    ```

2. **Defining Overloaded Methods**:
    ```python
    class MathOperations:
        @overload
        def add(self, x: int, y: int) -> int:
            ...

        @overload
        def add(self, x: float, y: float) -> float:
            ...

        def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
            return x + y
    ```

   - **@overload Decorators**: These indicate to static type checkers that `add` can be called with either two integers or two floats.
   - **Union Type**: `Union[int, float]` indicates that the parameters can be either `int` or `float`, and the return type will match the parameter types.

3. **Runtime Implementation**:
    ```python
    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        return x + y
    ```

   - This method handles both cases at runtime. Python’s dynamic nature allows this single method to handle different types seamlessly.

### More Complex Example with Overloading

Consider a more complex example with different numbers of parameters:

```python
from typing import overload, Union

class Converter:
    @overload
    def convert(self, value: int) -> str:
        ...

    @overload
    def convert(self, value: float, precision: int) -> str:
        ...

    def convert(self, value: Union[int, float], precision: int = 2) -> str:
        if isinstance(value, int):
            return str(value)
        elif isinstance(value, float):
            return f"{value:.{precision}f}"
        else:
            raise TypeError("Unsupported type")

converter = Converter()
print(converter.convert(10))             # Output: "10"
print(converter.convert(3.14159, 3))     # Output: "3.142"
```

### Explanation:

1. **Overloaded Methods**:
    ```python
    @overload
    def convert(self, value: int) -> str:
        ...

    @overload
    def convert(self, value: float, precision: int) -> str:
        ...
    ```

   - The first overload indicates `convert` can take an `int` and return a `str`.
   - The second overload indicates `convert` can take a `float` and an `int` (precision) and return a `str`.

2. **Runtime Implementation**:
    ```python
    def convert(self, value: Union[int, float], precision: int = 2) -> str:
        if isinstance(value, int):
            return str(value)
        elif isinstance(value, float):
            return f"{value:.{precision}f}"
        else:
            raise TypeError("Unsupported type")
    ```

   - This method handles both cases: converting an integer to a string and converting a float to a string with specified precision.

3. **Creating and Using the Converter Object**:
    ```python
    converter = Converter()
    print(converter.convert(10))             # Output: "10"
    print(converter.convert(3.14159, 3))     # Output: "3.142"
    ```

### Key Points:

- `@overload` is used for static type checking, not runtime behavior.
- The actual method implementation must handle all the different types or numbers of parameters.
- `Union` and `Optional` from the `typing` module can be used to specify multiple types for parameters and return types.

Using `@overload` effectively helps improve the readability and maintainability of your code by providing clear type hints, which can be checked by tools like `mypy`.