from pygraph.Graph import Graph
from pygraph.GraphMatrix import GraphMatrix

if __name__ == '__main__':
    print('Running Graph test... ', end='')
    g: Graph = Graph(5)
    g.insert_edge(0, 1, 1.0)
    g.insert_edge(0, 3, 1.0)
    g.insert_edge(0, 4, 3.0)
    g.insert_edge(1, 2, 2.0)
    g.insert_edge(1, 4, 1.0)
    g.insert_edge(3, 4, 3.0)
    g.insert_edge(4, 2, 3.0)
    g.insert_edge(4, 3, 3.0)
    print('Success!')

    print('Running GraphMatrix test... ', end='')
    gm: GraphMatrix = GraphMatrix(5, undirected=False)
    gm.set_edge(0, 1, 1.0)
    gm.set_edge(0, 3, 1.0)
    gm.set_edge(0, 4, 3.0)
    gm.set_edge(1, 2, 2.0)
    gm.set_edge(1, 4, 1.0)
    gm.set_edge(3, 4, 3.0)
    gm.set_edge(4, 2, 3.0)
    gm.set_edge(4, 3, 3.0)
    print('Success!')