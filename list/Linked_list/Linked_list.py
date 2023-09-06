class Node : 
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def len(self): # O(n)
        current = self.head
        cnt = 0
        
        while(current.next):
            current = current.next
            cnt = cnt + 1
        
        return cnt+1
        
            
    def append(self, value): # O(1)
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            # current = self.head
            # while(current.next):
            #     current = current.next    
            # current.next = new_node
    
    def get(self, idx): # O(n)
        if idx < 0:
            raise Exception("out of idx range")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    def insert(self, idx, value): # idx == 0 : O(1) / idx > 0 : O(n)
        insert_node = Node(value)
        
        if idx == 0:
            insert_node.next = self.head
            self.head = insert_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            insert_node.next = current.next
            current.next = insert_node
    
    def remove(self, idx): # idx == 0 : O(1) / idx > 0 : O(n)
        if idx == 0:
            current = self.head
            self.head = current.next
            current.next = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            current.next = current.next.next
            
            # prev = self.head
            # _next = self.head
            # cnt = 0
        
            # for _ in range(idx + 1):
            #     if cnt < idx - 1:
            #         prev = prev.next
            #     _next = _next.next
            #     cnt = cnt + 1
        
            # prev.next = _next
        