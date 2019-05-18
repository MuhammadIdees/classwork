#Task 1
"""
 Draw the given graph

"""

graph = {
    "Mayor House"   : ["Bakery", "Brewery"],
    "Bakery"        : ["Mayor House", "McPane Farm"],
    "Brewery"       : ["Mayor House", "Inn", "McPane Farm"],
    "McPane Farm"   : ["Bakery", "Brewery", "Thomas Farm"],
    "Thomas Farm"   : ["McPane Farm"],
    "Inn"           : ["Brewery", "Library", "Dry Cleaner"],
    "Library"       : ["Inn", "City Hall"],
    "Dry Cleaner"   : ["Inn", "City Hall"],
    "City Hall"     : ["Dry Clearner", "Library"],
}

print (graph["d"])
print("The nodes / vertices of graph: ", graph.keys())
print("The edges of the graph for keys {0} are {1}".format(graph.keys() , graph.values()))

for i, j in graph.items():
    print(i , j)

# Task 2
"""
 Generating edges

"""

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

print ("Generating Edges: ", generate_edges(graph))

# Task 3
"""
Finding isolated nodes

"""
def find_isolated_nodes(graph):

    isolated = []
    for node in graph:       # traverse each node
        if not graph[node]:        # value for this node is nothing
            isolated += node # add the node to list
    return isolated

print("Isolated nodes", find_isolated_nodes(graph))

#Task 4
"""
Find path between two nodes

"""

def find_path(graph, start, end, path = []): # the empty list saves the value of path
    path = path + [start] # adding first node

    if start == end: # check if both are same
        return path

    if not (start in graph): # if key start not present in graph
        return None

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                return newpath
                
    return None

path = []

print("Path between nodes", find_path(graph, 'e', 'd', path))

#Task 5
"""
Finding all paths between two nodes

"""
def find_all_paths(graph, start, end, path = []):
    path = path + [start]

    if start == end:
        return [path]

    if not start in graph:
        return []
    
    paths = []
    
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

print("All Paths between nodes", find_all_paths(graph, 'd', 'b'))

# Task 6
"""
Find the shortest path

"""
def find_shortest_path(graph, start, end, path = []):
    path = path + [start]

    if start == end:
        return path

    if not start in graph:
        return None
    
    shortest = None
    
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            
            if newpath:
                if not shortest or len(newpath) <  len(shortest):
                    shortest = newpath
    return shortest

print("Shortest path: ", find_shortest_path(graph, '1', '7'))

#Task 7
"""
Adding Edges

"""
print("Actual graph",graph)

#Adding an edge
def add_edge(graph,edge):
    edge = set(edge)        # if you don’t want duplicates in list than you will use set
    (n1,n2) = tuple(edge)   # same as list; can’t be changed
    
    if n1 in graph:
        graph[n1] += n2      
    
    return graph

print("After adding an edge:", add_edge(graph,{'9','8'}))

#Task 8
"""
Cycles in graph

"""

def find_cycle_single_node(graph, start):
    for node in graph[start]:
        if node == start:
            return "cycle exists"
    
    return "cycle does not exist"

print (find_cycle_single_node(graph, "1"))

#Task 9
"""
Degree of vertex

"""

def find_degree(graph, node):
    degree = 0
    t = []

    for neighbour in graph[node]:
        t.append(neighbour)
        degree += 1
    
    return degree

degree = find_degree(graph, "4")
print("Degree of the vertex : ", degree)

#Task 10
"""
Connected Graphs

"""

def graph_connected(graph, seen_node = None, start = None):
    if seen_node == None:
        seen_node = set()
        nodes = list(graph.keys())              #list of all the graph keys

    if not start:
        start = nodes[0]                   #vertex at the 0th wil be start
        seen_node.add(start)

        if len(seen_node) < len(nodes):
            for othernodes in graph[start]:
                if othernodes not in seen_node:
                    if graph_connected(graph, seen_node, othernodes):
                        return True
                else:
                    return True

    return False

conn = graph_connected(graph, seen_node = None, start = None)

if conn:
    print ("The graph is connected")
else:
    print ("The graph is not connected")