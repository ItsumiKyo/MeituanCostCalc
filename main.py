# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

def calc():
    order_fee = float(input("原价（元）："))
    pack_fee = float(input("打包费（元）："))
    distance = float(input("距离（千米）："))
    dis_fee = 2.9
    if distance > 3:
        dis_fee += (distance - 3) * 1.1
    #省/不省打包费 省/不省配送费
    base1 = base_calc(order_fee) + dis_fee #都不省
    base2 = base_calc(order_fee - pack_fee) + dis_fee #省打包
    base3 = base_calc(order_fee - dis_fee) + dis_fee #省配送
    base4 = base_calc(order_fee - pack_fee - dis_fee) + dis_fee #省打包+配送
    sum1 = base1 + (order_fee + pack_fee + dis_fee) * 0.064 if (order_fee + pack_fee + dis_fee) * 0.064 > 1.04 else 1.04
    sum2 = base2 + (order_fee + dis_fee) * 0.064 if (order_fee + dis_fee) * 0.064 > 1.04 else 1.04
    sum3 = base3 + (order_fee + pack_fee) * 0.064 if (order_fee + pack_fee) * 0.064 > 1.04 else 1.04
    sum4 = base4 + (order_fee) * 0.064 if (order_fee) * 0.064 > 1.04 else 1.04
    min = sum1
    flag = 0
    index = 0
    for i in [sum2, sum3, sum4]:
        if min > i:
            min = i
            flag = index + 1
        index += 1
    if flag == 1:
        print("都不省抽成最少，抽成：" + str(min) + "元")
    elif flag == 2:
        print("省打包抽成最少，抽成：" + str(min) + "元")
    elif flag == 3:
        print("省配送抽成最少，抽成：" + str(min) + "元")
    elif flag == 4:
        print("省打包+配送抽成最少，抽成：" + str(min) + "元")
def base_calc(base):
    if base <= 20:
        return 0
    elif base <= 30:
        return (base - 20) * 0.17
    elif base <= 50:
        return (base - 30) * 0.16
    else:
        return (base - 50) * 0.15

if __name__ == '__main__':
    calc()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
