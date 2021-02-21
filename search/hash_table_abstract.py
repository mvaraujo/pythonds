class HashTableAbstract:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value)

                while self.slots[next_slot] is not None and \
                        self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hashfunction(key)

        data = None
        position = start_slot

        while self.slots[position] is not None:
            if self.slots[position] == key:
                data = self.data[position]
                break

            position = self.rehash(position)

            if position == start_slot:
                break

        return data

    @staticmethod
    def string_ordinal_values(str_key, size):
        ordinal_sum = 0

        for c in str_key:
            ordinal_sum += ord(c)

        return ordinal_sum % size