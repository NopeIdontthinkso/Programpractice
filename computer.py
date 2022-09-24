while True:
    order = str(input())
    if order == 'end':
        break
    elif order == '+':
        a = float(input())
        b = float(input())
        print(a + b)
    elif order == '-':
        a = float(input())
        b = float(input())
        print(a - b)
    elif order == '*':
        a = float(input())
        b = float(input())
        print(a * b)
    elif order == '/':
        a = float(input())
        b = float(input())
        print(a / b)
    else:
        print('Error')