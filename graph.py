from __future__ import unicode_literals


class Node(object):
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, othernode):
        return self.value == othernode.value


class Edge(object):
    def __init__(self, node1val, node2val):
        if node1val == node2val:  # We may allow this later
            raise ValueError("node1 may not be node2")
        self.node1 = Node(node1val)
        self.node2 = Node(node2val)

    def __eq__(self, otheredge):  # May need to update this when we add weights
        return \
            ((self.node1 == otheredge.node1)
                and (self.node2 == otheredge.node2)) \
            or \
            ((self.node1 == otheredge.node2)
                and (self.node2 == otheredge.node1))


class Graph(object):
    def __init__(self):
        self._node_list = []
        self._edge_list = []

    def add_node(self, nodeval):
        """insert node into the graph"""
        node = Node(nodeval)
        if node not in self._node_list:
            self._node_list.append(node)

    def add_edge(self, node1val, node2val):
        """Insert edge between node1 & node2, add nodes if not present"""
        node1 = Node(node1val)
        node2 = Node(node2val)
        if node1 not in self._node_list:
            self.add_node(node1val)

        if node2 not in self._node_list:
            self.add_node(node2val)

        newedge = Edge(node1val, node2val)
        if newedge not in self._edge_list:
            self._edge_list.append(newedge)

    def nodes(self):
        """Return list of nodes in graph"""
        return [node.value for node in self._node_list]

    def edges(self):
        """Return list of edges in graph"""
        return [(edge.node1.value, edge.node2.value)
                for edge in self._edge_list]

    def del_node(self, nodeval):
        """Delete node from graph, ValueError if not present. Also deletes
        any edges connecting to this node"""
        node = Node(nodeval)
        self._node_list.remove(node)
        for edge in self._edge_list[:]:
            if (node == edge.node1) or (node == edge.node2):
                self._edge_list.remove(edge)

    def del_edge(self, node1val, node2val):
        """Delete the edge between these two nodes.
        ValueError if not present"""
        edge = Edge(node1val, node2val)
        self._edge_list.remove(edge)

    def has_node(self, nodeval):
        """Return True if node in graph, False otherwise"""
        node = Node(nodeval)
        return node in self._node_list

    def neighbors(self, nodeval):
        """Return list of neighbors of node, ValueError if not not in graph"""
        node = Node(nodeval)
        if node not in self._node_list:
            raise ValueError("node must be in graph")
        neigbhor_list = []
        for edge in self._edge_list:  # If we start allowing more than one edge
            if edge.node1 == node:    # between node pairs, revise this
                neigbhor_list.append(edge.node2.value)
            if edge.node2 == node:
                neigbhor_list.append(edge.node1.value)
        return neigbhor_list

    def adjacent(self, node1val, node2val):
        if (not self.has_node(node1val)) or (not self.has_node(node2val)):
            raise ValueError("nodes must be in graph")
        node1 = Node(node1val)
        node2 = Node(node2val)
        for edge in self._edge_list:
            if ((node1 == edge.node1) and (node2 == edge.node2)) or \
               ((node1 == edge.node2) and (node2 == edge.node1)):
                return True
        return False

    def _DFT(self, start_node, path):
        start_node.discovered = True
        path.append(start_node.value)
        for nodeval in self.neighbors(start_node.value):
            neighbor = self._node_list[self.nodes().index(nodeval)]
            if not neighbor.discovered:
                self._DFT(neighbor, path)
                path.append(start_node.value)

    def depth_first_traversal(self, start_nodeval):
        for node in self._node_list:
            node.discovered = False
        start_node = self._node_list[self.nodes().index(start_nodeval)]
        path = []
        self._DFT(start_node, path)
        return path

    def breadth_first_traversal(self, start_nodeval):
        for node in self._node_list:
            node.discovered = False
        start_node = self._node_list[self.nodes().index(start_nodeval)]
        path = []
        from queue import Queue  # My implementation from earlier
        queue = Queue()
        start_node.discovered = True
        queue.enqueue(start_node)
        while True:
            try:
                next_node = queue.dequeue()
            except IndexError:
                break
            path.append(next_node.value)
            for nodeval in self.neighbors(next_node.value):
                neighbor = self._node_list[self.nodes().index(nodeval)]
                if not neighbor.discovered:
                    neighbor.discovered = True
                    queue.enqueue(neighbor)

        return path


if __name__ == '__main__':
    graph = Graph()

    graph.add_edge(1, 2)  # .   1
    graph.add_edge(1, 3)  # . / | \
    graph.add_edge(1, 4)  # .2--3  4
    graph.add_edge(2, 3)  # .|  |
    graph.add_edge(2, 5)  # .5--6
    graph.add_edge(5, 6)
    graph.add_edge(3, 6)

    print graph.depth_first_traversal(3)
    print "Depth first, should have been",\
          [3, 1, 2, 5, 6, 5, 2, 1, 4, 1, 3]
    print graph.breadth_first_traversal(3)
    print "Breadth first, should have been",\
          [3, 1, 2, 6, 4, 5]
