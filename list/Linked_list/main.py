from Linked_list import Node, LinkedList
from brower_history import BrowserHistoryList

# Linked List
        
# first = Node(1)
# second = Node(2)
# third = Node(3)

# first.next = second
# second.next = third

# test = LinkedList()
# test.append(1)
# test.append(3)
# test.append(5)
# test.append(7)
# test.insert(0,100)

# for i in range(test.len()):
#     print(test.get(i))

# BrowserHistory

BHS = BrowserHistoryList("leetcode.com")
BHS.visit("google.com")
BHS.visit("facebook.com")
BHS.visit("youtube.com")
print(BHS.back(1))
print(BHS.back(1))
print(BHS.forward(1))
BHS.visit("linkedin.com")
# print(BHS.list)
print(BHS.forward(2))
print(BHS.back(2))
print(BHS.back(7))