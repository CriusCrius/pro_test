#  卡普雷卡尔数学黑洞


def get_value(i, num):
    num_len = len(num)
    l = list()
    for i in range(num_len):
        # a = num % (10 ** (num_len-i)) // (10 ** (num_len-i-1))  # 获取每一位数字
        a = int(num[i])  # 获取每一位数字
        l.append(a)

    l.sort(reverse=False)  # 升序排序
    min_num = 0
    for i in range(num_len):
        n = l[i] * (10 ** (num_len-i-1))
        min_num += n
    print("min_num == %s" %min_num)
    l.sort(reverse=True)   # 降序
    max_num = 0
    for i in range(num_len):
        n = l[i] * (10 ** (num_len - i - 1))
        max_num += n
    print("max_num == %s" % max_num)
    value = max_num - min_num
    print("value == %s " %value)
    value = str(value)
    if i-1 >= 0:
        print("第%s次值：" %(11-i), get_value(i-1, value))
    return value


if __name__ == '__main__':
    num = input("请输入四位数均不相同的4位数整数：")
    get_value(10, num)
