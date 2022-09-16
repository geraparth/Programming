class Node:
    """Class to define structure of each node of the linked list"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):

        self.head = None

    def getLength(self):
        """
        This method computes the length of the linked list

        Inputs:
            self

        Returns:
            lengthCounter: Length of the linked list as an integer
        """

        if self.head is None:
            return 0

        lengthCounter = 0
        iterElem = self.head

        while iterElem:
            iterElem = iterElem.next
            lengthCounter += 1

        return lengthCounter

    def insertBeginning(self, data):
        """
        Insert an element (provided by user) at the beginning of the linked list

        Inputs:
            data : Element to be inserted

        Returns:
        """

        insertionNode = Node(data, self.head)
        self.head = insertionNode

    def insertEnd(self, data):
        """
        Insert an element (provided by user) at the end of the linked list

        Inputs:
            data : Element to be inserted

        Returns:
        """

        if self.head is None:
            self.head = Node(data, None)
            return

        iterElem = self.head

        while iterElem.next:
            iterElem = iterElem.next

        insertionNode = Node(data, iterElem.next)
        iterElem.next = insertionNode

    def insertAny(self, data, insertIndex):
        """
        Insert an element (provided by user) at the index provided by the user

        Inputs:
            data : Element to be inserted
            insertIndex : Index from the start at which the element is to be inserted

        Returns:
        """

        if insertIndex == 0:
            self.insertBeginning(data)
            return

        if insertIndex == self.getLength():
            self.insertEnd(data)
            return

        if insertIndex > self.getLength():
            print("Insertion index is more than the length of the list")
            return

        iterElem = self.head
        for i in range(insertIndex - 1):
            iterElem = iterElem.next

        insertionNode = Node(data, iterElem.next)
        iterElem.next = insertionNode

    def insertAfterValue(self, data, insertAfter):
        """
        Insert an element (provided by user) after a particular value provided by the user

        Inputs:
            data : Element to be inserted
            insertAfter : Value after which the new element is to be inserted

        Returns:
        """

        if self.head is None:
            print("The list is empty. Element not found")
            return

        iterElem = self.head

        for i in range(self.getLength()):

            if iterElem.data == insertAfter:
                self.insertAny(data, i+1)
                return

            iterElem = iterElem.next

        print(f"The element: {insertAfter} is not present in the linked list")

    def deleteBeginning(self):
        """
        Delete the element at the start of the linked list

        Inputs:
            self
        Returns:
        """

        if self.head is None:
            print("Linked List is empty. There is no element to delete")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next

    def deleteEnd(self):
        """
        Delete the element at the end of the linked list

        Inputs:
            self

        Returns:
        """

        if self.head is None:
            print("Linked List is empty. There is no element to delete")
            return

        if self.getLength() == 1:
            self.head = None
            return

        iterElem = self.head

        for i in range(self.getLength() - 2):
            iterElem = iterElem.next

        iterElem.next = None

    def deleteAny(self, deleteIndex):
        """
        Delete an element present at the index provided by the user

        Inputs:
            deleteIndex : Index at which the element is to be deleted
        Returns:
        """

        if self.head is None:
            print("Linked List is empty. There is no element to delete")
            return

        if deleteIndex == 0:
            self.deleteBeginning()
            return

        if deleteIndex == (self.getLength() - 1):
            self.deleteEnd()
            return

        if deleteIndex > (self.getLength() - 1):
            print("The deletion index is greater than the length")
            return

        iterElem = self.head

        for i in range(deleteIndex - 1):
            iterElem = iterElem.next

        iterElem.next = iterElem.next.next

    def deleteByValue(self, deleteData):

        if self.head is None:
            print("Linked List is empty. There is no element to delete")
            return

        iterElem = self.head
        for i in range(self.getLength()):

            if iterElem.data == deleteData:

                self.deleteAny(i)
                return

            iterElem = iterElem.next

        print(f"The linked list doesn't have {deleteData}")

    def printList(self):
        """
        Print the linked list
        """

        if self.head is None:
            print("Linked List is empty")
            return

        iterElem = self.head
        elementList = []

        while iterElem:
            elementList.append(iterElem.data)
            iterElem = iterElem.next

        print(elementList)


# l1 = LinkedList()
# l1.insertBeginning(25)
# l1.insertBeginning(45)
# l1.insertBeginning(60)
# l1.insertBeginning(60)
# l1.insertBeginning(10)
# l1.insertBeginning(45)
# l1.insertAny(0, 1)
# l1.deleteAny(0)
# l1.deleteEnd()
# l1.insertEnd(25)
# l1.insertAfterValue(-10, 60)
# l1.printList()
# l1.deleteByValue(-10)
# l1.printList()
ll = LinkedList()
ll.insertEnd("banana")
ll.insertEnd("mango")
ll.insertEnd("grapes")
ll.insertEnd("orange")
ll.printList()
ll.insertAfterValue("apple", "mango") # insert apple after mango
ll.printList()
ll.deleteByValue("orange") # remove orange from linked list
ll.printList()
ll.deleteByValue("figs")
ll.printList()
ll.deleteByValue("banana")
ll.deleteByValue("mango")
ll.deleteByValue("apple")
ll.deleteByValue("grapes")
ll.printList()
