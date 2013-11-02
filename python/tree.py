import struct
import random
import argparse
from itertools import imap
from xml.dom import minidom

import gv


def random_num(n):
    return tuple((random.choice(xrange(256)) for x in xrange(n)))


def get_cheharda(n):
    return ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    for x in range(n)])


def rgb_to_hex(rgb):
    return "#{}".format(struct.pack('BBB',*rgb).encode('hex'))


def create_attr_str(items):
    items.sort(key=lambda x: x[0])
    str_attr = '|'.join(imap(lambda x: x[0], items))
    str_val = '|'.join(imap(lambda x: x[1], items))
    return "{{{}}}|{{{}}}".format(str_attr, str_val)


class XmlTree(object):

    def __init__(self, path, output):
        self.path = path
        self.output = output
        self.nodes = ""
        self.edges = ""
        self.colors = {}

    def visualize(self):
        xmldoc = minidom.parse(self.path)
        self.create(xmldoc.childNodes[0])
        dot = 'digraph graphname {{{}{}\n}}\n'.format(self.nodes, self.edges)
        gvv = gv.readstring(dot)
        gv.layout(gvv, 'dot')
        gv.render(gvv, 'png', self.output)

    def create(self, a):
        node_name = '"' + a.tagName + get_cheharda(3) + '"'
        self.nodes += '\n{}[label="{}", style=filled, fillcolor="{}"]'.format(
                              node_name, a.tagName, self.set_color(a.tagName))
        if a.hasChildNodes():
            for i in a.childNodes:
                if (i.nodeType != 3):
                    child_name = self.create(i)
                    self.edges += '\n{} -> {}'.format(node_name, child_name)
        if a.hasAttributes():
            self.create_attr(node_name, create_attr_str(a.attributes.items()))
        return node_name

    def create_attr(self, a, u):
        attr_name = '"' + get_cheharda(3) + '"'
        self.nodes += '\n{}[label="{}",shape=record]'.format(attr_name, u)
        self.edges += '\n{} -> {}[style=dotted]'.format(a, attr_name)

    def set_color(self, tag_name):
        if not self.colors.has_key(tag_name):
            self.colors[tag_name] = rgb_to_hex(random_num(3))
        return self.colors[tag_name]


if __name__ =="__main__":
    parser = argparse.ArgumentParser(prog='xml tree image')
    parser.add_argument('-file', default='test.xml', help='xml file')
    parser.add_argument('-out', default='test.png', help='output png file')
    args = parser.parse_args()
    XmlTree(args.file, args.out).visualize()

