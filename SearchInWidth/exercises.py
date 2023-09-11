from collections import deque

""" Поиск кратчайшего пути исходя из наименьшего количества ребер """

graph = {
    'A': ['P', 'B'],
    'B': ['A', 'D'],
    'D': ['B', 'C'],
    'P': ['A', 'C'],
    'C': ['P', 'D']
}


def search(start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current_node = queue.popleft()

        if current_node == goal:
            break

        next_nodes = graph[current_node]
        for node in next_nodes:
            if node not in visited:
                queue.append(node)
                visited.update({node: current_node})

    return visited


start = 'A'
goal = 'C'

visited = search(start, goal)

current_node = goal

route = []

while current_node != start:
    route.append(current_node)
    current_node = visited[current_node]
route.append(start)
print(route[::-1])
