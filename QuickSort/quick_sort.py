"""
Быстрая сортировка
Смысл в том, что берется опорный элемент, создаются два подмассива, один - элементы меньше опорного,
второй - элементы больше опорного, к ним применяется тот же алгоритм быстрой сортировки
Занимает достаточно большое кол-во памяти
O-notation - n*log(n)
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        support_element = arr[0]
        less_than_support_element = [i for i in arr[1::] if i <= support_element]
        greate = [i for i in arr[1::] if i > support_element]

        return quick_sort(less_than_support_element) + [support_element] + quick_sort(greate)


print(quick_sort([1, 10, 2, 50, 3, 2]))
