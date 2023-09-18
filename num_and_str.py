def bai1():
    c = float(input("Nhập độ c: "))
    f = (c*1.8)+32
    print("độ f là: ", f)
# bai1()

def bai2():
    canh = int(input("Nhập cạnh hv: "))
    print("chu vi hình vuông là: ", canh*4)
    print("diện tích là: ", canh*canh)
# bai2()

import math
def bai3():
    x1 = float(input("Nhập x1: "))
    y1 = float(input("Nhập y1: "))
    x2 = float(input("Nhập x2: "))
    y2 = float(input("Nhập y2: "))
    kc = math.sqrt((x1-y1)**2+(x2-y2)**2)
    print(kc)
# bai3()

# def tim_sochinhphuong(n):
#     flag = 0
#     for i in range(1, n+1):
#         if i**2==n:
#             flag = 1
#         return flag

    
# def bai4():
#     n = int(input("Nhập n: "))
#     if n%2==0:
#         print(n, "là số chẵn")
#     else:
#         print(n, "k phải số chẵn")
#     check = tim_sochinhphuong(n)
#     if check == 1:
#         print(n, "là số chính phương")
#     else:
#         print(n, "k là số chính phương")
# bai4()

def bai4():
    n = int(input("Nhập n: "))
    print(n, "là số chẵn", n%2==0)
    print(n, "là số chính phương", math.trunc(math.sqrt(n))==math.sqrt(n))
# bai4()

def bai5():
    name = input("input name: ")
    age = int(input("input age: "))
    print("năm tròn 100 tuổi là ", 2023-age+100)
# bai5()   

def bai6():
    str = input("input string: ")
    char = input("input char: ")
    so_lan_xuat_hien = str.count(char)
    print(f"số lần xuất hiện của {char} là: ", so_lan_xuat_hien)

    print(f"số lần xuất hiện của {char} có >5", so_lan_xuat_hien>5)
# bai6()

def bai7():
    str = "   ---Do youwanna pppe mah bf???///   "
    # print(str.strip().lstrip('-').rstrip('/').replace('youwanna', 'you wanna').replace('ppp','b'))
    print(str.replace("   ---Do youwanna pppe mah bf???///   ","Do you wanna be my bf???"))
# bai7()

def bai8():
    date = input("Nhập date: ")
    ngay = date[0:2]
    thang = date[3:5]
    nam = date[6:]
    print("ngày: ", ngay)
    print("tháng: ", thang)
    print("năm: ", nam)
# bai8()

def bai9():
    year = int(input("input year of birth: "))
    age = 2023-year
    if age>18:
        print("Đã đủ tuổi lái xe")
    else:
        print("chưa đủ tuổi lái xe")
        print("còn",18-age,"năm nữa mới đủ tuổi lái xe")
# bai9()

def bai10():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a>b:
        print("result of a>b is: ", 2*(a-b))
    elif a<b:
        print("result of a<b is: ", b+a**2)
    elif a==b:
        print("2 số bằng nhau")
# bai10()

def bai11():
    month = int(input("Input month: "))
    if month<4:
        print("Spring")
    elif month<7:
        print("Summer")
    elif month<10:
        print("Autumn")
    else:
        print("Winter")
# bai11()

def bai12():
    ds = float(input("Input ds: "))
    if ds<50:
        hh = 3%ds
    elif ds<150:
        hh = 8%ds
    elif ds<400:
        hh = 15%ds
    else:
        hh=25%ds
    print("Hoa hong nhận đc là: ", hh, "triệu")
    if hh>10:
        print("có thể nhập lô hàng giá 10tr")
    else:
        print("k thể")
# bai12()

def bai5():
    n = int(input("Nhập n: "))
    if n%2==0 and n>10:
        print("số chẵn lớn hơn 10")
    elif n%2!=0 and n>10:
        print("số lẻ lớn hơn 10")
    elif n<10:
        print("n là số nguyên âm")
    else:
        print("trường hợp khác")
# bai5()

def bai6():
    string = " BBHeLLo???worLD!***ww "
    print(string.strip().lstrip('B').rstrip('w').rstrip('*').replace('???',' ').title())
# bai6()

def bai7():
    str = input("Input string: ")
    ktr = str.count(' ')
    if ktr%3==0:
        print("số ký tự ktr chia hết cho 3")
    else:
        print("số ký tự ktr k chia hết cho 3")
# bai7()

def bai8():
    x1 = int(input("Nhập x1"))
    y1 = int(input("Nhập y1"))
    print(f"điểm đối xứng qua trục tung là: ", ({-x1}, {y1}))
    print(f"điểm đối xứng qua trục hoành là: ", ({x1}, {-y1}))
    print("khoảng cách là: ", math.sqrt(x1**2 + y1**2))
# bai8()

def bai1():
    for i in range(1,101):
        if i%5==0:
            print(i)
# bai1()

def bai2():
    n = int(input("Nhập n: "))
    while True:
        n = int(input("Nhập n: "))
        if n<0:
            print("Bạn đã nhập số âm")
            break
# bai2()

def bai3():
    n = int(input("Nhập n: "))
    s = 0
    for i in range(1,n+1):
        if n%i==0:
            s += 1
            print(i, f"là ước của n")
            if i%3==0:
                s += 1
    print(s)
# bai3()

def bai4():
    s = 0
    for i in range(1,16):
        if i%2!=0:
            s += i**2
    print(s)
# bai4()

def bai5():
    n = int(input("Nhập n: "))
    s = 0
    for i in range(1,n+1):
        if i%2==0:
            s += i
    print(s)
# bai5()

def bai6():
    n = int(input("Nhập n: "))
    count = 0
    while (n):
        n = n//10
        count += 1
    print(count)
# bai6()

def bai7():
    n = int(input("Nhập n: "))
    for i in range(1, n+1):
        print('*'*i)
# bai7()

def bai9():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a==0:
        if b==0:
            print("pt vô nghiệm")
        else:
            print("pt vô số nghiệm")
    else:
        x = -b/a
    print(x)
# bai9()

def bai10():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    if a*b<0:
        print("2 số khác dấu")
    else:
        print("2 số cùng dấu")
# bai10()

def bai1():
    lst = []
    n = int(input("Nhập chiều dài của list: "))
    for i in range(n):
        lst.append(int(input(f"Nhập lst: ")))
    print(lst)
# bai1()

def bai2():
    lst = []
    sum = 0
    n = int(input("Nhập chiều dài của list: "))
    for i in range(n):
        lst.append(int(input(f"Nhập lst: ")))
    for s in lst:
        sum += s
    print(sum)
# bai2()

# def bai3():





    



        


    




    


