import argparse

import gv
from pygraph.readwrite.dot import write
from pygraph.classes.digraph import digraph

from dijkstra_I import get_input, dijkstra


def get_args():
    parser = argparse.ArgumentParser(prog='graph visualization')
    parser.add_argument('-type', default='m', choices=['m', 'g'],
                        help='manual or pygraph')
    parser.add_argument('-file', default='input.txt', help='txt data file')
    parser.add_argument('-out', default='test.png', help='output png file')
    args = parser.parse_args()
    return args


def emit_edge(graph):
    for start, v in graph.items():
        for stop, d in v.items():
            yield start, stop, d


def visualize_with_pygraph(args):
    data, nodes = get_input(args.file)
    graph = digraph()
    graph.add_nodes(nodes)
    for start, stop, distance in emit_edge(data):
        graph.add_edge((start, stop), distance)
    dot = write(graph, weighted=True)
    gvv = gv.readstring(dot)
    gv.layout(gvv, 'dot')
    gv.render(gvv, 'png', args.out)


def visualize_manual(args):
    start, stop = "A", "F"
    graph, nodes = get_input(args.file, directional=True)
    distance, root = dijkstra(graph, nodes, start, stop)
    result = list(root)
    dst, last = [], None
    for v in reversed(result):
        if last:
            dst.append((last, v))
        last = v
    nodes = ''.join(map(lambda x: '\n{}[{}]'.format(x,
                                  'style=filled,fillcolor="#4ebd32"' \
                                  if x in result else ''),
                        nodes))
    edges = ''.join(map(lambda x: '\n{}->{}[weight={d},label={d}{tail}];'.\
                                  format(x[0], x[1], d=x[2],
                                         tail=',color="#4ebd32"'\
                                         if (x[0], x[1]) in dst else ''),
                        emit_edge(graph)))
    dot = 'digraph graphname {{{}{}\n}}\n'.format(nodes, edges)
    gvv = gv.readstring(dot)
    gv.layout(gvv, 'dot')
    gv.render(gvv, 'png', args.out)


if __name__ == "__main__":
    args = get_args()
    if args.type == 'm':
        visualize_manual(args)
    elif args.type == 'g':
        visualize_with_pygraph(args)

