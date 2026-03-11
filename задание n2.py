for i in range(7):
    children1 = int(input('введите свой возраст чтобы я мог пробить вам билет'))
    if children1 < 8:
        print('для вход бесплатный.')
    elif children1 > 12:
        print('заплатите 600 рублей.')
    else:
        print('заплатите 300 рублей')
