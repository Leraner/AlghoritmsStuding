"""
Алгоритм бинарного поиска
Смысл: отрезать от правой или от левой части списка половину,
смотря где находится наш искомый элемент.
О-большое - log(n)
"""

number = - 1
numbers = [i for i in range(1, 101)]


def binary_search(number, numbers):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(number, numbers))
