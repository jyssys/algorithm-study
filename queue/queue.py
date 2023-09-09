from collections import deque

# queue는 BFS에 활용
# array list based
queue = []

# eunqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# dequeue() O(n) -> front의 위치를 한칸씩 앞으로 떙겨하므로 해당 과정에서 O(n)이 발생
queue.pop(0)
queue.pop(0)
queue.pop(0)


# dequeue based (linked list)
queue = deque()
# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()