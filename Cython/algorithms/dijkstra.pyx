"""
    Dijkstra's algorithm for weighted graphs (II). Matrix representation.
    cython -3 dijkstra.pyx
    gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python3.3 -o dijkstra.so dijkstra.c
"""
from array import array

from cython.view cimport array as carray


cdef short[:] get_root(int start, int stop, short[:] previous):
    cdef int v = stop
    root = array('h')
    while True:
        root.append(v)
        if v == start:
            break
        v = previous[v]
    return root


cdef dijkstra(float [:, :] W, int start, int stop, int n):
    cdef int V = start, v, j, i
    P = array('f', [float('inf') for v in range(n)])
    T = array('f', [float('inf') for v in range(n)])
    Pr = array('h', [0 for v in range(n)])
    S = array('f', [0 for v in range(n)])
    P[start] = 0

    while V != stop:
        for j in range(n):
            S[j] = P[V] + W[V][j]
        for j in range(n):
            if S[j] < T[j]:
                Pr[j] = V
        for j in range(n):
            T[j] = min(T[j], S[j])
        i = T.index(min(T))
        P[i] = T[i]
        T[i] = float('inf')
        for j in range(n):
            W[j][i] = float('inf')
        V = i

    return P[V], get_root(start, stop, Pr)


cdef class Extract:

    vertex = {}

    cpdef float [:, :] get_input(self, file_path):
        cdef int n, i, j, start, stop, index = 0
        cdef float distance
        temp, vertex = [], self.vertex
        with open(file_path, "r") as f:
            for line in f:
                _start, _stop, _distance = line.split()
                for v in [_start, _stop]:
                    if v not in vertex:
                        vertex[v] = index
                        index += 1
                temp.append((vertex[_start], vertex[_stop], float(_distance)))

        n = len(vertex)
        graph = carray(shape=(n, n), itemsize=sizeof(float), format="f")
        cdef float [:, :] _graph = graph
        for i in range(n):
            for j in range(n):
                if i != j:
                    _graph[i][j] = float('inf')
                else:
                    _graph[i][j] = 0

        for start, stop, distance in temp:
            _graph[start][stop] = distance
            _graph[stop][start] = distance
        return graph

    cpdef get_path(self, file_path, start, stop):
        cdef float [:, :] graph
        graph, vertex = self.get_input(file_path), self.vertex
        distance, root = dijkstra(graph, vertex[start], vertex[stop], len(vertex))
        vertex = {v: k for k, v in vertex.items()}
        result = ""
        for v in root:
            result = "{} -> ".format(vertex[v]) + result
        result += " {:.2f}".format(distance)
        print(result)