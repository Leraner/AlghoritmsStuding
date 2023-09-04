# Известна фамилия, нужно найти номер в телефонной книге.

phone_book = [
    {'Peter': 89213617788},
    {'Mary': 89235567798},
    {'Jane': 89123334455},
    {'Jack': 89276665533}
]


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if list(guess.keys())[0] == item:
            return mid

        if item in map(lambda x: list(x.keys())[0], lst[low:mid]):
            high = mid - 1
        else:
            low = mid + 1

    return None


sorted_list = sorted(phone_book, key=str)
result = binary_search(sorted_list, 'Peter')
# Возвращает индекс записи
print(result)

# Известен номер, нужно найти фамилию в телефонной книге.

phone_book = [
    {89217773366: 'Peter'},
    {89218889900: 'Jane'},
    {89318883311: 'Jack'},
    {89413334422: 'Mary'},
]


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if list(guess.keys())[0] == item:
            return mid

        if item in map(lambda x: list(x.keys())[0], lst[low:mid]):
            high = mid - 1
        else:
            low = mid + 1

    return None


sorted_list = sorted(phone_book, key=lambda x: int(list(x.keys())[0]))
print(sorted_list)
result = binary_search(sorted_list, 89218889900)
# Возвращает индекс записи
print(result)
