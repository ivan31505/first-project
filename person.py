def build_person(first_name, last_name, age = None):
    """Возвращает словарь с информацией о человеке"""
    person = {"first":first_name,'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person("иоган", 'бах', age = 300)
print(musician)
