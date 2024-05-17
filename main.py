import logging
class Calculation:
    call: str
    num1: int
    num2: int

    def __init__(self, call, num1, num2):
        self.call = call
        self.num1 = num1
        self.num2 = num2


logging.basicConfig(level=logging.DEBUG,
                    filename='logs.txt',
                    filemode='w',
                    format='LOG DATA: %(asctime)s | %(levelname)s | %(message)s')

num1 = input('number1: ')
num2 = input('number2: ')
call = input('ArithmeticOperation: ')
result: float
flag = False

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError as ex:
    flag = True
    logging.exception(ex)
try:
    if call == '+':
        result = num1 + num2
    elif call == '-':
        result = num1 - num2
    elif call == '*':
        result = num1 * num2
    elif call == '/':
        result = num1 / num2
except BaseException as ex:
    flag = True
    logging.exception(ex)
finally:
    if flag:
        print(f'{num1} || {num2} are not digit')
    else:
        print(f'{num1} {call} {num2} = {result}')
