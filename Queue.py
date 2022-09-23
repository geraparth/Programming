import time
import threading

#Queue using a linked list
class Node:

    def __init__(self, data, next):

        self.data = data
        self.next = next

class Queue:

    def __init__(self):

        self.front = None
        self.rear = None

    def size(self):

        if self.front is None:
            return 0

        iterElem = self.front
        lengthCounter = 0

        while iterElem:
            lengthCounter += 1
            iterElem = iterElem.next

        return lengthCounter

    def isEmpty(self):

        return self.size() == 0

    def enqueue(self, data):

        newElement = Node(data, None)
        if self.rear is None:
            self.front = self.rear = newElement
            return

        self.rear.next = newElement
        self.rear = newElement

    def dequeue(self):

        if self.size == 0:
            raise Exception("The queue is empty. No element to delete")

        removeElement = self.front.data
        self.front = self.front.next

        print(removeElement)

        return removeElement

## 1) Using Queue to enqueue and dequeue stock prices data #################
pq = Queue()
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size())
print(pq.dequeue())
print(pq.dequeue())
print(pq.isEmpty())
print(pq.dequeue())
print(pq.isEmpty())

## 2) Using queue to build a Food ordering System for a restaurant #########################
def placeOrder(orderQueue, *orders):

    for newOrder in orders:
        time.sleep(0.5)
        print(f"Order placed for {newOrder}")
        orderQueue.enqueue(newOrder)

def serveOrder(orderQueue):

    time.sleep(2)
    serve = orderQueue.dequeue()
    print(f"Order ready to serve for {serve}")

orderQueue = Queue()

if __name__ == '__main__':

    orders = ['pizza','samosa','pasta','biryani','burger']

    placeThread = threading.Thread(target=placeOrder, args=(orderQueue, *orders))
    serveThread = threading.Thread(target=serveOrder, args=(orderQueue, ))

    placeThread.start()
    time.sleep(1)
    serveThread.start()

    placeThread.join()
    serveThread.join()

## 3)


