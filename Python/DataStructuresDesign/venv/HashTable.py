class HashNode:

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __str__(self):
        if self.deleted:
            return ""
        return str(self.key) + " = " + str(self.value)


class HashTable:

    def __init__(self):
        self.__capacity = 1000003
        self.size = 0
        self.__list = [None] * self.__capacity
        self.__num_doubling_times = 0
        self.__doubled_capacity = \
            self.__capacity * (1 + self.__num_doubling_times)

    def __hash(self, key):
        return (id(key) * 587) % self.__capacity

    def __is_full(self):
        return self.size is self.__doubled_capacity

    def is_empty(self):
        return self.size is 0

    def insert(self, key, value):

        hash_key = idx = self.__hash(key)

        # check if this key is already in the table
        if self.__list[hash_key] is not None and\
                self.__list[hash_key].key is key:

            self.__list[hash_key].value = value
            return

        if self.__is_full():
            self.__num_doubling_times += 1
            self.__list += self.__capacity * [None]
            self.__doubled_capacity += self.__capacity
            idx += self.__num_doubling_times * self.__capacity
            pass

        # Linear probing technique
        while idx is not self.__doubled_capacity and\
                (self.__list[idx] is not None and
                 not self.__list[idx].deleted):

            idx += 1
            pass

        # Rounding around the list to get place in the start of the list
        # if and only if there is no place after the key
        if idx is self.__doubled_capacity:

            # if the list was resized you can start searching
            # for a place starting from the beginning of the new list
            # which is added to the class list in the line 37
            idx = self.__num_doubling_times * self.capacity
            pass

        while idx is not hash_key and self.__list[idx] is not None:
            idx += 1
            pass

        self.__list[idx] = HashNode(key, value)
        self.size += 1

    def find(self, key):

        hash_key = idx = self.__hash(key)
        found = False

        for n in range(self.__num_doubling_times + 1):

            while self.__list[idx].key is not key and\
                    idx is not self.capacity * (1 + n):

                idx += 1
                pass

            if idx is self.__capacity * (1 + n):
                idx = n * self.capacity
                pass

            while idx is not hash_key:
                idx += 1
                pass

            if idx is hash_key:
                found = True
                pass

            if found:
                return self.__list[idx]

            pass

        return None

    def remove(self, key):

        node = self.find(key)

        if node is not None:
            node.deleted = True
            pass

        self.size -= 1

    def get_value(self, key):

        node = self.find(key)

        if node is None or node.deleted:
            return None

        return node.value

    def __str__(self):

        ret = "["

        for node in self.__list:
            if node is not None and not node.deleted:
                ret += str(node) + ", "
                pass
            pass

        ret = ret[:-2] + "]"
        return ret
