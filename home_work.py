#def main(input: str) -> str:
#
#    if len(input) != 3 : raise ValueError("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")    
#
#    b = input[1]
#
#    if b not in "+-*/":
#
#        raise Exception("строка не является математической операцией")
#
#    try:
#        a = int(input[0])
#        if a >= 10:
#            raise ValueError("a >= 10")
#
#        c = int(input[2])
#        if c >= 10:
#            raise ValueError("c >= 10")
#    except ValueError as e:
#        print(f"Ошибка {e}")
#        exit(1)
#
#    if b == "+":
#        b = a + c
#        print(b)
#    elif b == "-":
#        b = a - c
#        print(b)
#    elif b == "*":
#        b = a*c
#        print(b)
#    else:
#        try:
#            b=a // c        
#        except ZeroDivisionError as e:
#            print(f"Ошибка {e}")
#        print(b)
#
#
#
#print(" Это терминальный мини-калькулятор\n  Принцип работы \n    Введите: целое число, символ операции +, -, *, / и еще одно целое число. Числа и символ операции должны быть разделены пробелом")
#
#
#abc = input("Введите 3 символа: ").split(" ")
#
#main(abc)

####################################################################################################################################################################

class Calculator:
#
    """func add input int param and return int"""
    def add(self, a:int, b:int) -> int:
        return a + b
    
    """func multiply input int param and return int"""
    def multiply(self, a:int, b:int) -> int:
        return a * b
    
    """func divide input int param and return int"""
    def divide(self, a:int, b:int) -> int:
        return a // b
    
    """func sub input int param and return int"""
    def sub(self, a:int, b:int) -> int:
        return a - b
    

"""Take 3 simbol from stdin and return processed"""
def input_processor() -> str:
    print(" Это терминальный мини-калькулятор\n  Принцип работы \n    Введите: целое число, символ операции +, -, *, / и еще одно целое число. Числа и символ операции должны быть разделены пробелом")
    abc = input("Введите 3 символа: ").split(" ")

    return abc


def main(input: str) -> str:
    calc = Calculator()
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
        b = calc.add(a,c)
        print(b)

    elif b == "-":
        b = calc.sub(a,c)
        print(b)

    elif b == "*":
        b = calc.multiply(a,c)
        print(b)

    else:
        try:
            b = calc.divide(a,c)
        except ZeroDivisionError as e:
            print(f"Ошибка {e}")
        print(b)

    return str(b)

abc = input_processor()

main(abs)