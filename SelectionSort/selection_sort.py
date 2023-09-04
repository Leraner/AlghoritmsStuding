"""
Алгоритм сортировки выбором
Смысл находить максимальный или минимальный элемент и добавлять в новый список
О-большое - n^2
"""


# Возвращает индекс самого маленького элемента
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


# Сортирует список
def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort([3, 2, 5]))
