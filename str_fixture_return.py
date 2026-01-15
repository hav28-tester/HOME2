def test_the_str(fixture_return_string, function_fixture, session_fixture, module_fixture ):
    print("********************")
    assert fixture_return_string in ['Ira', 'Grigorii']
    print(f"Имя {fixture_return_string} прошло проверку")

def test_the_numbers(fixture_return_number, function_fixture, session_fixture, module_fixture):
    assert fixture_return_number > 0
    assert fixture_return_number < 0

def test_dir(fixture_dir, function_fixture, session_fixture, module_fixture):
    assert fixture_dir == "apple"

def test_tuple(fixture_tuple, function_fixture, module_fixture, session_fixture, class_fixture):
    assert fixture_tuple == 8

def test_list_sum(fixture_sum_list, function_fixture, module_fixture, session_fixture, class_fixture):
    print (f"Список после сложения 2 списков: {fixture_sum_list}")
    assert fixture_sum_list == 10

def test_return_class_list(fixture_return_class, function_fixture, session_fixture, class_fixture):
    assert fixture_return_class.hello("Маша") == "Привет Маша"

def test_return_class_class_number(fixture_return_class, function_fixture, session_fixture, class_fixture):
    assert fixture_return_class.mod2.pow(2,3) == 8

def test_return_class_math(fixture_return_class, function_fixture, session_fixture, class_fixture):
    assert fixture_return_class.mod2.fabs(-8) == 8

def test_return_division(division_test_data, module_fixture, class_fixture, session_fixture, function_fixture):
    instance, num1, num2, expected = division_test_data
    result = instance.number_sum(num1,num2)
    print(result)
    assert result == expected

