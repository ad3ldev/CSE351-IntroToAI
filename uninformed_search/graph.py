from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end, weight):
        self.graph[start].append([end, weight])
