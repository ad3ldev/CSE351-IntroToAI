from uninformed_search.dls import dls


def idfs(graph, start, visited):
    for i in range(1, len(graph) + 1):
        print("depth: ", i)
        print("-----------------")
        dls(graph, start, i, visited)
