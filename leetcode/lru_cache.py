from collections import deque
import operator

class CacheMostUsed:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.current_count = 0

    def get(self, key: int) -> int:
        if(key in self.store.keys()):
            key_local = self.store[key]
            counter = key_local[1] 
            counter += 1
            self.store[key] = (key_local[0], counter)
            return self.store[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(self.current_count > self.capacity-1):
           #res =  min(self.store.values(), key=lambda x: x[1])
           min_key = next(k for k, v in self.store.items() if v == min(self.store.values(), key=lambda x: x[1]))       
           self.store.pop(min_key[0])
           self.current_count -= 1
        self.store[key] = (value, 0)
        self.current_count += 1
  
class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l
        
    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.next = self.right
        node.prev = last
        self.right.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove from wherever it was in the linked list
            self.insert(self.cache[key]) #insert it into the right end(mru)
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove if already exists
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) #insert as mru
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)       
            del self.cache[lru.key]       

#[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)
lru.put(4,4)
lru.get(3)
lru.get(4)
print(lru.cache)