"""
Алгоритм Дейкстры
Поиск кратчайшего пути исходя из веса ребер (Вес ребер не должен быть отрицательным).

Три хэш таблицы:
    1) Граф
    2) Стоимость
    3) Родители
"""

graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}
}
costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

# Массив для отслеживания всех уже обработанных узлов,
# так как один узел не должен обрабатываться многократно
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(processed)
print(costs['fin'])