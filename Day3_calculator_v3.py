import sys
def calculator(a, b, phep_tinh):
    if(phep_tinh == '+'):
        print(f'{a} + {b} = {a + b}')
    elif(phep_tinh == '-'):
        print(f'{a} - {b} = {a - b}')
    elif(phep_tinh == '*'):
        print(f'{a} * {b} = {a * b}')
    elif(phep_tinh == '/'):
        if(b == 0):
            print('Mau so khong the bang 0')
        else:
            print(f'{a} / {b} = {a / b}')

lich_su_pt = []
thong_ke_pt = {"+":0, "-":0, "*":0, "/":0}
while True:
    try:
        print('Nhap gia tri va phep tinh')
        print('*****So lan dung phep tinh*****')
        for phep, so_lan in thong_ke_pt.items():
            print(f'{phep} : {so_lan}')
        a = int(input(">>>"))
        phep_tinh = input(">>>")
        if phep_tinh not in ['+', '-', '*','/']:
            print('Nhap sai phep tinh! Xin hay nhap lai!!!')
            continue
        thong_ke_pt[phep_tinh] += 1
        b = int(input(">>>"))
        calculator(a, b, phep_tinh)
        kq = calculator(a, b, phep_tinh)
        lich_su_pt.append(f"{a} {phep_tinh} {b} = {kq}")
        print('1 de tiep tuc / 2 de thoat / 3 xem lich')
        while True:
            menu = (input('Chon '))
            match menu:
                case '1':
                    break
                case '2':
                    sys.exit()
                case '3':
                    for item in lich_su_pt:
                        print(item)
                    continue
                case _:
                    print('Khong hop le xin nhap lai')
                    continue
        continue
    except ValueError:
        print('Hay nhap lai')

