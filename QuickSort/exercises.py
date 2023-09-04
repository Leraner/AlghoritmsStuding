music_player = [
    {'listeners': 100, 'music': 'SomeMusic1'},
    {'listeners': 20, 'music': 'SomeMusic2'},
    {'listeners': 3000, 'music': 'SomeMusic3'},
    {'listeners': 90, 'music': 'SomeMusic4'}
]


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        support_element = array[0]
        support_element_listeners = support_element['listeners']
        less_than_support_element = [i for i in array[1::] if i['listeners'] <= support_element_listeners]
        greate = [i for i in array[1::] if i['listeners'] > support_element_listeners]

        return quick_sort(less_than_support_element) + [support_element] + quick_sort(greate)


print(quick_sort(music_player))
