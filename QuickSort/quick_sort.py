"""
Быстрая сортировка
Смысл в том, что берется опорный элемент, создаются два подмассива, один - элементы меньше опорного,
второй - элементы больше опорного, к ним применяется тот же алгоритм быстрой сортировки
Занимает достаточно большое кол-во памяти
O-notation - n*log(n)

Если берем первый элемент, затрачивается много памяти из-за стека вызовов, потому что он всегда держит массив []
Лучшего случая не бывает, бывает худший и средний, потому что лучший случай - средний
Даже если брать рандомный элемент всегда будет средний случай
"""
import random


def quick_sort1(arr):
    if len(arr) < 2:
        return arr
    else:
        support_element = arr[0]
        less_than_support_element = [i for i in arr if i <= support_element]
        greate = [i for i in arr if i > support_element]

        return quick_sort1(less_than_support_element) + [support_element] + quick_sort1(greate)


def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    else:
        low = 0
        high = len(arr) - 1
        support_element = arr[(low + high) // 2]
        arr.pop((low + high) // 2)
        less_than_support_element = [i for i in arr if i <= support_element]
        greate = [i for i in arr if i > support_element]

        return quick_sort2(less_than_support_element) + [support_element] + quick_sort2(greate)


def quick_sort3(arr):
    if len(arr) < 2:
        return arr
    else:
        index = random.randint(0, len(arr) - 1)
        support_element = arr[index]
        arr.pop(index)
        less_than_support_element = [i for i in arr if i <= support_element]
        greate = [i for i in arr if i > support_element]

        return quick_sort2(less_than_support_element) + [support_element] + quick_sort2(greate)


print(quick_sort3([1, 5, 3, 2]))
