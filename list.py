def bai1():
    lst = []
    length = int(input("Input length:  "))
    for i in range(length):
        lst.append(int(input(f"Input list: ")))
    print(lst)
# bai1()

def bai2():
    lst = []
    sum = 0
    length = int(input("Input length:  "))
    for i in range(length):
        lst.append(int(input(f"Input list: ")))
    for s in lst:
        sum += s
    print(sum)
bai2()

def bai3():
    lst = []
    sum = 0
    length = int(input("Input length:  "))
    for i in range(length):
        lst.append(int(input(f"Input list: ")))
    for s in lst:
        sum += s
        tbc = sum/length
    print(tbc)
# bai3()

def bai4():
    lst = []
    index  = 0
    length = int(input("Input length:  "))
    for i in range(length):
        lst.append(int(input(f"Input list: ")))
    for index in lst:
        if index>0:
            print(lst)
bai4()

def bai5():
    lst = []
    index  = 0
    length = int(input("Input length:  "))
    k = int(input("Nhập k: "))

    while True:
        lst.append(int(input(f"Input list: ")))

bai5()

def bai6():
    lst = []
    length = int(input("Input length:  "))
    for i in range(0,len(lst)):
        lst.append(int(input(f"Input list: ")))
    k = int(input("Nhập k: "))
    lst.remove(k)
    print(lst)
bai6()

