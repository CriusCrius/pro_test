a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test():
    for i in a:
        yield i
        print("i == ", i)
    print("-----end -------")


if __name__ == '__main__':
    t = test()
    print(t.__next__())
    print(t.__next__())
    # print(t.__next__())
