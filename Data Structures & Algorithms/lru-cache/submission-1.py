class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.dq = deque()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.dq.remove(key)
        self.dq.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dq.remove(key)
        elif len(self.dq) == self.capacity:
            lru = self.dq.popleft()
            del self.cache[lru]

        self.dq.append(key)
        self.cache[key] = value
