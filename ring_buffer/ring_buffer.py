class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity-1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        storage = []

        for item in self.storage:
            if item:
                storage.append(item)
        return storage
