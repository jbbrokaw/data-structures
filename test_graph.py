"""
code that tests the graph class defined in graph.py

can be run with py.test
"""

from __future__ import unicode_literals

import pytest  # used for the exception testing

from graph import Graph
from graph import Node
from graph import Edge
import random


def test_node_initialization():
    """Node should initailize with a single value (None OK) without error"""
    node = Node()
    assert node.value is None

    node = Node(None)
    assert node.value is None

    node = Node("LAX")
    assert node.value == "LAX"

    with pytest.raises(TypeError):
        Node(1, 2, 3)


def test_edge_initialization():
    """Edge initailization requires two node endpoints. The nodes must be
    different."""
    with pytest.raises(TypeError):
        edge = Edge()

    with pytest.raises(TypeError):
        edge = Edge(1)

    edge = Edge(1, 2)
    assert edge.node1 == Node(1)
    assert edge.node2 == Node(2)

    with pytest.raises(ValueError):
        edge = Edge("node1", "node1")  # Must be different


def test_graph_initialization():
    """Graph should initialize without any error"""
    with pytest.raises(TypeError):
        graph = Graph(None)

    with pytest.raises(TypeError):
        graph = Graph(1, 2)

    graph = Graph()
    assert graph._edge_list == []
    assert graph._node_list == []


def test_add_node():
    """g.add_node(n): adds a new node 'n' to the graph"""
    graph = Graph()
    with pytest.raises(TypeError):
        graph.add_node()

    graph.add_node(1)  # Has to be a node

    assert Node(1) in graph._node_list

    graph.add_node(1)
    assert len(graph._node_list) == 1  # Cannot have the same node twice


def test_add_edge():
    """g.add_edge(n1, n2): adds a new edge to the graph connecting n1 and n2,
    if either n1 or n2 are not already present in the graph,
    they should be added."""
    graph = Graph()
    with pytest.raises(TypeError):
        graph.add_edge()
    with pytest.raises(TypeError):
        graph.add_edge(1)

    graph.add_edge(1, 2)

    assert len(graph._edge_list) == 1
    assert Node(1) in graph._node_list
    assert Node(2) in graph._node_list

    assert graph._edge_list[0].node1 == Node(1)
    assert graph._edge_list[0].node2 == Node(2)

    with pytest.raises(ValueError):
        graph.add_edge(1, 1)

    graph.add_edge(1, 2)
    assert len(graph._edge_list) == 1  # Cannot add the same edge twice


def test_nodes():
    """g.nodes(): return a list of all nodes in the graph"""
    graph = Graph()
    assert graph.nodes() == []

    with pytest.raises(TypeError):
        graph.nodes(None)  # No arguments allowed
    with pytest.raises(TypeError):
        graph.nodes([1, 2, 3])  # No arguments allowed

    graph.add_node("node1")
    list_of_nodes = ["node1"]
    assert graph.nodes() == list_of_nodes

    for i in xrange(10):
        val = random.randint(0, 1e8)
        list_of_nodes.append(val)
        graph.add_node(val)

    assert graph.nodes() == list_of_nodes


def test_edges():
    """g.edges(): return a list of all edges in the graph"""
    graph = Graph()
    assert graph.edges() == []

    with pytest.raises(TypeError):
        graph.edges(None)  # No arguments allowed
    with pytest.raises(TypeError):
        graph.edges([1, 2, 3])  # No arguments allowed

    graph.add_edge("node1", "node2")
    list_of_nodes = ["node1", "node2"]
    list_of_edges = [("node1", "node2")]
    assert graph.edges() == list_of_edges
    assert graph.nodes() == list_of_nodes

    for i in xrange(10):
        val1 = random.randint(0, 1e8)
        val2 = random.randint(0, 1e8)
        list_of_nodes.append(val1)
        list_of_nodes.append(val2)
        list_of_edges.append((val1, val2))
        graph.add_edge(val1, val2)

    assert graph.edges() == list_of_edges
    assert graph.nodes() == list_of_nodes


def test_del_node():
    """g.del_node(n): deletes the node 'n' from the graph, raises an error
    if no such node exists"""
    graph = Graph()

    with pytest.raises(TypeError):
        graph.del_node()  # node required

    graph.add_node("node1")
    graph.add_edge("node1", "node2")
    assert len(graph.nodes()) == 2
    assert len(graph.edges()) == 1
    graph.add_node("node3")
    assert len(graph.nodes()) == 3

    graph.del_node("node3")
    assert len(graph.nodes()) == 2
    assert len(graph.edges()) == 1
    with pytest.raises(ValueError):
        graph.del_node("node3")  # This is not in there!

    graph.del_node("node2")

    assert len(graph.nodes()) == 1  # Still have node1
    assert len(graph.edges()) == 0  # The edge should go away, too


def test_del_edge():
    """g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from
    the graph, raises an error if no such edge exists"""

    graph = Graph()

    with pytest.raises(TypeError):
        graph.del_edge()  # edge required

    graph.add_edge("node1", "node2")
    graph.add_edge("node1", "node3")
    graph.add_edge("node2", "node3")  # A triangle
    assert len(graph.nodes()) == 3
    assert len(graph.edges()) == 3

    graph.del_edge("node1", "node2")
    assert len(graph.edges()) == 2

    with pytest.raises(ValueError):  # Now it's not in there
        graph.del_edge("node1", "node2")

    graph.del_edge("node1", "node3")
    assert len(graph.edges()) == 1

    graph.del_edge("node2", "node3")
    assert len(graph.edges()) == 0


def test_has_node():
    """g.has_node(n): True if node 'n' is contained in the graph,
    False if not."""
    graph = Graph()

    with pytest.raises(TypeError):
        graph.has_node()  # node required

    assert not graph.has_node("node1")
    graph.add_node("node1")
    assert graph.has_node("node1")
    graph.add_node("node2")
    assert graph.has_node("node2")
    assert graph.has_node("node1")


def test_neighbors():
    """g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
    raises an error if n is not in g"""
    graph = Graph()

    with pytest.raises(TypeError):
        graph.neighbors()  # node required

    graph.add_edge("node1", "node2")
    graph.add_edge("node1", "node3")
    graph.add_edge("node2", "node3")  # A triangle

    assert "node2" in graph.neighbors("node1")
    assert "node3" in graph.neighbors("node1")

    graph.del_edge("node1", "node2")
    assert "node2" not in graph.neighbors("node1")
    assert "node2" not in graph.neighbors("node1")

    graph.del_edge("node1", "node3")
    assert graph.neighbors("node1") == []
    assert graph.neighbors("node2") == ["node3"]
    assert graph.neighbors("node3") == ["node2"]

    with pytest.raises(ValueError):
        graph.neighbors("node4")


def test_adjacent():
    """g.adjacent(n1, n2): returns True if there is an edge connecting
    n1 and n2, False if not, raises an error if either of the supplied
    nodes are not in g"""
    graph = Graph()

    with pytest.raises(TypeError):
        graph.adjacent()  # nodes required

    graph.add_edge("node1", "node2")
    graph.add_edge("node1", "node3")
    graph.add_edge("node2", "node3")  # A triangle
    graph.add_edge("node3", "node4")  # with node4 dangling off node3

    assert graph.adjacent("node4", "node3")
    assert not graph.adjacent("node4", "node2")
    assert graph.adjacent("node1", "node3")
    assert graph.adjacent("node3", "node2")

    with pytest.raises(ValueError) as err:
        graph.adjacent("node3", "node5")
        assert "must be in graph" in err.value
