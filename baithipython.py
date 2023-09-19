def bai1():
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    chuvi = (a+b)*2
    dientich = a*b
    with open('bai1.txt', mode = 'w') as fileout:
        fileout.write(f"{a} {b}\n")
        fileout.write(f"Chu vi:{chuvi}\n")
        fileout.write(f"Dien tich:{dientich}")
# bai1()

def bai2():
    dtb = float(input("Nhap diem trung binh: "))
    if dtb<5:
        print("hoc luc yeu")
    elif dtb<6.5:
        print("hoc luc trung binh")
    elif dtb<8:
        print("hoc luc kha")
    else:
        print("hoc luc gioi")
# bai2()

def bai3():
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))
    if a <= b <= c:
        print("%d %d %d" % (a, b, c))
    elif a <= c <= b:
        print("%d %d %d" % (a, c, b))
    elif b <= a <= c:
        print("%d %d %d" % (b, a, c))
    elif b <= c <= a:
        print("%d %d %d" % (b, c, a))
    elif c <= a <= b:
        print("%d %d %d" % (c, a, b))
    else:  
        print("%d %d %d" % (c, b, a))
# bai3()

def bai4():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            print(i)
# bai4()

def bai5():
    str = input("Nhập chuỗi: ")
    khoang_trang = str.count(' ')
    print(khoang_trang)
# bai5()

def bai6():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    for i in range(1,10):
        if a<b:
            print(a,'x',i,'=',a*i)
        else:
            print(b,'x',i,'=',b*i)
# bai6()

def bai7():
    a = []
    n = int(input("chiều dài danh sách: "))
    sum = 0
    for i in range(n):
        a.append(int(input("Nhập list: ")))
        sum += a[i]
    print(sum)
# bai7()

def bai8():
    n = int(input("Nhập n: "))
    n_str = str(n)
    print(n_str[0])
# bai8()

import re
def bai9():
    str = input("Nhập chuỗi: ")
    num = re.findall(r'\d', str)  
    print(''.join(num))

bai9()

def bai10():
    tra_dao = 30000
    sua_chua = 35000
    tra_xanh = 35000
    ca_phe = 25000
    a = int(input("Nhập số lượng khách mua trà đào cam sả: "))
    b = int(input("Nhập số lượng khách mua sữa chua xoài: "))
    c = int(input("Nhập số lượng khách mua trà xanh đá xay: "))
    d = int(input("Nhập số lượng khách mua cà phê đen: "))
    tongbill = a*tra_dao + b*sua_chua + c*tra_xanh + d*ca_phe
    discount = 0
    if tongbill>250000:
        discount = 0.05*tongbill
    elif tongbill>350000:
        discount = 0.1*tongbill
    print("HÓA ĐƠN THANH TOÁN")
    if a>0:
        print("Trà đào cam sả: ", a*tra_dao)
    if b>0:
        print("Sữa chua xoài: ", b*sua_chua)
    if c>0:
        print("Trà xanh đá xay: ", c*tra_xanh)
    if d>0:
        print("Cà phê đen: ", a*ca_phe)
    print("Tổng tiền: ", tongbill)
    print("Giảm giá: ", discount,'%')
    thanh_toan = tongbill - discount
    print("Số tiền cần thanh toán: ", thanh_toan)

# bai10()