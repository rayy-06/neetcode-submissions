class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # key to node. node has all other 
        
        # dummy nodes: head.next is least recent, tail.prev is most recent
        # head <-> [least recent] <-> ... <-> [most recent] <-> tail. head, tail are dummy
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # define methods to remove a node, add a node, to the dll
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node  # node itself gets skipped over
        next_node.prev = prev_node
    
    def add(self, node):
        # insert at the most recent slot by default (right before tail)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # before returning, this is a "use". so remove the associated node and readd it
        # to the most recent position
        node = self.cache[key]
        self.remove(node)   # also, get node from dict. then val from node
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # so the process is fresh each time
        node = Node(key, value)
        self.cache[key] = node  # dict overwriten here anyways, so we didnt need to delete ley explicitly
        self.add(node)
        if len(self.cache) > self.capacity:
            # least recent is self.head.next, grab it
            recent_node = self.head.next
            self.remove(recent_node)    # delete it from dll
            recent_key = recent_node.key    # grab the key, use it to delete from cache
            self.cache.pop(recent_key)
        







"""
from collections import deque   # use append, popleft. this is a FIFO cache not LRU
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.c_dict = {}
        self.c_deque = deque()
        

    def get(self, key: int) -> int:
        if key not in self.c_dict:
            return -1
        return self.c_dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.c_dict:
            self.c_dict[key] = value
        else:
            if len(self.c_dict) + 1 > self.capacity:
                k, v = self.c_deque.popleft()
                self.c_dict.pop(k)
            
            self.c_deque.append((key, value))
            self.c_dict[key] = value
"""
