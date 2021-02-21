from .linked_list_abstract import LinkedListAbstract
from .linked_list_node import LinkedListNode


class LinkedListOrdered(LinkedListAbstract):

    def __init__(self):
        super(LinkedListOrdered, self).__init__()

    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.getData() > item:
                break

            previous = current
            current = current.getNext()

        temp = LinkedListNode(item)

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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
