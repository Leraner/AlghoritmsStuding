"""
Рекурсия
Нужна для понимания быстрой сортировки (Quick Sort)
"""


def countdown(num):
    print(num)
    if num <= 0:
        # Базовый случай
        return
    else:
        # Рекурсивный случай
        countdown(num - 1)


countdown(3)
