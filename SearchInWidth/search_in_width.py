"""
Поиск в ширину

Поиск в ширину работает с графами.
Решает два вопроса:
    1) Есть ли путь от узла А к узлу Б?
    2) Как выглядит самый короткий пусть от узла А к узлу Б?
Смысл в том, чтобы создавать очередь, добавлять соседей узла, с которого начинаем, начинаем проверку всех соседей,
Если сосед не является тем, что нам нужно, то в очередь добавляем всех соседей соседа и т.д
В результате выводит того, кто нам нужен, или же False.
Поиск в ширину выполняется за время O(кол-во ребер + кол-во узлов)
"""

from collections import deque

already_gotten = []


def person_is_seller(person):
    if person == 'peggy':
        return True
    already_gotten.append(person)
    return False


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]

    while search_queue:
        person = search_queue.popleft()
        if not person in already_gotten:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
    return False


search('you')
