def get_input():
    value = input("Enter number: ")
    if not value.isnumeric():
        raise TypeError('You can can use just numbers')
    return float(value)


try:
    while True:
        s = input("Знак (+,-,*,/): ")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
            try:
                x = get_input()
                y = get_input()
            except TypeError as e:
                print(str(e))
                break

            if s == '+':
                print("%s" % (x + y))
            elif s == '-':
                print("%s" % (x - y))
            elif s == '*':
                print("%s" % (x * y))
            elif s == '/':
                try:
                    print(f"{x} / {y}= {x/y}")
                except ZeroDivisionError as e:
                    print(str(e))
        else:
            print("Неверный знак операции!")
except KeyboardInterrupt:
    print("By by!!!")
