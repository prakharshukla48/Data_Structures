class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    
    def pop(self):
        a = self.stack.pop()
        return a

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# exp = 'ab*c/ef/g*+k+xy*-'
def _main(exp):
    stack = Stack()
    for i in exp:
        if not(i in ['+', '-', '*', '/', '^']):
            stack.push(Node(i))
        else:
            a = stack.pop()
            b = stack.pop()
            node = Node(i)
            node.left = b
            node.right = a
            stack.push(node)

    return node

root = _main('ab*c/ef/g*+k+xy*-')
print (root.right.data)
print (root.PreorderTraversal(root))
            
