print(" Это терминальный мини-калькулятор\n  Принцип работы \n    Введите: целое число, символ операции +, -, *, / и еще одно целое число. Числа и символ операции должны быть разделены пробелом")

abc = input("Введите 3 символа: ").split(" ")


if len(abc) != 3 : raise ValueError("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")    

b = abc[1]

if b not in "+-*/":

    raise Exception("строка не является математической операцией")

try:
    a = int(abc[0])
    if a >= 10:
        raise ValueError("a >= 10")
    
    c = int(abc[2])
    if c >= 10:
        raise ValueError("c >= 10")
except ValueError as e:
    print(f"Ошибка {e}")
    exit(1)

if b == "+":
    b = a+c
    print(b)
elif b == "-":
    b = a-c
    print(b)
elif b == "*":
    b=a*c
    print(b)
else:
    try:
        b=a/c        
    except ZeroDivisionError as e:
        print(f"Ошибка {e}")
    print(b)



