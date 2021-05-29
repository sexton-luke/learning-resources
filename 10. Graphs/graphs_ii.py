from reference_classes.graph import Graph
from reference_classes.partition import Partition
from reference_classes.references_priority_base_queues import HeapPriorityQueue, AdaptableHeapPriorityQueue


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

    vertice_map = {}  # map from vertex label to Vertex instance
    for v in V:
        vertice_map[v] = g.insert_vertex(v)

    for e in E:
        src = e[0]
        destination = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(vertice_map[src], vertice_map[destination], element)

    return g


E = (
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'D'), ('C', 'D'), ('C', 'E'),
    ('D', 'E'), ('E', 'A')
)

graph = graph_from_edge_list(E, True)

vertices = []
edges = []
print('1. Vertices (Directed Graph):')
for vertex in graph.incoming:
    vertices.append(vertex)
    print(vertex)

for vertex in graph.incoming:
    print('>>> Vertex --', vertex)
    print('>>> Adjacent Vertices (Origin, Destination, Path Number')
    incidents = graph.incident_edges(vertex)
    for incident in incidents:
        edges.append(incident)
        print(">>> Incident:", incident)

# Question 2
E2 = (
    ('A', 'B', 4), ('A', 'C', 7), ('A', 'D', 6), ('A', 'F', 15),
    ('B', 'E', 3), ('C', 'F', 8), ('D', 'E', 2),
    ('E', 'F', 5)
)

graph = graph_from_edge_list(E, False)

vertices = []
edges = []
print('\n2. Vertices (directed Graph):')
for vertex in graph.outgoing:
    vertices.append(vertex)
    print(">>> Vertex:", vertex)

for vertex in graph.outgoing:
    print('Vertex --', vertex)
    print('Adjacent Vertices (Origin, Destination, Path Number)')
    incidents = graph.incident_edges(vertex)
    for incident in incidents:
        edges.append(incident)
        print(">>> Incident:", incident)


# Question 3
E = (
        ('A', 'B', 4), ('A', 'C', 9), ('A', 'D', 6),
        ('B', 'D', 3), ('B', 'F', 7), ('C', 'D', 2), ('C', 'E', 9),
        ('D', 'E', 5), ('D', 'F', 3), ('F', 'E', 1)
    )

graph = graph_from_edge_list(E, False)

vertices = []
edges = []
print('\n3. Vertices (Directed Graph):')
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


# Question 4
def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.

    The elements of the graph's edges are assumed to be weights.
    """
    tree = []  # list of edges in spanning tree
    pq = HeapPriorityQueue()  # entries are edges in G, with weights as key
    forest = Partition()  # keeps track of forest clusters
    position = {}  # map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)  # edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)

    return tree


print("\n4. Krushkal's Algorithm")
minimum_spanning_tree = MST_Kruskal(graph)
for spanning_tree in minimum_spanning_tree:
    print(">>> Spanning Tree:", spanning_tree)


# Question 5
def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph g.

    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}  # d[v] is bound on distance to tree
    tree = []  # list of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()  # d[v] maps to value (v, e=(u,v))
    pq_locator = {}  # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:  # this is the first node
            d[v] = 0  # make it the root
        else:
            d[v] = float('inf')  # positive infinity
        pq_locator[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value  # unpack tuple from pq
        del pq_locator[u]  # u is no longer in pq
        if edge is not None:
            tree.append(edge)  # add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pq_locator:  # thus v not yet in tree
                # see if edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:  # better edge to v?
                    d[v] = wgt  # update the distance
                    pq.update(pq_locator[v], d[v], (v, link))  # update the pq entry

    return tree


print("\n5. Prim-Jarnik's Algorithm")
minimum_spanning_tree = MST_PrimJarnik(graph)
for spanning_tree in minimum_spanning_tree:
    print("Spanning Tree:", spanning_tree)
