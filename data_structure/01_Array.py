# 线性结构——数组和列表，特点：内存连续、可通过下标访问


# 实现一个数组
class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._item = [None] * size

    def __getitem__(self, item):
        return self._item[item]

    def __setitem__(self, key, value):
        self._item[key] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(self._size):
            self._item[i] = value

    def __iter__(self):
        for i in range(self._size):
            yield self._item[i]


if __name__ == '__main__':
    array = Array(10)
    array[0] = 0
    array[1] = 1
    array[2] = 'a'
    assert array[3] == None

    array.clear()
    assert array[2] == None