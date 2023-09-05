from Linked_list import Node, LinkedList

# --------------------------------------
        
# first = Node(1)
# second = Node(2)
# third = Node(3)

# first.next = second
# second.next = third

test = LinkedList()
test.append(1)
test.append(3)
test.append(5)
test.append(7)
test.remove(1)

for i in range(test.len()):
    print(test.get(i))