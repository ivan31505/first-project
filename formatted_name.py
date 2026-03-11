def get_formatted_name(first_name,middle_name, last_name = ''):
    """Возвращает аккуратно отформотированное полное имя"""
    full_name = f"{first_name}  {middle_name}  {last_name}"
    return full_name.title()
musician = get_formatted_name('иоган', 'себастьян', 'бах')
print(musician)








