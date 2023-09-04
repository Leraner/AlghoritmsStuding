music_player = [
    {'listeners': 100, 'music': 'SomeMusic1'},
    {'listeners': 20, 'music': 'SomeMusic2'},
    {'listeners': 3000, 'music': 'SomeMusic3'},
    {'listeners': 90, 'music': 'SomeMusic4'}
]


def find_smallest(arr):
    smallest = arr[0]['listeners']
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i]['listeners'] < smallest:
            smallest = arr[i]['listeners']
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort(music_player))
