def make_album(albom, name):
    """Возвращает аккуратно отформотированное полное имя"""
    full_name = {'Название альбома': albom, 'Имя исполнителя': name}
    return full_name
while True:
    print("\nПожалуйста,сообщите имя исполнителя:")
    print(" (Введите 'quit',для выхода из программы)")
    namer = input("name:")
    if namer == 'quit':
        break
    albumm = input("albom:")
    if albumm == 'quit':
        break

    new_album = make_album(namer, albumm)
    print(f"\nОбязательно послушаю {new_album}")
    
    
