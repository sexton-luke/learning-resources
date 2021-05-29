from reference_classes.graph import Graph


# Question 1
def graph_from_edge_list(E, directed=False):
    """Make a graph instance based on a sequence of edge tuples.

    Edges can be either of from (origin,destination) or
    (origin,destination,element). Vertex set is presume to be those
    incident to at least one edge.

    vertex labels are assumed to be hashable.
    """
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])

    vertices_map = {}  # map from vertex label to Vertex instance
    for v in V:
        vertices_map[v] = g.insert_vertex(v)

    for e in E:
        src = e[0]
        destination = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(vertices_map[src], vertices_map[destination], element)

    return g


E = (('U', 'V', 1), ('U', 'W', 2),
     ('V', 'X', 3), ('V', 'W', 4),
     ('W', 'X', 5), ('W', 'Y', 6),
     ('X', 'Y', 7), ('X', 'Z', 8)
     )
graph = graph_from_edge_list(E, False)

vertices = []
edges = []
print('1. Vertices (Undirected Graph):')
for vertex in graph.outgoing:
    vertices.append(vertex)
    print(vertex)

for vertex in graph.outgoing:
    print('>>> Vertex --', vertex)
    print('>>> Adjacent Vertices (Origin, Destination, Path Number')
    incidents = graph.incident_edges(vertex)
    for incident in incidents:
        edges.append(incident)
        print(">>> Incident:", incident)


# Question 2
def BFS(g, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]  # first level includes only s
    while len(level) > 0:
        next_level = []  # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):  # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:  # v is an unvisited vertex
                    discovered[v] = e  # e is the tree edge that discovered v
                    next_level.append(v)  # v will be further considered in next pass
        level = next_level  # relabel 'next' level to become current


def BFS_complete(g):
    """Perform BFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (vertices that are roots of a BFS tree are mapped to None).
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None  # u will be a root of a tree
            BFS(g, u, forest)
    return forest


print("\n2. Breadth First Search (BFS)")
bfs = BFS_complete(graph)
for key, value in bfs.items():
    print('>>> Found:', key, 'along the', value, 'path')


# Question 3
def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):  # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:  # v is an unvisited vertex
            discovered[v] = e  # e is the tree edge that discovered v
            DFS(g, v, discovered)  # recursively explore from v


def construct_path(u, v, discovered):
    """
    Return a list of vertices comprising the directed path from u to v,
    or an empty list if v is not reachable from u.

    discovered is a dictionary resulting from a previous call to DFS started at u.
    """
    path = []  # empty path by default
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]  # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()  # reorient path from u to v
    return path


def DFS_complete(g):
    """Perform DFS for entire graph and return forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None  # u will be the root of a tree
            DFS(g, u, forest)
    return forest


print("\n3. Depth First Search (DFS)")
dfs = DFS_complete(graph)
for key, value in dfs.items():
    print('>>> Found:', key, 'along the', value, 'path')

# Question 4
E2 = (('1', '2', 'Path1'), ('1', '3', 'Path2'), ('1', '4', 'Path3'),
      ('2', '3', 'Path4'), ('2', '4', 'Path5'),
      ('3', '4', 'Path6'),
      ('4', '6', 'Path7'),
      ('6', '5', 'Path8'), ('6', '7', 'Path9'),
      ('5', '7', 'Path10'), ('5', '8', 'Path11'),
      ('7', '8', 'Path12')
      )
graph = graph_from_edge_list(E2, False)

vertices = []
edges = []
print('\n4a. Vertices (Undirected Graph):')
for vertex in graph.outgoing:
    vertices.append(vertex)
    print(">>> Vertex:", vertex)

for vertex in graph.outgoing:
    print('>>> Vertex --', vertex)
    print('>>> Adjacent Vertices (Origin, Destination, Path Number')
    incidents = graph.incident_edges(vertex)
    for incident in incidents:
        edges.append(incident)
        print(">>> Incident:", incident)

print("\n4b. Breadth First Search (BFS)")
bfs = BFS_complete(graph)
for key, value in bfs.items():
    print('>>> Found:', key, 'along the', value)

print("\n4c. Depth First Search (DFS)")
dfs = DFS_complete(graph)
for key, value in dfs.items():
    print('>>> Found:', key, 'along the', value)
