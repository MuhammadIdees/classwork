#Task 1
"""
Find the traversal path for the given
graph

"""

graph = {
    'A' : ['B', 'E', 'C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        
        for n in graph[node]:
            dfs(graph, n, visited)
    
    return visited

visited = dfs(graph, 'A', [])
print (visited)

graph = {
    'A' : ['C', 'B'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : ['E']
}

visited = dfs(graph, 'A', [])
print (visited)

graph = {
    '1' : ['5', '2'],
    '2' : ['1', '5', '3'],
    '3' : ['2', '4'],
    '4' : ['6','3','5'],
    '5' : ['4', '2', '4'],
    '6' : ['4']
}

visited = dfs(graph, '1', [])
print (visited)


graph = {
    '1' : ['3', '2'],
    '2' : [],
    '3' : ['4', '2'],
    '4' : ['3']
}

visited = dfs(graph, '1', [])
print (visited)

# Task 2
"""
All path between two nodes

"""

graph = {
    'A' : set(['B', 'E', 'C']),
    'B' : set(['D', 'E']),
    'C' : set([]),
    'D' : set([]),
    'E' : set([])
}

def dfs_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
            

print(list(dfs_paths(graph, 'A', 'E')))

#Task 3
"""
Shortest path between two nodes

"""

graph = {
    'A' : ['B', 'E', 'C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

def dfs_shortest_path(graph, start, goal):
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

print(dfs_shortest_path(graph, 'A', 'E'))

graph = {
    '1' : ['3', '4', '2'],
    '2' : ['4', '5'],
    '3' : ['6'],
    '4' : ['6', '7'],
    '5' : ['4', '7'],
    '6' : [],
    '7' : ['6'] 
}

print(dfs_shortest_path(graph, '2', '6'))

graph = {
    '1' : set(['3', '4', '2']),
    '2' : set(['4', '5']),
    '3' : set(['6']),
    '4' : set(['6', '7']),
    '5' : set(['4', '7']),
    '6' : set([]),
    '7' : set(['6']) 
}

print(list(dfs_paths(graph, '2', '6')))