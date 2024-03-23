def calc(line):
    global value
    global cnt_err
    # print(f'Read line {line}', flush=True)
    operand_1, operation, operand_2 = line.split()
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        cnt_err += 1
        print(f'Неизвестный операнд "{operation}" в строке "{line}"\n'
              f'Номер строки: {cnt}\n')
    return value


total = 0
cnt = 0
cnt_err = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        cnt += 1
        try:
            total += calc(line)
        except ValueError as err:
            cnt_err += 1
            if 'unpack' in err.args[0]:
                print(f'Не хватает операндов {err} в строке "{line}"\n'
                      f'Номер строки: {cnt}\n')
            else:
                print(f'Не могу преобразовать к целому {err} в строке "{line}"\n'
                      f'Номер строки: {cnt}\n')

print(f'Total line: {cnt}')
print(f'Total error: {cnt_err}')
print(f'Total: {total}')
