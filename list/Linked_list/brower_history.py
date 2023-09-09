# doubly Linked list
class ListNode(object):
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        
        
class BrowserHistory(object):
    def __init__(self, homepage:str):
        self.head = self.current = ListNode(value = homepage)
    
    # visit = new node (append)
    def visit(self, url):
        self.current.next = ListNode(value = url, prev = self.current)
        self.current = self.current.next
        return None
    
    def back(self, steps):
        while steps > 0 and self.prev != None:
            self.current = self.current.prev
            steps -= 1
        return self.current.value
            
    def forward(self, steps):
        while steps > 0 and self.next != None:
            self.current = self.current.next
            steps -= 1
        return self.current.value
    
    
# array List
class BrowserHistoryList(object):
    def __init__(self, homepage:str):
        self.list = [homepage]
        self.idx = 0
    
    def visit(self, url):
        if self.idx != len(self.list) - 1:
            for _ in range(len(self.list)-1, self.idx, -1):
                self.list.pop()
            self.list.append(url)
        else:
            self.list.append(url)
        
        self.idx += 1
        
    def back(self, steps):
        if self.idx - steps < 0:
            self.idx = 0
            return self.list[0]
        else:
            self.idx = self.idx - steps
            return self.list[self.idx]
        
    def forward(self, steps):
        if self.idx + steps > len(self.list) - 1:
            self.idx = len(self.list) - 1
            return self.list[self.idx]
        else:
            self.idx = self.idx + steps
            return self.list[self.idx]