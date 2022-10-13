if __name__ == '__main__':
    num = int(input('Введите число: '))
    i = 1
    while i <= num:
        i = i + 1
        if num % i == 0:
            print('Наименьший делитель, отличный от единицы:', i)
            break
