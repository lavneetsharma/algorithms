#function to detect Cycle in linked list.
def detectCycle(self):
    slowPointer = self.head
    fastPointer = self.head

    while (slowPointer and fastPointer):
        fastPointer = fastPointer.getNext()

        if fastPointer == slowPointer:
            return True

        if fastPointer == None:
            return False

        fastPointer = fastPointer.getNext()

        if fastPointer == slowPointer:
            return True

            slowPointer = slowPointer.getNext()
