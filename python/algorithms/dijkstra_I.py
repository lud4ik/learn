"""
    Dijkstra's algorithm for weighted graphs (I).
    Work for directional and nondirectional graphs.
"""
import time
from collections import defaultdict


def get_input(file_path, directional=True):
    graph, nodes = defaultdict(dict), set()
    with open(file_path, "r") as f:
        for line in f:
            start, stop, distance = line.split()
            nodes = nodes.union([start, stop])
            graph[start][stop] = float(distance)
            if not directional:
                graph[stop][start] = float(distance)
    return graph, nodes


def get_root(stop, path):
    v = stop
    while v:
        yield v
        v = path[v][1]


def dijkstra(graph, gvertex, start, stop):
    path = defaultdict(lambda: [float('inf'), 0])
    vertex = set()
    for v in gvertex:
        path[v]
        vertex.add(v)

    path[start][0] = 0

    while vertex:
        permanent = min(vertex, key=lambda x: path[x][0])
        if permanent == stop:
            break

        distance = path[permanent][0]
        vertex.remove(permanent)

        for v, d in graph[permanent].items():
            _v = path[v]
            if distance + d < _v[0]:
                _v[0], _v[1] = distance + d, permanent

    if path[stop][0] != float('inf'):
        return  path[stop][0], get_root(stop, path)
    else:
        return None, None


def get_path(file_path, start, stop, directional=True):
    graph, vertex = get_input(file_path, directional)
    distance, root = dijkstra(graph, vertex, start, stop)
    if distance:
        result = ""
        for v in reversed(list(root)):
            result += "{} -> ".format(v)
        result += "{:.2f}".format(distance)
        print(result)
    else:
        print("No root from {} to {}.".format(start, stop))


if __name__ == "__main__":
    start = time.time()
    get_path("input.txt", "A", "F", directional=False)
    stop = time.time()
    print("{:.10f}".format(stop - start))