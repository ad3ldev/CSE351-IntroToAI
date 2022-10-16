def bfs(graph, start):
    visited = {}
    for i in graph:
        visited[i] = False
    queue = [start]
    visited[start] = True
    while queue:
        start = queue.pop(0)
        if len(start) > 1:
            start = start[0]
        print(start)
        for i in graph[start]:
            node = i[0]
            if node == "":
                continue
            if not visited[node]:
                queue.append(i)
                visited[node] = True
