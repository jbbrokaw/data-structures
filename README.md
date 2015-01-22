Data Structures
=====

![Travis status](https://travis-ci.org/jbbrokaw/data-structures.svg?branch=master "Travis status")


## Simple implementations of data structures:
  1. Stacks
    * Full unit test coverage including errors
    * Implements push & pop
    * No collaborators, some reference to Wikipedia VDM definition
  2. Linked list
    * Full unit test coverage including errors
    * Implements insert, pop, size, search, remove, print
    * No collaborators, some reference to Wikipedia VDM definition
  3. Doubly linked list
    * Inherits from linked list, which gave me the very useful search() method,
      but was otherwise confusing.
    * Doubly linked lists are more useful when you need to use both ends (like a queue, see below)
  4. Queue
    * Basically reimplements doubly linked list
    * Only methods are queue(), enqueue(), and size
    * Directions are back  <-  [next, value, previous] -> front (i.e., the person at the front of the line calls "NEXT" to get the next customer)
  5. Binary heap
    * Either maximum heap or minimum heap, depending on contructor (defaults to maximum)
    * Only has push & pop methods (which include the rebuilding necessary)
    * A few little helper functions are in there
  6. Priority Queue
    * Reuses binary heap, but only takes tuples of (priority, value)
    * Only returns value
  7. Binary Search Tree
    * Has insert(val), contains(val), size(), depth(), and balance() (a representation of the left - right balance)
    * Now has delete(), which tries to maintain good balance
    * running get_dot() will return a string for importing into graphviz (save as .dot file)
    * A test.dot will be saved automatically if bst.py is run (if __name__ == "__main__")
    * Has four traversal methods that return generators (in-order, post-order, pre-order, & breadth_first)
    * Has a naive rebalancing method that just deletes & re-inserts unbalanced nodes until the tree is balanced
    * All functions tested with pytest
  8. Simple Graph
    * A basic graph with nodes & edges
    * graph.nodes(): returns a list of all nodes in the graph
    * graph.edges(): returns a list of all edges in the graph
    * graph.add_node(n): adds a new node 'n' to the graph
    * graph.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.
    * graph.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists
    * graph.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists
    * graph.has_node(n): True if node 'n' is contained in the graph, False if not.
    * graph.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g
    * graph.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
    * g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
    * g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.
    * g.dijkstra(start, end): Return the distance and shortest path from start node to end node
    * g.astar_distance(start, end): Given coordinates on the nodes, uses the A* algorithm to heuristically pick what is likely the best path (in the direction toward the end node); otherwise identical to dijkstra. This is obviously useful when arriving at a good solution faster is desired; the exhaustive search is actually slower because of the distance calculation overhead.
  9. Hash Table
    * Uses a fairly simple rotating hash function
    * Buckets are used in each address to handle collisions
    * Only strings can be used as keys
    * get(key) returns the value stored with the given key
    * set(key, val) stores the given val using the given key
    * hash(key) hashes the key provided
  10. AVL Tree
    * Binary search tree which incorporates the AVL rebalancing algorith on insertion and deletion
  11. Red-Black Tree
    * Binary search tree which incorporates the red-black rebalancing algorithm on insertion


## Algorithms:
  1. parse_parentheses(text)
    * Counts parentheses in text, decides if all opened ones are closed or if anything is broken
    * Returns 1 if more open, -1 if closes unopened ones, 0 if all opens are closed
    * Tests provided
  2. Insertion Sort
    * Terribly performing, very simple in-place sort of a standard python list
