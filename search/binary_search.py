class BinarySearch:
    def __init__(self, list):
        self.list = list

    def index_of(self, item):
        first = 0
        last = len(self.list) - 1

        while first <= last:
            midpoint = (first + last) // 2

            if self.list[midpoint] == item:
                return midpoint
            else:
                if item < self.list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        return None

    def exists(self, item):
        return self.index_of(item) is not None
