'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

'''

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.key = []

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.key.remove(key)
#             self.key.append(key)
#             return self.cache[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key not in self.cache:
#             self.cache[key] = value
#             self.key.append(key)
#         elif key in self.cache:
#             self.cache[key] =  value
#             self.key.remove(key)
#             self.key.append(key)
#             return
        
#         if len(self.key) > self.capacity:
#             del self.cache[self.key.pop(0)]

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key:node}
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left


    def add(self, node):
        previous_node = self.right.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.right
        self.right.prev = node # necessary
    
    def remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    
    def get(self, key):

        if key in self.cache:
            node =  self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        
        return -1 

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            next_node = self.left.next
            self.remove(next_node)
            del self.cache[next_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)