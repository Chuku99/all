def bai1():
    a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]
    print(sum)
# bai1()

def bai2():
    a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
    count = 0
    sum = 0
    for i in range(0,len(a)):
        if a[i]>0:
            sum += a[i]
            count += 1
    print("số hạng dương: ",count)
    print("tổng là: ", sum)
# bai2()

def bai3():
    a = [1,2,3,-2]
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]
    print("tbc cả list: ",sum/len(a))
    count = 0
    sum_duong = 0
    for i in range(0,len(a)):
        if a[i]>0:
            count += 1
            sum_duong += a[i]
    print("tbc các số dương: ",sum_duong/count)
# bai3()

def bai4():
    a = [1,2,-3,-2,8]
    index = 0
    while a[index]>=0:
        index += 1
        if index==len(a):
            break
    if index==len(a):
        print('k có pt âm')
    else:
        print(index+1)
# bai4()

n = int(input("Nhập n: "))
for i in range(1,n+1):
    print(f"Đây là dòng {i} ")


