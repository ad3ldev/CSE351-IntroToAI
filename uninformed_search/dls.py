def dls(graph: object, start: object, max_depth: object, visited: object) -> object:
    if max_depth <= 0:
        return
    visited[start] = True
    print(start)
    for i in graph[start]:
        node = i[0]
        if node != "":
            dls(graph, node, max_depth - 1, visited)
