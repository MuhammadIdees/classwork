#Question 1
"""
Breadth first search

"""

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E'],
    'C' : ['A', 'F'],
    'D' : ['A', 'E', 'G'],
    'E' : ['B', 'D', 'G'],
    'F' : ['C', 'G'],
    'G' : ['F', 'E'],   
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

print("All nodes : ", bfs_connected_components(graph, 'A'))

#Question 2
"""
Shortest Path Algorithm

"""
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


print("Path between 1 and 6 : ",bfs_shortest_path(graph, 'A', 'G'))

#Question 3
"""
All paths

"""


graph = {
    'A' : set(['B', 'C', 'D']),
    'B' : set(['A', 'E']),
    'C' : set(['A', 'F']),
    'D' : set(['A', 'E', 'G']),
    'E' : set(['B', 'D', 'G']),
    'F' : set(['C', 'G']),
    'G' : set(['F', 'E']),   
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
            

print("All path between 1 and 6 : ", list(bfs_paths(graph, 'A', 'G')))