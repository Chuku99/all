import math

def bai1():
    with open('bai1.txt') as filein:
        data = filein.read()
    print(data.upper())

# bai1()

def bai2():
    n = int(input("Nhập độ dài cạnh hv: "))
    dc = n * math.sqrt(2)
    dt = n ** 2 
    with open('bai2.txt', mode='w') as fileout:
        fileout.write(f"Do dai canh hv: {n}\n")
        fileout.write(f"Do dai duong cheo: {dc}\n")
        fileout.write(f"dien tich: {dt}\n")
    print(fileout)
# bai2()

def bai3():
    with open('bai3_input.txt') as filein:
        name = filein.readline().rstrip('\n')
        year = int(filein.readline())

    print("Name: ", name)
    print("Nam sinh: ", year)
    with open('bai3_output.txt', mode = 'w') as fileout:
        fileout.write(f"Nam nay tuoi cua {name} la {2023 - year}")

# bai3()

def bai3_1():
    with open('bai3_1_input.txt') as filein:
        name = filein.readline()
        year = int(filein.readline())
        country = filein.readline()
    print("đọc file")
    with open('bai3_1_output.txt', mode='w') as fileout:
        tuoi = 2023-year
        if tuoi>18:
            fileout.write(f"Chi {name} ngay sinh la {year} co quoc tich la {country} da du tuoi lai xe")
        else:
            fileout.write(f"Chi {name} ngay sinh la {year} co quoc tich la {country} chua du tuoi lai xe")


# bai3_1()

def bai4():
    n = int(input("Nhập n: "))
    with open('bai4.txt', mode='w') as filein:
        for i in range(1,n+1):
            filein.write(f"Day la dong: {i}\n")
# bai4()

def bai5():
    string = input("Nhập chuỗi: ")
    count = 0
    for i in string:
        if i.isupper():
            count += 1
            with open('bai5.txt', mode='w') as fileout:
                fileout.write(f"so luong ki tu in hoa la:{count} ")
        if i.islower():
            with open('bai5.txt', mode='w') as fileout:
                fileout.write("k co ki tu in hoa")
# bai5()

def bai7():
    string = input("Nhập chuỗi: ")
    num_of_space = string.count(' ')
    with open('bai7.txt', mode = 'w') as filein:
        filein.write(f"so ky tu khoang trang la:{num_of_space}\n ")
        if num_of_space%3==0:
            filein.write("so ky tu khoang trang chia het cho 3  ")
        else:
            filein.write("so ky tu khoang trang k chia het cho 3  ")
# bai7()

# def bai8():
    
        
























    











    

