Data Structures
=====

## Simple implementations of:
  1. stacks
    * Full unit test coverage including errors
    * Implements push & pop
    * No collaborators, some reference to Wikipedia VDM definition
  2. linked list
    * Full unit test coverage including errors
    * Implements insert, pop, size, search, remove, print
    * No collaborators, some reference to Wikipedia VDM definition
  3. parse_parentheses(text)
    * Counts parentheses in text, decides if all opened ones are closed or if anything is broken
    * Returns 1 if more open, -1 if closes unopened ones, 0 if all opens are closed
    * Tests provided
  4. Doubly linked list
    * Inherits from linked list, which gave me the very useful search() method,
      but was otherwise confusing.
    * Doubly linked lists are more useful when you need to use both ends (like a queue, see below)
  5. Queue
    * Basically reimplements doubly linked list
    * Only methods are queue(), enqueue(), and size
    * Directions are back  <-  [next, value, previous] -> front (i.e., the person at the front of the line calls "NEXT" to get the next customer)
  6. Binary heap
    * Either maximum heap or minimum heap, depending on contructor (defaults to maximum)
    * Only has push & pop methods (which include the rebuilding necessary)
    * A few little helper functions are in there
  7. Priority Queue
    * Reuses binary heap, but only takes tuples of (priority, value)
    * Only returns value
  8. Binary Search Tree
    * Has insert(val), contains(val), size(), depth(), and balance() (a representation of the left - right balance)
    * Now has delete()
    * running get_dot() will return a string for importing into graphviz (save as .dot file)
    * All funcitons tested with pytest
