#Task 1
"""
Breadth first search

"""

graph = {
    'A':['B', 'E'],
    'B':['F'],
    'C':['G'],
    'D':['E', 'H'],
    'E':['A', 'D', 'H'],
    'F':['B', 'G', 'I', 'J'],
    'G':['C', 'F', 'J'],
    'H':['D', 'E', 'I'],
    'I':['F', 'H'],
    'J':['F', 'G'],
}


def bfs_connected_components (graph, start):

    explored = []
    queue   = [start]

    while queue:
        node = queue.pop(0)

        if node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    
    return explored

print(bfs_connected_components(graph, 'A'))

#Task 2
"""
Shortest Path Algorithm

"""

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A','D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B','D'],
    'F': ['C'],
    'G': ['C']
}

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue   = [[start]]

    if start == goal:
        return "Thet was easy! Start =  Goal"
    
    while queue:
        path = queue.pop(0)
        node = path [-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == goal:
                        return new_path
            
            explored.append(node)

    return "So sorry, but a connecting path doesn't exist :("


print("Path between G and D : ",bfs_shortest_path(graph, 'G', 'D'))

#Task 3
"""
Add an isolated node 'I' and find path between
'A' and 'I'

"""


graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A','D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B','D'],
    'F': ['C'],
    'G': ['C'],
    'I': []
}

print("Path between A and I : ", bfs_shortest_path(graph, 'A', 'I'))

#Task 4
"""
All paths

"""

graph = {
    'A': set(['B', 'C', 'E']),
    'B': set(['A','D', 'E']),
    'C': set(['A', 'F', 'G']),
    'D': set(['B', 'E']),
    'E': set(['A', 'B','D']),
    'F': set(['C']),
    'G': set(['C']),
}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
            

print(list(bfs_paths(graph, 'G', 'D')))