from heapq import heappop, heappush


class Graph(dict):

    def get_node(self, id):
        node = self.get(id)
        if node is None:
            self[id] = node = Node(id)
        return node

    def add_data(self, out, to, distance):
        node = self.get_node(out)
        node.add_edge(to, distance)

    def get_length(self, start, end):
        start, end = self[start], self[end]
        start.score = 0
        vertex = []
        for _id in self:
            heappush(vertex, self[_id])
        while vertex:
            permanent = heappop(vertex)
            if permanent == end:
                break
            for _id, d in permanent.edges:
                self[_id].update_score(permanent.score + d, permanent.id)
        return end.score, reversed(list(self.get_root(end)))

    def get_root(self, node):
        yield node.id
        while node.score != 0:
            node = self[node.prev]
            yield node.id


class Node:

    def __init__(self, id):
        self.id = id
        self.edges = set()
        self.score = float('inf')
        self.prev = None

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def add_edge(self, node, length):
        self.edges.add((node, length))

    def update_score(self, score, prev):
        if score < self.score:
            self.score = score
            self.prev = prev


if __name__ == '__main__':
    graph = Graph()
    with open('input.txt', 'rt') as f:
        for line in f:
            out, to, d = line.strip().split()
            distance = float(d)
            graph.add_data(out, to, distance)
            graph.add_data(to, out, distance)
    length, root = graph.get_length("A", "F")
    print(' -> '.join(root), " -> {}".format(length))
