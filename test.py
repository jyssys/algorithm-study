# 스택 구현하기 by class

class Stack(object):
    def __init__(self, value:list):
        self.list = [value]
        self.idx = 0
    
    def push(self, value = 0):
        if value is None:
            raise Exception("Empty value")
        
        self.list.append(value)
        self.idx += 1
    
    def pop(self, idx = None):
        if idx is None:
            ret_val = self.list[self.idx]
            self.list.pop()
            self.idx -= 1
            
            return ret_val
        
        ret_val = self.list[idx]
        self.list.pop(idx)
        self.idx -= 1
        
        return ret_val
    
    def peek(self, idx = None):
        if idx is None:
            ret_val = self.list[self.idx]
            return ret_val
        
        ret_val = self.list[idx]
        return ret_val
        
    
    def size(self):
        return len(self.list)
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.list) != 0:
            return True
        return False

def palindrome(word:str):
    new_stack = Stack(None) # new_stack = [None]
    new_stack.pop()

    for i in range(int(len(word)/2)): # abcba = 2, abccba = 3
        new_stack.push(word[i]) # new_stack = ['a','b'], i = 1 / new_stack = ['a','b','c'], i = 2
    
    if len(word)%2 > 0: # word의 길이가 홀수일 때 (가운데는 무시해야함)
        i += 1 # i = 2 / i = 2
        
    while not new_stack.is_empty():
        i += 1
        if i > len(word)-1: # 우선 더하기 때문에 string out of range가 발생할 수도 있음.
            break
        if word[i] != new_stack.pop():
            return False
    return True


print(palindrome('bacba'))