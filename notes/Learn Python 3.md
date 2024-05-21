### Step 19: Working with APIs

1. **Using the `requests` Library**:
    ```python
    import requests

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n")
    else:
        print("Failed to retrieve posts")
    ```

2. **Making POST Requests**:
    ```python
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print("Post created successfully")
    else:
        print("Failed to create post")
    ```

### Step 20: Advanced Data Structures

1. **Collections Module**:
    ```python
    from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

    # Namedtuple
    Point = namedtuple('Point', 'x y')
    pt = Point(1, 2)
    print(pt.x, pt.y)

    # Deque
    d = deque([1, 2, 3])
    d.append(4)
    d.appendleft(0)
    print(d)

    # Counter
    cnt = Counter('hello world')
    print(cnt)

    # OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    print(od)

    # Defaultdict
    dd = defaultdict(int)
    dd['a'] += 1
    print(dd)
    ```

### Step 21: Multithreading and Multiprocessing

1. **Multithreading with `threading` Module**:
    ```python
    import threading

    def print_numbers():
        for i in range(1, 6):
            print(i)

    def print_letters():
        for letter in 'abcde':
            print(letter)

    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Threads have finished execution")
    ```

2. **Multiprocessing with `multiprocessing` Module**:
    ```python
    from multiprocessing import Process, Queue

    def square_numbers(numbers, queue):
        for n in numbers:
            queue.put(n * n)

    if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5]
        q = Queue()
        p = Process(target=square_numbers, args=(numbers, q))
        p.start()
        p.join()

        while not q.empty():
            print(q.get())
    ```

### Step 22: Asynchronous Programming

1. **Asyncio Basics**:
    ```python
    import asyncio

    async def say_hello():
        print("Hello")
        await asyncio.sleep(1)
        print("World")

    async def main():
        await asyncio.gather(say_hello(), say_hello())

    asyncio.run(main())
    ```

2. **Asynchronous HTTP Requests**:
    ```python
    import aiohttp
    import asyncio

    async def fetch(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def main():
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        content = await fetch(url)
        print(content)

    asyncio.run(main())
    ```

### Step 23: Context Managers and Generators

1. **Custom Context Managers**:
    ```python
    class FileManager:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()

    with FileManager('test.txt', 'w') as f:
        f.write("Hello, World!")
    ```

2. **Advanced Generators**:
    ```python
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    for number in countdown(5):
        print(number)
    ```

### Step 24: Decorators in Depth

1. **Function Decorators**:
    ```python
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper

    @my_decorator
    def say_hello(name):
        print(f"Hello, {name}!")

    say_hello("Alice")
    ```

2. **Class Decorators**:
    ```python
    class ClassDecorator:
        def __init__(self, cls):
            self.cls = cls

        def __call__(self, *args, **kwargs):
            instance = self.cls(*args, **kwargs)
            instance.say_hello = self.say_hello_override
            return instance

        def say_hello_override(self):
            print("Hello from the decorated class!")

    @ClassDecorator
    class MyClass:
        def say_hello(self):
            print("Hello from MyClass!")

    obj = MyClass()
    obj.say_hello()
    ```

### Step 25: Working with Databases

1. **SQLite**:
    ```python
    import sqlite3

    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")

    connection.commit()

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    connection.close()
    ```

2. **Using SQLAlchemy**:
    ```python
    from sqlalchemy import create_engine, Column, Integer, String, Sequence
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
        name = Column(String(50))
        age = Column(Integer)

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([User(name='Alice', age=25), User(name='Bob', age=30)])
    session.commit()

    for user in session.query(User).all():
        print(user.name, user.age)
    ```

---