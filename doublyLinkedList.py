class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrev(self, newPrev):
        self.prev = newPrev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def displayList(self):
        current = self.head
        list = []
        while current != None:
            list.append(current.getData())
            current = current.getNext()
        return list

    def addAtBeginning(self, nodeData):
        temp = Node(nodeData)
        if self.head == None:
            print("\n if \n")
            self.head = self.tail = temp
        else:
            print("\n else \n")
            temp.setNext(self.head)
            temp.setPrev(None)
            self.head.setPrev(temp)
            self.head = temp

    def addAtEnd(self, nodeData):
        temp = Node(nodeData)
        if self.tail == None:
            self.head = self.tail = temp
        else:
            temp.setNext(None)
            temp.setPrev(self.tail)
            self.tail.setNext(temp)
            self.tail = temp

    def addInMiddle(self, pos, nodeData):
        if pos == 0:
            self.addAtBeginning(nodeData)
        elif pos == self.length():
            self.addAtEnd(nodeData)
        elif pos > self.length():
            print("cannot add at pos {} as list has only {} elements".format(pos, self.length()))
        else:
            temp = Node(nodeData)
            current = self.head
            count = 0
            while count < pos - 1:
                current = current.getNext()
                count += 1
            temp.setNext(current.getNext())
            temp.setPrev(current)
            current.setNext(temp)
            temp.getNext().setPrev(temp)

    def clear(self):
        self.head = self.tail = None
        print("\nlist cleared.")

    def deleteAtBeginning(self):
        if self.length() == 0:
            print("\nList is empty.")
        elif self.length() == 1:
            print("removed '{}'".format(self.head.getData()))
            self.head = self.tail = None
        else:
            print("removed '{}'".format(self.head.getData()))
            self.head = self.head.getNext()
            self.head.setPrev(None)

    def deleteAtEnd(self):
        if self.length() == 0:
            print("\n List is empty.")
        elif self.length() == 1:
            self.deleteAtBeginning()
        else:
            print("removed '{}'".format(self.tail.getData()))
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

    def deleteWithData(self, data):
        print("deleteWithData")
        if self.head.getData() == data:
            self.deleteAtBeginning()
        elif self.tail.getData() == data:
            self.deleteAtEnd()
        else:
            current = self.head
            found = False
            while not found:
                if current.getData() == data:
                    found = True
                else:
                    current = current.getNext()

            print("data {}".format(data))
            print("current.getData() {}".format(current.getData()))

            print("removed '{}'".format(current.getData()))
            current.getPrev().setNext(current.getNext())
            current.getNext().setPrev(current.getPrev())


obj = DoublyLinkedList()

print("\n")
print("is Empty : {}".format(obj.isEmpty()))
print("length : {}".format(obj.length()))
print("List : {}".format(obj.displayList()))

obj.addAtEnd(3)

print("\n")
print(obj.head)
print(obj.head.getPrev())
print(obj.head.getNext())
print("\n")
print(obj.tail)
print(obj.tail.getPrev())
print(obj.tail.getNext())

print("\n")
print("is Empty : {}".format(obj.isEmpty()))
print("length : {}".format(obj.length()))
print("List : {}".format(obj.displayList()))

obj.addAtEnd(2)

print("\n")
print(obj.head)
print(obj.head.getPrev())
print(obj.head.getNext())
print("\n")
print(obj.tail)
print(obj.tail.getPrev())
print(obj.tail.getNext())

print("\n")
print("is Empty : {}".format(obj.isEmpty()))
print("length : {}".format(obj.length()))
print("List : {}".format(obj.displayList()))

obj.addAtEnd(1)

print("\n")
print(obj.head)
print(obj.head.getPrev())
print(obj.head.getNext())
print("\n")
print(obj.tail)
print(obj.tail.getPrev())
print(obj.tail.getNext())

print("\n")
print("is Empty : {}".format(obj.isEmpty()))
print("length : {}".format(obj.length()))
print("List : {}".format(obj.displayList()))

obj.deleteWithData(2)

print("\n")
print(obj.head)
print(obj.head.getPrev())
print(obj.head.getNext())
print("\n")
print(obj.tail)
print(obj.tail.getPrev())
print(obj.tail.getNext())

print("\n")
print("is Empty : {}".format(obj.isEmpty()))
print("length : {}".format(obj.length()))
print("List : {}".format(obj.displayList()))
