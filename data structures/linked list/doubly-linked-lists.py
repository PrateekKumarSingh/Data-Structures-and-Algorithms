class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def getNode(self):
        return "{} -> {}".format(self.data, self.next)


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        print('Doubly Linked List          : Head <-> ',end='')
        pr = None
        while temp:
            print(f'{temp.data} <-> ', sep=' ',end='')
            pr = temp
            temp = temp.next

        print('None')
        print('Reversed Doubly Linked List : None <-> ',end='')
        temp = pr
        while temp:
            print(f'{temp.data} <-> ', sep=' ',end='')
            temp = temp.prev
        print('Head\n')

    def insertAtStart(self,data):

        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertBetween(self,prevNode,data):
        if prevNode.next != None:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next.prev = newNode
            newNode.prev = prevNode
            prevNode.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp


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
                    temp.next.next.prev = prev
                    prev.next = next
                    print('deleted: ',item)
                temp = temp.next

    # search on basis of data
    def search(self,item):
        temp = self.head
        while temp.next != None:
            if temp.data == item:
                print(f'Found: {item}')
                break
            temp = temp.next



ll = DoublyLinkedList()
myNode0 = Node(1)
myNode1 = Node(3)
myNode2 = Node(4)

ll.head = myNode0
ll.head.prev = None
ll.printLinkedList()

ll.head.next = myNode1
ll.head.next.prev = myNode0
ll.printLinkedList()

ll.head.next.next = myNode2
ll.head.next.next.prev = myNode1
ll.printLinkedList()

ll.insertAtEnd(5)
ll.insertAtEnd(6)
ll.printLinkedList()

ll.insertBetween(myNode0,2)
ll.printLinkedList()

ll.search(5)

ll.delete(5)
ll.printLinkedList()

# ll.delete(7)
# ll.printLinkedList()