def get_formatted_name(first_name,last_name, middle_name = ''):
    """Возвращает аккуратно отформотированное полное имя"""
    full_name =f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\пожалуйста сообщите мне свое имя:")
    print("(Введите 'quit',для выхода из программы)")
    f_name = input("Имя:")
    if f_name == 'quit':
        break
    l_name = input("Фамилия:")
    if l_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nпривет, {formatted_name}")
