from linked_node import LinkedNode


class OrderedLinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.getData()

            current = current.getNext()

    def __str__(self):
        return "[" + ", ".join([str(i) for i in self]) + "]"

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.getData() > item:
                break

            previous = current
            current = current.getNext()

        temp = LinkedNode(item)

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None:
            if current.getData() == item:
                found = True
                break

            if current.getData() > item:
                break

            current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
                break

            previous = current
            current = current.getNext()

        if not found:
            raise Exception(f'Item {item} not found!')
        else:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
