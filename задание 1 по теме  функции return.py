def city_country(c,t):
    """возвращает словрь с инофрмацией о месте"""
    citis = f"{c}  {t}"
    return citis.title()
countris = city_country('орел', 'россия')
countris2 = city_country('омск', 'россия')
countris3 = city_country('рязань', 'россия')
print(countris)
print(countris2)
print(countris3)
