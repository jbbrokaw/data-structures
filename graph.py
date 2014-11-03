from __future__ import unicode_literals


class Node(object):
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, othernode):
        return self.value == othernode.value


class Edge(object):
    def __init__(self, node1, node2):
        if (not isinstance(node1, Node)) or (not isinstance(node2, Node)):
            raise TypeError("node1 and node2 must be Node instances")
        if node1 is node2:  # We may allow this later
            raise ValueError("node1 may not be node2")
        self.node1 = node1
        self.node2 = node2

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

    def add_node(self, node):
        """insert node into the graph"""
        if not isinstance(node, Node):
            raise TypeError("Only nodes can be added")
        if node not in self._node_list:
            self._node_list.append(node)

    def add_edge(self, node1, node2):
        """Insert edge between node1 & node2, add nodes if not present"""
        if node1 not in self._node_list:
            self.add_node(node1)

        if node2 not in self._node_list:
            self.add_node(node2)

        newedge = Edge(node1, node2)
        if newedge not in self._edge_list:
            self._edge_list.append(newedge)

    def nodes(self):
        """Return list of nodes in graph"""
        return self._node_list

    def edges(self):
        """Return list of edges in graph"""
        return self._edge_list

    def del_node(self, node):
        """Delete node from graph, ValueError if not present. Also deletes
        any edges connecting to this node"""
        if not isinstance(node, Node):
            raise TypeError("node must be a Node instance")
        self._node_list.remove(node)
        for edge in self._edge_list[:]:
            if (node == edge.node1) or (node == edge.node2):
                self._edge_list.remove(edge)

    def del_edge(self, node1, node2):
        """Delete the edge between these two nodes.
        ValueError if not present"""
        if (not isinstance(node1, Node)) or (not isinstance(node2, Node)):
            raise TypeError("nodes must be Node instances")
        edge = Edge(node1, node2)
        self._edge_list.remove(edge)

    def has_node(self, node):
        """Return True if node in graph, False otherwise"""
        if not isinstance(node, Node):
            raise TypeError("node must be a Node instance")
        return node in self._node_list

    def neighbors(self, node):
        """Return list of neighbors of node, ValueError if not not in graph"""
        if not isinstance(node, Node):
            raise TypeError("node must be a Node instance")
        if node not in self._node_list:
            raise ValueError("node must be in graph")
        neigbhor_list = []
        for edge in self._edge_list:  # If we start allowing more than one edge
            if edge.node1 == node:    # between node pairs, revise this
                neigbhor_list.append(edge.node2)
            if edge.node2 == node:
                neigbhor_list.append(edge.node1)
        return neigbhor_list

    def adjacent(self, node1, node2):
        if (not isinstance(node1, Node)) or (not isinstance(node2, Node)):
            raise TypeError("nodes must be Node instances")
        if (not self.has_node(node1)) or (not self.has_node(node2)):
            raise ValueError("nodes must be in graph")
        for edge in self._edge_list:
            if ((node1 == edge.node1) and (node2 == edge.node2)) or \
               ((node1 == edge.node2) and (node2 == edge.node1)):
                return True
        return False
