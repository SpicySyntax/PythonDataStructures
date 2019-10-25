class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add_value(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            if self.root == None:
                self.root = Node(val)
            else:
                next = self.root
                while next != None:
                    if val > next.val:
                        if next.right == None:
                            next.right = Node(val)
                            return
                        else:
                            next = next.right
                    else:
                        if next.left == None:
                            next.left = Node(val)
                            return
                        else:
                            next = next.left
    def has_value(self, val) -> bool:
        if self.root == None:
            return False
        else:
            next = self.root
            while next != None:
                if next.val == val:
                    return True
                if val > next.val:
                    next = next.right
                else:
                    next = next.left
            return False


    def print_me(self):
        nodes = [self.root]
        while len(nodes) > 0:
            node = nodes.pop()
            print(node.val)
            if node.right != None:
                nodes.append(node.right)
            if node.left != None:
                nodes.append(node.left)


bst = BinarySearchTree()
bst.add_value(3)
bst.add_value(1)
bst.add_value(2)
bst.add_value(5)
bst.add_value(4)

bst.print_me()


print(bst.has_value(42))
print(bst.has_value(4))
print(bst.has_value(1))