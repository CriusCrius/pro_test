# 实现一个单链表


# 定义一个节点：节点内容、指向下一个节点
class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# 单链表
class LinkedList(object):
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.root = Node()
        self.tailNode = None
        self.next = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxSize is not None and len(self) > self.maxSize:
            raise Exception("it's full")
        node = Node(value)
        tailnode = self.tailNode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailNode = node
        self.length += 1

    def appendleft(self, value):  # 在根节点的后面添加一个节点
        if self.maxSize is not None and len(self) > self.maxSize:
            raise Exception("it's full")
        node = Node(value)
        if self.tailNode is None:  # 如果是空则在最后加入节点
            self.tailNode = node
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tailNode:
            yield currnode
            currnode = currnode.next
        if currnode is not None:
            yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):  # 删除对应的节点
        prevnode = self.root
        currnode = self.root.next
        while currnode.next is not None:
            if currnode.value == value:
                prevnode.next = currnode.next
                if currnode is self.tailNode:
                    self.tailNode = prevnode
                del currnode
                self.length -= 1
                return 1
            else:
                prevnode = currnode
        return -1

    def find(self, value):  # 找到对应的节点
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):  # 从左边删除一个节点
        if self.root.next is None:
            raise Exception("head node is node")
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        if self.tailNode is headnode:
            self.tailNode = None
        del headnode
        self.length -= 1
        return value  # 将删除的值返回

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


if __name__ == '__main__':
    ll = LinkedList(10)

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.appendleft(0)

    assert len(ll) == 5
    assert ll.find(3) == 3
