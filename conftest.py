import pytest
import random
import math

@pytest.fixture()
def function_fixture(request):
    print(f"Фикстура тип {request.scope} открыта")

    def fin():
        print (f"Фикстура типа {request.scope} закрыта")
    request.addfinalizer(fin)

@pytest.fixture(scope = 'session')
def session_fixture(request):
    print(f"Фикстура тип {request.scope} открыта")
    def fin():
        print(f"Фикстура тип {request.scope} закрыта")
    request.addfinalizer(fin)

@pytest.fixture (scope = "class")
def class_fixture(request):
    print (f"Фикстура тип {request.scope} открыта")

    def fin():
        print (f"Фикстура тип {request.scope} закрыта")
    request.addfinalizer(fin)

@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"Фикстура тип {request.scope} открыта")
    def fin():
        print(f"Фикстура тип {request.scope} закрыта")
    request.addfinalizer(fin)

@pytest.fixture #1
def fixture_return_string():
    names = ["Vasilii","Sasha", "Ira", "Grigorii", "ivan"]
    name = random.choice(names)
    print (f"Выбранное имя: {name}")
    return name

@pytest.fixture #2
def fixture_return_number():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a*b

@pytest.fixture #3
def fixture_dir():
    dist = {1:"apple", 2: "orange"}
    fruit = random.choice(list(dist.values()))
    print(f"Выбранное значение: {fruit}")
    return fruit

@pytest.fixture
def fixture_tuple():
    listed = (12, "orange", 234, "true", 23, -566, "dog", 111)
    selection = int(len(listed))
    print(f"В строке: {selection} элементов")
    return selection

@pytest.fixture
def fixture_sum_list():
    listed_1 = [1, 3, 4, 5, "Misha"]
    listed_2 = [3, 5, "Vova" , 567, 12]
    for a in listed_2:
        listed_1.append(a)
    print(f"Полный спискок: {listed_1}")
    return int(len(listed_1))

class TestClass:

    def __init__(self, mod1= None, mod2= None, name = None, age = None, phone = None, num1 = None, num2 = None):
        self.mod1 = mod1
        self.mod2 = mod2
        self.name = name
        self.age = age
        self.phone = phone
        self.num1 = num1
        self.num2 = num2

    def set_person_info(self, name, age, phone):
        """Устанавливает информацию о человеке"""
        self.name = name
        self.age = age
        self.phone = phone

    def hello(self, name):
        return f"Привет {name}"

    def albert(self):
        return f"{self.name}, {self.age} лет, тел.: {self.phone}"

    def number_sum(self, num1, num2):
        if self.num2 == 0:
            print(f"Ошибка, значение {self.num2} не корректно, на {self.num2} делить нельзя.")
            return None  # Важно вернуть None, чтобы избежать ошибки
        else:
            result = num1/num2
        return result


@pytest.fixture
def fixture_return_class():
    return TestClass(mod1=random, mod2=math)

@pytest.fixture(params=[
    (10, 5, 2.0),    # 10/5 = 2
    (8, 2, 4.0),     # 8/2 = 4
    (10, -5, -2.0),  # 10/-5 = -2
    (0, 5, 0)
])
def division_test_data(request):
    """Фикстура с параметрами для тестирования деления"""
    num1, num2, expected = request.param
    instance = TestClass()
    instance.num1 = num1
    instance.num2 = num2
    return instance, num1, num2, expected


