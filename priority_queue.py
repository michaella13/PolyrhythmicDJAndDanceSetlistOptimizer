import doubly_linked_list as dll

class PriorityQueue:
    def __init__(self, data=None):
        self.dll = dll.DoublyLinkedList()
        # TODO
        if data is not None:
            for value in data:
                self.push(value)

    def push(self, data):
        # TODO
        self.dll.insert_ordered(data)
    
    
    def pop(self):
        return self.dll.pop(-1)

        
    
    def peek(self):
        # TODO
        return self.dll[-1]
    
    def __str__(self):
        # TODO
        return str(self.dll)
    
    def __bool__(self):
        # TODO
        return bool(self.dll)
    
    def __len__(self):
        # TODO
        return len(self.dll)

