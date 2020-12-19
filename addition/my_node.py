from binarytree import tree, Node, bst, build


class MyNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)

b = tree(height=3, is_perfect=True)
print(b)

c = Node(7)
c.left = Node(3)
c.right = Node(11)

c.left.left = Node(1)
c.left.right = Node(5)

c.right.left = Node(9)
c.right.right = Node(13)

print(c)

d = build([7, 3, 11, 1, 5, 9, 3])
print(d)
