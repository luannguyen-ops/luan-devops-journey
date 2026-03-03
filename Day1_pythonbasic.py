print("Nhap gia tri va phep tinh")
a = int(input(">>>"))
phep_tinh = input(">>>")
b = int(input(">>>"))
if(phep_tinh == '+'):
    print(f'{a} + {b} = {a + b}')
elif(phep_tinh == '-'):
    print(f'{a} - {b} = {a - b}')
elif(phep_tinh == '*'):
    print(f'{a} * {b} = {a * b}')
elif(phep_tinh == '/'):
    print(f'{a} / {b} = {a / b}')
