class Node:
    # Constructor for a node with data
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Constructor for an empty list
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # Insert a new node after the given node
    # This is a private method and should not be called directly from outside the class
    def _insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
        self.size += 1
    
    # Remove the given node and return its data
    # This is a private method and should not be called directly from outside the class
    def _pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.data
    
    # Insert after the last node
    def append(self, data):
        self._insert_after(self.tail.prev, data)
  
    # Insert before the node at the given index
    # Valid positions are 0 through len(dll), where len(dll) appends to the end
    # Negative indices count from the end of the list, so -1 inserts before the last node
    # Insertion has one more valid position than indexing (N+1 vs. N),
    # which is why insert walks the list itself rather than using _get_node
    def insert(self, index, data):
        if index < 0:
            # Walk backward from the tail to the node at the index
            node = self.tail
            for _ in range(-index):
                node = node.prev
                if node == self.head:
                    raise IndexError
            self._insert_after(node.prev, data)
        else:
            # Walk forward from the head to the node before the insertion point
            node = self.head
            for _ in range(index):
                node = node.next
                if node == self.tail:
                    raise IndexError
            self._insert_after(node, data)

    # Remove all nodes except head and tail
    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # Return the index of the first node with the given data
    def index(self, data):
        index = 0
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return index
            index += 1
            node = node.next
        return -1
    
    # Return True if the list is not empty
    # Supports the if dll: syntax to check if the list is not empty
    def __bool__(self):
        return self.head.next != self.tail
    
    # Return True if the list contains a node with the given data
    # Supports the syntax:  data in dll
    def __contains__(self, data):
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return True
            node = node.next
        return False

    # Return the number of nodes in the list
    # Supports the syntax:  len(dll)
    def __len__(self):
        return self.size
    
    # Generator that yields the data in each node, from first to last
    # Supports the syntax:  for data in dll:
    # Each call returns a new generator with its own node variable,
    # so separate loops over the same list don't interfere with each other
    def __iter__(self):
        node = self.head.next
        while node != self.tail:
            yield node.data
            node = node.next
    
    # Return a string representation of the list
    # Supports the following syntax to convert a list to a string:  str(dll)
    def __str__(self):
        return ' '.join(str(data) for data in self)
    
    #---- Homework Methods ----#

    # Return the node at the given index
    # Negative indices count from the end of the list, walking backward from the tail
    # Raise an IndexError if the index is out of range
    # This is a private method and should not be called directly from outside the class
    def _get_node(self, index):
        # TODO
        #check valid index first to see if it out of bounds
        if not (index < self.size and index >= -self.size ):
            raise IndexError
        
        if (index >= 0):
            node = self.head.next
            for _ in range(index):
                node = node.next
        elif (index < 0):
            node = self.tail.prev
            for _ in range(-index-1):
                node = node.prev
        
        return node
    # Add a new node in order before the first node with data greater than the given data
    def insert_ordered(self, data):
        # TODO
        node = self.head.next
        for _ in range(self.size):
            if (node.data > data):
                break
            node = node.next
        self._insert_after(node.prev, data)

    # Remove and return the data of the node at the given index
    # Negative indices count from the end of the list
    def pop(self, index):
        # TODO
        return self._pop_node(self._get_node(index))
        

    # Sort the list in ascending order using insertion sort
    def sort(self):
        # TODO
        values = list(self)
        self.clear()
        for value in values:
            self.insert_ordered(value)


    # Return the data of the node at the given index
    # Supports the syntax:  data = dll[index]
    # Negative indices count from the end of the list
    def __getitem__(self, index):
        # TODO
        return self._get_node(index).data

    # Set the data of the node at the given index
    # Supports the syntax:  dll[index] = data
    # Negative indices count from the end of the list
    def __setitem__(self, index, data):
        # TODO
        self._get_node(index).data = data
        
