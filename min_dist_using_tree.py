class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.down = None

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.PreorderTraversal(root.right)
            res = res + self.PreorderTraversal(root.down)
        return res


a = [[1, 1, 2], [2, 3, 1], [2, 2, 1]]
s = a[0][0]
n, m = 3, 3
minimum = 10000

def _main(i, j, minimum, s=0):
    s = s
    
    if (i+1 >= n and j+1 >= m):
        s = s + a[i][j]
        print (s)
        if (minimum > s):
            minimum = s
            
        return Node(a[i][j]), minimum

    if (i >= n):
        return Node(None), minimum

    if (j >= m):
        return Node(None), minimum

    node = Node(a[i][j])
    s = s + a[i][j]
    node.right, minimum = _main(i, j+1, minimum, s)
    node.down, minimum = _main(i+1, j, minimum, s)

    return node, minimum


root, minn = _main(0, 0, minimum)
print (minn)
