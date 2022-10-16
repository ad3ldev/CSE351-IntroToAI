from uninformed_search.bfs import bfs
from uninformed_search.dfs import dfs_iterative, dfs_recursive
from uninformed_search.dls import dls
from uninformed_search.graph import Graph
from uninformed_search.idfs import idfs
from uninformed_search.ucs import ucs


def empty_visited(graph):
    visited = {}
    for i in graph:
        visited[i] = False
    return visited


if __name__ == '__main__':
    g = Graph()
    g.add_edge("S", "A", 2)
    g.add_edge("S", "F", 7)
    g.add_edge("A", "F", 8)
    g.add_edge("A", "C", 4)
    g.add_edge("F", "H", 2)
    g.add_edge("F", "A", 8)
    g.add_edge("F", "G", 5)
    g.add_edge("C", "D", 3)
    g.add_edge("C", "G", 5)
    g.add_edge("D", "G", 3)
    g.add_edge("H", "", 0)
    g.add_edge("G", "", 0)
    ucs(g.graph, "S")
