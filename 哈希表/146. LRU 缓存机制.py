class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap={}
        self.capacity=capacity
        self.dummy_head=Node(0,0)
        self.dummy_tail=Node(0,0)
        self.dummy_head.next=self.dummy_tail
        self.dummy_tail.prev=self.dummy_head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.moveTohead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node=self.hashmap[key]
            node.value=value
            self.moveTohead(node)
        else:
            new_node=Node(key,value)
            if len(self.hashmap)<self.capacity:
                self.addToHead(new_node)

                self.hashmap[key]=new_node
            else:
                last_node=self.dummy_tail.prev
                self.removeFromTail()
                self.hashmap.pop(last_node.key)
                self.addToHead(new_node)
                self.hashmap[key]=new_node

    def addToHead(self,node):
        next=self.dummy_head.next
        self.dummy_head.next=node
        node.prev=self.dummy_head
        node.next=next
        next.prev=node
    
    def removeFromTail(self):
        node=self.dummy_tail.prev
        prev=node.prev
        prev.next=self.dummy_tail
        self.dummy_tail.prev=prev
    
    def removeFromMid(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def moveTohead(self,node):
        self.removeFromMid(node)
        self.addToHead(node)

# hashtable + doubly linked list   保证复杂度都为O(1)  {key:node}  node.key  node.value node.next node.prev 用链表维护顺序
# https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/