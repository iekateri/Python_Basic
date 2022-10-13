def sum_nums(n):
    list_num = list(str(n))
    summ = 0
    for num in list_num:
        summ += int(num)
    return summ


def count_nums(n):
    list_num = list(str(n))
    return len(list_num)


if __name__ == '__main__':
    N = int(input('Введите число: '))
    a = sum_nums(N)
    b = count_nums(N)
    print(f'Сумма цифр: {a}')
    print(f'Количество цифр в числе: {b}')
    print(f'Разность суммы и количества цифр: {a - b}')
