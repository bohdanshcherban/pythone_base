# Калькулятор.
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("first number ="))
        y = float(input("second number ="))
        if s == '+':
            print("%s" % (x+y))
        elif s == '-':
            print("%s" % (x-y))
        elif s == '*':
            print("%s" % (x*y))
        elif s == '/':
            if y != 0:
                print("%s" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")

