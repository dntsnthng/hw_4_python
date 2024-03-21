

def test_greeting():
    name = "Анна"
    age = 25
    hi = "Привет"
    u = "Тебе"
    l = "лет"
    output = f"{hi}, {name}! {u} {age} {l}."
    # TODO Сформируйте нужную строку


    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    perimeter= (a*2)+(b*2)
    area= a*b
    # TODO сосчитайте периметр


    assert perimeter == 60

    # TODO сосчитайте площадь


    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    import math
    r = 23
    # TODO сосчитайте площадь
    area = math.pi*r**2

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2*math.pi*r

    assert length == 144.51326206513048


def test_random_list():

    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список

    l = [1,22,15,88,54,60,18,2,10,100]
    list.sort(l)


    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    l= list(set(l))

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    dict_keys = list(first)
    second = [1, 2, 3, 4, 5]
    dict_vals = list(second)
    # TODO создайте словарь
    d = {"a":1,"b":2,"c":3,"d":4,"e":5}

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second


