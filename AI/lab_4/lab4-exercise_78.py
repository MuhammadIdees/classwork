#Question: a
"""
Traverse through graph

"""

graph = {
    '1' : ['2', '3', '4'],
    '2' : ['3', '4', '1'],
    '3' : ['2', '1', '4'],
    '4' : ['1', '2' ,'3', '5'],
    '5' : ['6', '7', '8', '4'],
    '6' : ['7', '8', '5'],
    '7' : ['6', '5', '8'],
    '8' : ['5', '6','7']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        
        for n in graph[node]:
            dfs(graph, n, visited)
    
    return visited

visited = dfs(graph, '1', [])
print ("Traversal Path : ",visited)

#Question: b
"""
Shortest path between 1 and 6

"""

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

print("Shortest path between 1 and 6 : ", dfs_shortest_path(graph, '1', '6'))

#Question: c
""" path between 1 and 6

"""

graph = {
    '1' : set(['2', '3', '4']),
    '2' : set(['3', '4', '1']),
    '3' : set(['2', '1', '4']),
    '4' : set(['1', '2' ,'3', '5']),
    '5' : set(['6', '7', '8', '4']),
    '6' : set(['7', '8', '5']),
    '7' : set(['6', '5', '8']),
    '8' : set(['5', '6', '7'])
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
            

print("All paths between 1 and 6 :", list(dfs_paths(graph, '1', '6')))

print("\n\n\n")

#Question: 2

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E'],
    'C' : ['A', 'F'],
    'D' : ['A', 'E', 'G'],
    'E' : ['B', 'D', 'G'],
    'F' : ['C', 'G'],
    'G' : ['F', 'E'],   
}

visited = dfs(graph, 'A', [])
print ("Traversal Path : ",visited)

print("Shortest path between A and G : ", dfs_shortest_path(graph, 'A', 'G'))

graph = {
    'A' : set(['B', 'C', 'D']),
    'B' : set(['A', 'E']),
    'C' : set(['A', 'F']),
    'D' : set(['A', 'E', 'G']),
    'E' : set(['B', 'D', 'G']),
    'F' : set(['C', 'G']),
    'G' : set(['F', 'E']),   
}

print("All paths between A and G :", list(dfs_paths(graph, 'A', 'G')))


