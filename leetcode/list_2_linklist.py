
class LinkNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def list_2_linklist(arr):
    tem_node = LinkNode()
    node = LinkNode()
    for i in arr:
        if not tem_node.val:
            tem_node.val = i
            node = tem_node
        else:
            tem_node.next = LinkNode(i)
            tem_node = tem_node.next
    return node


# if __name__ == '__main__':
#     array = [1, 2, 3, 4, 5, 6, 7]
#     print(list_2_linklist(array).val)
