from .linked_list_abstract import LinkedListAbstract
from .linked_list_node import LinkedListNode


class LinkedListUnordered(LinkedListAbstract):

    def __init__(self):
        super(LinkedListUnordered, self).__init__()
        self.tail = None

    def add(self, item):
        temp = LinkedListNode(item)

        temp.setNext(self.head)
        self.head = temp

        if self.tail is None:
            self.tail = temp

    def append(self, item):
        if self.tail is None:
            self.add(item)
        else:
            temp = LinkedListNode(item)

            self.tail.setNext(temp)
            self.tail = temp

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
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
