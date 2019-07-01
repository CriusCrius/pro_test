"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNums(self, l1, l2):
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            r.next = ListNode(1)

        return re.next


def list_2_linklist(arr):
    tem_node = ListNode()
    node = ListNode()
    for i in arr:
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = ListNode(i)
            tem_node = tem_node.next
    return node


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    node1 = list_2_linklist(l1)
    node2 = list_2_linklist(l2)

    solution = Solution()
    print(str(solution.addTwoNums(node1, node2).val) + '->' + str(solution.addTwoNums(node1, node2).next.val) + '->'+ str(solution.addTwoNums(node1, node2).next.next.val))

