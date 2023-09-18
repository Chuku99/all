def bai1():
    for i in range(1,101):
        if i%5==0:
            print(i)
# bai1()


def bai2():
    n = int(input("Nhap n:"))
    while True:
        n = int(input("Nhap n:"))
        if n<0:
            print("ban da nhap so am")
            break
# bai2()

    

def bai3():
    n = int(input("nhap n: "))
    s = 0
    for i in range(1, n+1):
        if n%i==0:
            s = s+1
            print(i, f"la uoc cua n")
            if i%3==0:
                s = s+1
    print(s)
# bai3()

def bai4():
    s = 0
    for i in range(1, 16):
        if i%2!=0:
            s += i**2
    print("tong la: ", s)
# bai4()

def bai5():
    n = int(input("nhap n: "))
    s = 0
    for i in range(1, n+1):
        if i%2==0:
            s = s+i
    print("tong la:", s)
# bai5()

def bai6():
    n = int(input("nhap n: "))
    s = 0
    while(n):
        n = n//10
        s += 1
    print(s)
bai6()

def bai7():
    n = int(input("nhap n: "))
    for i in range(1, n+1):
        print('*'*i) #chuoi nhan voi so la lap di lap lai chuoi so lan
# bai7()

def bai8():
    sum = 0
    i = 0
    while sum <= 100:
        i += 1
        sum += i
    print("tong la:", sum)
    print("so hang la: ", i)
# bai8()

def bai9():
    a = float(input("nhap a: "))
    b = float(input("nhap b: "))
    if a==0:
        if b==0:
            print("pt vo so  nghiem")
        else:
            print("pt vo nghiem")
    else:
        x = -b/a
        print("pt co 1 nghiem", x)
# bai9()

def bai10():
    a = float(input("nhap a: "))
    b = float(input("nhap b: "))
    if a*b<0:
        print("2 so trai dau")
    else:
        print("2 so cung dau")
# bai10()

    

    

        




