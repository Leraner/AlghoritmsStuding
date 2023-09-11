"""
Упражнения к алгоритму Декстры
"""

# Найти пут
graph = {
    'start': {
        'b': 1,
        'd': 4,
        'c': 9
    },
    'b': {
        'e': 1,
        'd': 2,
    },
    'd': {
        'e': 4,
        'f': 2,
        'fin': 9,
        'c': 5
    },
    'c': {
        'd': 5,
        'f': 8,
    },
    'e': {
        'd': 4,
        'fin': 5
    },
    'f': {
        'd': 2,
        'fin': 1
    },
    'fin': {}
}
costs = {
    'b': 1,
    'd': 4,
    'c': 9,
    'e': float('inf'),
    'f': float('inf'),
    'fin': float('inf')
}
parents = {
    'b': 'start',
    'c': 'start',
    'd': 'start',
    'e': None,
    'f': None,
    'fin': None
}

processed = []


def find_smallest(costs):
    lower_cost = float('inf')
    lower_cost_node = None

    for node in costs:
        cost = costs[node]
        if node not in processed and cost < lower_cost:
            lower_cost = cost
            lower_cost_node = node

    return lower_cost_node


node = find_smallest(costs)
while node is not None:
    neighbours = graph[node]
    cost = costs[node]
    for n in neighbours:
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            parents[n] = node
            costs[n] = new_cost

    processed.append(node)
    node = find_smallest(costs)

# Отображение пути
goal = 'start'
a = []
node = 'fin'
while node != goal:
    node = parents[node]
    a.append(node)

for i in a[::-1]:
    print(i + ' ----> ', end='')
else:
    print('fin', end='')























