class Node:
    """ Class to define structure of each node"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    """Class to define stack structure"""
    def __init__(self):

        self.top = None

    def getStackLength(self):
        """
        This method computes the length of the linked list

        Inputs:
            self

        Returns:
            lengthCounter: Length of the linked list as an integer
        """

        if self.top is None:
            return 0

        iterElem = self.top
        lengthCounter = 0

        while iterElem:
            lengthCounter += 1
            iterElem = iterElem.next

        return lengthCounter

    def push(self, data):
        """
        Insert an element in the stack

        Inputs:
            data : Element to be inserted

        Returns:
        """

        insertionNode = Node(data, self.top)
        self.top = insertionNode

    def pop(self):
        """
        Delete(pop) an element from the stack. Also display the element removed

        Inputs:
        Returns:
        """

        if self.top is None:
            raise Exception("The stack is empty. No element to remove")

        removeElem = self.top.data
        self.top = self.top.next
        print(removeElem)

        return removeElem

    def peek(self):
        """
        Display the topmost element in the stack
        """

        if self.top is None:
            raise Exception("The stack is empty. No element present")

        print(self.top.data)
        return self.top.data

    def isEmpty(self):
        """
        Return if the stack is empty or not
        """

        if self.top is None:
            return True
        else:
            return False


myStack = Stack()

myStack.push(3)
myStack.push(5)
myStack.push(-10)
print(myStack.pop())


def reverseString(myText):
    """
    Reverse a string using the stack class

    Input:
        myText: String/text of any length

    Returns:
        reverseText :  Reversed string
    """

    textStack = Stack()

    for textChar in myText:
        textStack.push(textChar)

    reverseText = ''

    while not textStack.isEmpty():
        reverseText += textStack.pop()

    return reverseText

print(reverseString("We will conquere COVID-19"))

# In python, we can directly define stack using a list, collections.deque, queue.LifoQueue.
# We'll implement collections.deque below #

from collections import deque

class StackDeque:

    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)