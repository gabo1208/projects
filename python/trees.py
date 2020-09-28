class Node:
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.contains(data)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(data)
            else:
                return False

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()

        print(self.data)

        if self.right:
            self.right.printInOrder()

    def printInReverseOrder(self):
        if self.right:
            self.right.printInReverseOrder()

        print(self.data)

        if self.left:
            self.left.printInReverseOrder()

    def printInPreOrder(self):  # DFS like
        print(self.data)

        if self.left:
            self.left.printInPreOrder()

        if self.right:
            self.right.printInPreOrder()

    def printInPostOrder(self):
        if self.left:
            self.left.printInPostOrder()

        if self.right:
            self.right.printInPostOrder()

        print(self.data)

    def getHeightSums(self, root, height):
        sum = height
        if root.left:
            sum += self.getHeightSums(root.left, height + 1)
        if root.right:
            sum += self.getHeightSums(root.right, height + 1)
        return sum

    def getSubtreesHeightSum(self, root, height):
        sum = height * (height + 1)

        if root.left:
            sum += self.getSubtreesHeightSum(root.left, height + 1)
        if root.right:
            sum += self.getSubtreesHeightSum(root.right, height + 1)
        return sum

    def treeFromInOPreO(self, inorder, preorder):
        indexes = {}
        for i in range(len(inorder)):
            indexes[inorder[i]] = i

        def recTree(i, p, s, e):
            if s >= e:
                return None

            root = Node(p.pop(0))
            root.left = self.recTree(p, i, s, indexes[root.data])
            root.right = self.recTree(p, i, self.indexes[root.data] + 1, e)

            return root

        return recTree(inorder, preorder, 0, len(inorder))

    def treeFromInOPostO(self, inorder, postorder):
        indexes = {}
        for i in range(len(inorder)):
            indexes[inorder[i]] = i

        def recTree(i, p, rI, s, e):
            if s >= e:
                return None

            root = Node(p.pop())
            root.right = self.recTree(p, i, indexes[root.data] + 1, e)
            root.left = self.recTree(p, i, s, indexes[root.data])

            return root

        return recTree(inorder, postorder, 0, len(inorder))

    def ppTree(self, pr, po, s, e, indexes):
        if s > e:
            return None
        print(pr)
        root = Node(pr.pop(0))

        if pr:
            nx = pr[0]

            if indexes[nx] >= s:
                root.left = self.ppTree(pr, po, s, indexes[nx], indexes)
            if indexes[root.data] < e:
                root.right = self.ppTree(
                    pr, po, indexes[nx] + 1, e, indexes)

        return root

    def treeFronPreOPostO(self, preorder, postorder):
        indexes = {}
        for i in range(len(postorder)):
            indexes[postorder[i]] = i

        return self.ppTree(preorder, postorder, 0, len(preorder) - 1, indexes)

    def inorderSucc(self, root, target, mem):
        if not root or (mem[0] and mem[1]):
            return

        self.inorderSucc(root.left, target, mem)

        if root.data == target:
            mem[0] = True
        elif mem[0] and not mem[1]:
            mem[1] = True
            print(root.data)
            return

        self.inorderSucc(root.right, target, mem)

    # def distanceToNode

    # def sumSubtreesValues

    # def sizeOfSubTree


tree = Node(7)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.insert(8)
tree.insert(6)
tree.insert(9)

mem = [False, False]  # (Found, Printed)
tree.inorderSucc(tree, 1, mem)
mem = [False, False]
tree.inorderSucc(tree, 9, mem)
if not mem[1]:
    print('404')
mem = [False, False]
tree.inorderSucc(tree, 4, mem)

'''
         7
      5     8
    2     6   9
 1    4
- -  3
'''
