def num_calculate(str_number):
    even, ood = [], []
    for i in str_number:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            ood.append(i)
    str_list = "".join([str(len(even)), str(len(ood)), str(len(even) + len(ood))])
    print("str_list  == %s" % str_list)
    return str_list


def BlackHole(str_number):
    i = 0
    number = num_calculate(str_number)
    while 1:
        i += 1
        print('第{}次:{}'.format(i, number))
        number = num_calculate(number)
        if int(number) == 123:
            print('第{}次:{}'.format(i, number))
            break


if __name__ == '__main__':
    BlackHole(input("随意输入一个数字: "))