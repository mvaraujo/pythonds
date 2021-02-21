class LinkedListAbstract:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current.getData()

            current = current.getNext()

    def __str__(self):
        return "[" + ", ".join([str(i) for i in self]) + "]"

    def __len__(self):
        current = self.head
        cnt = 0

        while current is not None:
            cnt += 1
            current = current.getNext()

        return cnt

    def is_empty(self):
        return self.head is None

    def add(self, item):
        raise NotImplementedError("add not implemented")

    def search(self, item):
        raise NotImplementedError("search not implemented")

    def remove(self, item):
        raise NotImplementedError("remove not implemented")
