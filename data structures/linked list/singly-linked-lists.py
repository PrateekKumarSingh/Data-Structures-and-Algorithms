class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getNode(self):
        return "{} -> {}".format(self.data, self.next)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        print('Head -> ',end='')
        while temp:
            print(f'{temp.data} -> ', sep=' ',end='')
            temp = temp.next
        print('None')

    def insertAtStart(self,data):

        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertBetween(self,prevNode,data):
        if prevNode.next != None:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    # # delete on basis of data
    def delete(self, item):

        if self.head == item:
            self.head = None
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data == item:
                    prev = temp
                    next = temp.next.next
                    prev.next = next
                temp = temp.next

    # search on basis of data
    def search(self,item):
        temp = self.head
        while temp.next != None:
            if temp.data == item:
                print(f'Found: {item}')
                break
            else:
                print(f'Not found: {item}')
            temp = temp.next



ll = LinkedList()
ll.head = Node(5)
ll.printLinkedList()

myNode1 = Node(11)
ll.head.next = myNode1
ll.printLinkedList()

myNode2 = Node(12)
ll.head.next.next = myNode2
ll.printLinkedList()

ll.insertAtStart(1)
ll.printLinkedList()

ll.insertAtStart(101)
ll.printLinkedList()

ll.insertAtEnd(7)
ll.insertAtEnd(72)
ll.printLinkedList()

ll.insertBetween(myNode1,15)
ll.printLinkedList()

ll.search(5)

ll.delete(15)
ll.printLinkedList()

ll.delete(7)
ll.printLinkedList()