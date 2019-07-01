"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
"""


class LinkNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    node1 = LinkNode(1, 2)
    node2 = LinkNode(2, 4)
    node3 = LinkNode(4)

    node4 = LinkNode(1, 3)
    node5 = LinkNode(3, 4)
    node6 = LinkNode(4)

