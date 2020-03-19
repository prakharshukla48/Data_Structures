class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

def precedence(ch):
    if (ch == '+' or ch == '-'):
        prec = 0
    elif (ch == '*' or ch == '/'):
        prec = 1
    elif (ch == '^'):
        prec = 2
    else:
        prec = 10
    return prec

def _main(exp):
    prec = 8
    
    for i in exp:
        if (precedence(i) <= prec):
            op = i
            prec = precedence(i)
    if (prec == 8):
        return Node(exp)
    
    s = exp.rsplit(op, 1)
    left = s[0]
    right = s[1]
    node = Node(op)
    node.left = _main(left)
    node.right = _main(right)
#    if not(prec == 10):
#        _main(left, node.left)
#        _main(right, node.right)

    return node


root = _main('a*b/c+e/f*g+k-x*y')


#while not(root == None):
#    print (root.data)
#    root = root.right
print (root.PreorderTraversal(root))

