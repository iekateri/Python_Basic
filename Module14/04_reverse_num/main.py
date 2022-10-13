def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]
    return float('.'.join(reversed_parts))


if __name__ == '__main__':
    N = float(input('Введите первое число: '))
    K = float(input('Введите второе число: '))
    print(f'Первое число наоборот: {reverse_float(N)}')
    print(f'Второе число наоборот: {reverse_float(K)}')
    print(f'Сумма: {reverse_float(N)+reverse_float(K)}')
