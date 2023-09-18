# def sum(a,b):
#     tong = a+b
#     return tong
# # sum(1,2)
# tong=sum(1,2)
# print(tong)

# def xinchao(name, tuoi):
#     print("Hello", name, tuoi)
# name = "Truc"
# xinchao("truc", 21)
# xinchao(name="truc", tuoi='21')

#Tich a,b,c cho truoc
# def tich(a,b,c):
#     return a*b*c
# A = tich(1,2,3)
# print(A)

#Tim m lon nhat thoa 1+2+3+...+m<N
# N= int(input("Nhap n: "))
# def tim_m(N):
#     sum=0
#     i=1
#     while sum<N:
#         sum += i
#         i += 1
#     return i-1
# m = tim_m(N)
# print(m)

import math
# #Liet ke cac so chinh phuong <N cho truoc
# #Kiem tra co pahi scp hay k
# n = int(input("nhap n: "))
# def so_chinh_phuong(x):
#     return math.trunc(math.sqrt(x)) == math.sqrt(x)

# #So <N
# def dap_an(N):
#     for i in range(1,n):
#         if so_chinh_phuong(i):
#             print(i)

# def so_nguyen_to(n):
#     f = 1
#     if n<2:
#         f = 0
#         return f
#     for i in range(2,n):
#         if n%i==0:
#             f = 0
#             break
#         return f
# n = int(input("Nhap n: "))
# ketqua = so_nguyen_to(n)
# if ketqua==1:
#     print(n, "la so nguyen to")
# else:
#     print(n, "k phai so nguyen to")


# def giai_thua(n):
#     giai_thua = 1
#     if n == 0 or n ==1:
#         return giai_thua
#     else:
#         for i in range(2, n+1):
#             giai_thua = giai_thua*i
#         return giai_thua
# print(giai_thua(10))

# def max(a,b,c):
#     max  = a
#     if max<b: 
#         max = b
#     if max<c:
#         max  = c
#     return max
# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))
# c = int(input("Nhap c: "))
# print("max la", max(a,b,c))

a = [1,11,23,54,12235]
def tim_so_le(a):
    for i in range(len(a)):
        if a[i]%2!=0:
            return a[i]
    return -1
print(tim_so_le(a))



















    
    

