"""
    Dijkstra's algorithm for weighted graphs (II). Matrix representation.
"""
import time


def get_input(file_path):
    temp, vertex, index = [], {}, 0
    with open(file_path, "r") as f:
        for line in f:
            start, stop, distance = line.split()
            for v in [start, stop]:
                if v not in vertex:
                    vertex[v] = index
                    index += 1
            temp.append((vertex[start], vertex[stop], distance))
    num_vertex = len(vertex)
    graph = [[float('inf') if c != r else 0 for c in range(num_vertex)] \
             for r in range(num_vertex)]
    for start, stop, distance in temp:
        graph[start][stop] = float(distance)
        graph[stop][start] = float(distance)
    return graph, vertex


def get_root(start, stop, previous):
    v = stop
    while True:
        yield v
        if v == start:
            break
        v = previous[v]


def dijkstra(W, start, stop, n):
    V = start
    P = [float('inf') for v in range(n)]
    T = [float('inf') for v in range(n)]
    Pr = [0 for v in range(n)]
    P[start] = 0

    while V != stop:
        S = [P[V] + W[V][j] for j in range(n)]
        for j in range(n):
            if S[j] < T[j]:
                Pr[j] = V
        T = [min(x, y) for x, y in zip(T, S)]
        i = T.index(min(T))
        P[i] = T[i]
        T[i] = float('inf')
        for j in range(n):
            W[j][i] = float('inf')
        V = i

    return P[V], reversed(list(get_root(start, stop, Pr)))


def get_path(file_path, start, stop):
    graph, vertex = get_input(file_path)
    distance, root = dijkstra(graph, vertex[start], vertex[stop], len(vertex))
    vertex = {v: k for k, v in vertex.items()}
    result = ""
    for v in root:
        result += "{} -> ".format(vertex[v])
    result += "{:.2f}".format(distance)
    print(result)


if __name__ == "__main__":
    start = time.time()
    get_path("input.txt", "A", "F")
    stop = time.time()
    print("{:.10f}".format(stop - start))