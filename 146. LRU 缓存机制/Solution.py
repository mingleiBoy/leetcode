# 146. LRU 缓存机制
# LRU缓存算法：
# https://www.jianshu.com/p/b1ab4a170c3c
#
# 官方题解：
# https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
#
# Labuladong:
# https://leetcode-cn.com/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # 利用伪头部 和 伪尾部
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 未命中，返回-1
        # 有的时候，未命中的时候需要执行 put()， 看要求
        if key not in self.cache:
            return -1

        # 命中后，挪到链表头
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int):
        if key in self.cache:
            # 在缓存中
            # 更新 key 对应的值
            # 节点提到 head
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            # 不在缓存中
            # 新建节点，保存到 cache 中
            # 节点提到 head
            node = Node(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 若 capacity 满了，移除 tail
                # 注意：移除 tail 后记得更新 cache
                tail = self.removeTail()
                self.cache.pop(tail.key)
                self.size -= 1

            return

        return

    # 以下其实都是双向链表的操作，不涉及到 cache
    def moveToHead(self, node: Node):
        self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node: Node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeTail(self) -> Node:
        node = self.tail.pre
        self.removeNode(node)
        return node

    def removeNode(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre
