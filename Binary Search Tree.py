class BinaryTreeNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):

        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTreeNode(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTreeNode(data)

    def inOrderTraversal(self):

        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def preOrderTraversal(self):

        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.inOrderTraversal()

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def postOrderTraversal(self):

        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        if self.right:
            elements += self.right.inOrderTraversal()

        elements.append(self.data)

        return elements


    def search(self, element):

        if self.data == element:
            return True

        if element < self.data:
            if self.left:
                return self.left.search(element)
            else:
                return False

        if element > self.data:
            if self.right:
                return self.right.search(element)
            else:
                return False

    def deleteNode(self, deleteElement):

        if self.data == deleteElement:
            if (not self.left) and (not self.right):
                return None
            elif self.left:
                return self.left
                # temp = self.left.findMax()
                # self.data = temp
                # self.left.deleteNode(temp)
            elif self.right:
                return self.right
                # temp = self.right.findMin()
                # self.data = temp
                # self.right.deleteNode(temp)

            temp = self.right.findMin()
            self.data = temp
            self.right = self.right.deleteNode(temp)

        elif deleteElement < self.data:
            if self.left:
                self.left = self.left.deleteNode(deleteElement)
            else:
                raise Exception(f"Element {deleteElement} is not present in the tree")

        else:
            if self.right:
                self.right = self.right.deleteNode(deleteElement)
            else:
                raise Exception(f"Element {deleteElement} is not present in the tree")

        return self

    def findMax(self):

        if self.right:
            return self.right.findMax()
        else:
            return self.data

    def findMin(self):

        if self.left:
            return self.left.findMin()
        else:
            return self.data

    def getSum(self):

        return sum(self.inOrderTraversal())

def buildBST(elements):

    root = BinaryTreeNode(elements[0])

    for elem in elements[1:]:
        root.addChild(elem)

    return root

if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbersTree = buildBST(numbers)
    print(numbersTree.inOrderTraversal())
    numbersTree.deleteNode(20)
    print(numbersTree.inOrderTraversal())

