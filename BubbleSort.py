import random

# target_list = [3, 1, 4, 6, 2, 5, 8, 9, 7]
# tl = [3, 1, 4, 6, 2, 5, 8, 9, 7]
def mp(tl):
    for i in range(0,len(tl)):
        for j in range(0,len(tl)-1-i):
            if tl[j] > tl[j+1]:
                tmp = tl[j + 1]
                tl[j + 1] = tl[j]
                tl[j] = tmp
                print(tl)

def mp_reverse(tl):
    for i in range(0,len(tl)):
        for j in range(0,len(tl)-1-i):
            if tl[j] < tl[j+1]:
                tmp = tl[j + 1]
                tl[j + 1] = tl[j]
                tl[j] = tmp
                print(tl)

while True:
    ins = input('请输入列表中整数的个数：')
    if ins.isdigit():
        number = int(ins)
        tl = [random.randint(1, 30) for _ in range(number)]
        print(tl)
        print('--------开始正冒泡排序--------')
        mp(tl[:])
        print('--------开始逆冒泡排序--------')
        mp_reverse(tl[:])
    else：
