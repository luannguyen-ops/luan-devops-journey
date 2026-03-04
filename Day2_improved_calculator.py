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

print("Nhap gia tri va phep tinh")

while True:
    try:
        a = int(input(">>>"))
        phep_tinh = input(">>>")
        if phep_tinh not in ['+', '-', '*','/']:
            print('Nhap sai phep tinh! Xin hay nhap lai!!!')
            continue
        b = int(input(">>>"))
        calculator(a, b, phep_tinh)
        break
    except ValueError:
        print('Hay nhap lai')

