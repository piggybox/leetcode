# Leetcode 146
# medium

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # This will maintain the order of keys based on their usage

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end of the order list
            self.cache.move_to_end(key)
            # Return the value associated with the key
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end of the order list
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # Remove the first (least recently used) item
                self.cache.popitem(last=False)
            # Add the new key-value pair to the cache
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)