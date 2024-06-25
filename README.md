
## Pytest-Tutorial-How-to-Test-Python-Code

https://www.youtube.com/watch?v=cHYq1MRoyI0 

https://raw.githubusercontent.com/RodrigoMvs123/Pytest-Tutorial-How-to-Test-Python-Code/main/README.md

https://github.com/RodrigoMvs123/Pytest-Tutorial-How-to-Test-Python-Code/blame/main/README.md

## What is Pytest ?
```
Testing framework for Python
Auto-discovery of tests
Rich assertion introspection 
Support parameterized and fixture-based testing
```

### Visual Studio Code
Terminal
```bash
python3 -m venv .venv
pip install pytest
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

my_functions.py
def add(number_one, number_two):
    return number_one + number_two

def divide(number_one, number_two):
    return number_one / number_two
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    pass
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

## Source Code
```pythonVisual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one:10, number_two:0)
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

my_functions.py
def add(number_one, number_two):
    return number_one + number_two

def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError
    return number_one / number_two
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
tests
test_my_functions.py
venv

test_my_functions.py
import pytest 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_add_strings():
    result = my_functions.add(number_one:"I like ", number_two:"burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_my_functions.py
```

Class Based Tests

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
test_my_functions.py
venv

shapes.py
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return 2 * math.pi * self.radius
```

```python

Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

test_circle.py
import pytest
import source.shapes as shapes 

class TestCicle():

    def test_one(self):
        assert True
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_circle.py 
cd tests/
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

test_circle.py
import pytest
import source.shapes as shapes 

class TestCircle():

    def setup_method(self, method):
        print(f"Setting up {method}")

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_one(self):
        assert True
```

### Visual Studio Code
Terminal
```bash
pytest test_circle.py 
pytest -s
```

## Source Code
Terminal
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

test_circle.py
import pytest
import source.shapes as shapes 

class TestCircle():

    def setup_method(self, method):
        print(f"Setting up {method}")

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_two(self):
        assert True
```

### Visual Studio Code
Terminal
```bash 
pytest -s
```

## Source Code
Terminal
```bash
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

test_circle.py
import pytest
import source.shapes as shapes 
import math

class TestCircle():

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_two(self):
        assert True
```

### Visual Studio Code
Terminal
```bash 
pytest test_circle.py
pytest test_circle.py -s
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

test_circle.py
import pytest
import source.shapes as shapes 
import math

class TestCircle():

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected 
```

### Visual Studio Code
Terminal
```bash 
pytest test_circle.py -s
```

Fixtures 

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
venv

shapes.py
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length 
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_rectangle.py
import pytest_
import source.shapes as shapes 

def test_area():
    rectangle = shapes.Rectangle(length:10, width:20)
    assert rectangle.area() == 10 * 20
```

### Visual Studio Code
Terminal
```bash 
pytest test_rectangle.py
```

## Source Code
Terminal
```bash
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_rectangle.py
import pytest_
import source.shapes as shapes 

def test_area():
    rectangle = shapes.Rectangle(length:10, width:20)
    assert rectangle.area() == 10 * 20

def test_perimeter():
    rectangle = shapes.Rectangle(length:10, width:20)
    assert rectangle.perimeter() == (10 * 2) + (20 * 2)
```

### Visual Studio Code
Terminal
```bash 
pytest test_rectangle.py
```

## Source Code
```python 
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_rectangle.py
import pytest_
import source.shapes as shapes 

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length:10, width: 20)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)
```

### Visual Studio Code
Terminal
```bash 
pytest test_rectangle.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

shapes.py
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        return self.width == other.width and self.length == other.length
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_rectangle.py
import pytest_
import source.shapes as shapes 

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length:10, width: 20)

@paytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length:5, width:6)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
```

### Visual Studio Code
Terminal
```bash 
pytest test_rectangle.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
conftest.py
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

conftest.py
import pytest_
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length:10, width: 20)

@paytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length:5, width:6)
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_rectangle.py
import pytest_
import source.shapes as shapes 

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
```

### Visual Studio Code
Terminal
```bash 
pytest test_rectangle.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_circle.py
import pytest
import source.shapes as shapes 
import math

class TestCircle():

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected 

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area() 
```

### Visual Studio Code
Terminal
```bash 
pytest test_circle.py
```

Parametrize and Mark 

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_my_functions.py
import pytest 
import time 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_add_strings():
    result = my_functions.add(number_one:"I like ", number_two:"burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)

def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one:10, number_two:5)
     assert result == 2
```

### Visual Studio Code
Terminal
```bash
pytest test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_my_functions.py
import pytest 
import time 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_add_strings():
    result = my_functions.add(number_one:"I like ", number_two:"burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one:10, number_two:5)
     assert result == 2
```

### Visual Studio Code
Terminal
```bash
pytest -m slow
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_my_functions.py
import pytest 
import time 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_add_strings():
    result = my_functions.add(number_one:"I like ", number_two:"burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(number_one:1, number_two:2) == 3
```

### Visual Studio Code
Terminal
```bash
pytest test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

test_my_functions.py
import pytest 
import time 
import source.my_functions as my_functions 

def test_add():
    result = my_functions.add(number_one:1, number_two:4)
    assert result == 5 

def test_add_strings():
    result = my_functions.add(number_one:"I like ", number_two:"burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one:10, number_two:0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(number_one:10, number_two:5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(number_one:1, number_two:2) == 3

@pytest.mark.xfail(reason="We know we can not divide by zero")
def test_divide_zero_broken():
    my_functions.divide(number_one:4, number_two:0)
```

### Visual Studio Code
Terminal
```bash
pytest test_my_functions.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
venv

shapes.py
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        return self.width == other.width and self.length == other.length
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length):
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_square.py
venv

test_square.py
import pytest
import source.shapes as shapes 

@pytest.mark.paramatrize("side_length, expected_area" [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shape.Square(side_length).area() == expected_area
```

### Visual Studio Code
Terminal
```bash
pytest test_square.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_square.py
venv

test_square.py
import pytest
import source.shapes as shapes 

@pytest.mark.paramatrize("side_length, expected_area" [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shape.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
```

### Visual Studio Code
Terminal
```bash
pytest test_square.py
```

Mocking

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_square.py
venv

service.py
database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_service.py
test_square.py
venv

test_service.py
import pytest_
import source.service as service
import unittest.mock as mock

@mock.patch("source.service, get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    
    assert user_name == "Mocked Alice"
```

```python
Visual Studio Code
Terminal
pytest test_service.py
cd ..
pip install requests 

Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_service.py
test_square.py
venv

test_service.py
import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError
```

https://jsonplaceholder.typicode.com/ 

https://jsonplaceholder.typicode.com/users 

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_service.py
test_square.py
venv

test_service.py
import pytest_
import source.service as service
import unittest.mock as mock

@mock.patch("source.service, get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    
    assert user_name == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_service.py
```

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_service.py
test_square.py
venv

test_service.py
import pytest_
import source.service as service
import unittest.mock as mock

@mock.patch("source.service, get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)
    
    assert user_name == "Mocked Alice"

@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}

@mock.patch("requests.get")
def test_get_users_errors(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
```

ChatGPT and Testing 

## Source Code
```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
school.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_service.py
test_square.py
venv

school.py
class TooManyStudents(Exception):
    pass

class Classroom:

    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title    

    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student) 
        else:
            raise TooManyStudents
        
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher

class Person:

    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass

chat.openai.com
Using pytest and the functions that come from it. Such as fixtures, parametrize, raises and mock, whenever necessary. Test the following code and theme it after Harry Potter: 

class TooManyStudents(Exception):
    pass

class Classroom:

    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title    

    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student) 
        else:
            raise TooManyStudents
        
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher

class Person:

    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass
```

```python
Visual Studio Code
EXPLORER
OPEN EDITORS
source
my_functions.py
school.py
service.py
shapes.py
test
tets_circle.py
test_my_functions.py
test_rectangle.py
test_school.py
test_service.py
test_square.py
venv

chat.openai.com
test_school.py
from pytest import raises
from unittest.mock import Mock
from your_module_name import Classroom, Teacher, Student, TooManyStudents

# Test adding a student to a classroom
def test_add_student():
    teacher = Teacher("Professor McGonagall")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Transfiguration"
    classroom = Classroom(teacher, students, course_title)

    new_student = Student("Harry Potter")
    classroom.add_student(new_student)

    assert len(classroom.students) == 11
    assert new_student in classroom.students

# Test adding too many students to a classroom
def test_add_too_many_students():
    teacher = Teacher("Professor Snape")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Potions"
    classroom = Classroom(teacher, students, course_title)

    with raises(TooManyStudents):
        classroom.add_student(Student("Ron Weasley"))

# Test removing a student from a classroom
def test_remove_student():
    teacher = Teacher("Professor Flitwick")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "Charms"
    classroom = Classroom(teacher, students, course_title)

    student_to_remove = students[3].name
    classroom.remove_student(student_to_remove)

    assert len(classroom.students) == 9
    assert student_to_remove not in [student.name for student in classroom.students]

# Test changing the teacher of a classroom
def test_change_teacher():
    initial_teacher = Teacher("Professor Binns")
    students = [Student(f"Student_{i}") for i in range(10)]
    course_title = "History of Magic"
    classroom = Classroom(initial_teacher, students, course_title)

    new_teacher = Teacher("Professor Dumbledore")
    classroom.change_teacher(new_teacher)

    assert classroom.teacher == new_teacher

# Test that the Person class initializes correctly
def test_person_init():
    name = "Severus Snape"
    person = Person(name)
    assert person.name == name
```

### Visual Studio Code
Terminal
```bash
pytest tests/test_school.py
```

