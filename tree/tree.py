from collections import deque

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, value = 0):
        self.root = Node(value = value)
    
    def insert_arr(arr):
        root = Node(arr[0])
        q = deque()
        q.append(root)
        
        idx = 1
        while idx < len(arr):
            cur_node = q.popleft()
            
            # left node
            if arr[idx] != None:
                cur_node.left = Node(arr[idx])
                q.append(cur_node.left)
            idx += 1
            
            # right node
            if arr[idx] != None:
                cur_node.right = Node(arr[idx])
                q.append(cur_node.right)
            idx += 1
        
        return root
    
    def bfs(root):
        # 초기세팅
        visited = []
        if root is None:
            return 0
        
        q = deque()
        q.append(root)
        
        # 트리 선회
        while q:
            cur_node = q.popleft()
            visited.append(cur_node.value)
            
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return visited
    
    def dfs(cur_node):
        if cur_node is None:
            return
        
        BinaryTree.dfs(cur_node.left)
        BinaryTree.dfs(cur_node.right)
        
    def LCA(root, p:int, q:int):
        # root : 모든 노드
        # p, q : search node
        if root == None:
            return None
        
        left = BinaryTree.LCA(root.left, p, q)
        right = BinaryTree.LCA(root.right, p, q)
        
        # root값이 p이거나 q이면 (자기자신도 ancestor가 될 수 있으므로)
        if root.value == p or root.value == q:
            return root.value
        # left, right값이 모두 존재한다면
        elif left and right:
            return root.value
        # left, right값이 하나만 존재하거나 둘다 None값이면
        return left or right
    
    
# new_tree = BinaryTree(3)
root = BinaryTree.insert_arr([3,5,1,6,2,0,8,None,None,7,4])
# print(root)
print(BinaryTree.LCA(root, 6, 4))
