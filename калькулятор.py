def calculate(expression):
    try:
        # Удаляем пробелы и проверяем, что выражение не пустое
        expression = expression.strip()
        if not expression:
            return "Ошибка: пустое выражение"

        # Поддерживаемые операции
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '**': lambda x, y: x ** y
        }

        # Ищем оператор в выражении
        for op in operators:
            if op in expression:
                # Разделяем строку по оператору
                parts = expression.split(op)
                if len(parts) != 2:
                    return f"Ошибка: некорректное использование оператора '{op}'"

                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                except ValueError:
                    return "Ошибка: в выражении должны быть числа"

                # Выполняем операцию
                if op == '/' and num2 == 0:
                    return "Ошибка: деление на ноль"
                
                result = operators[op](num1, num2)
                
                # Если результат целый, выводим как целое число
                if result.is_integer():
                    return int(result)
                else:
                    return result

        return "Ошибка: неподдерживаемый оператор (используйте +, -, *, /, **)"

    except Exception as e:
        return f"Ошибка: {str(e)}"



# Основной цикл программы
print("Калькулятор (введите 'выход' для завершения)")
while True:
    user_input = input("Введите выражение (например, 5 + 6): ")
    
    if user_input.lower() == 'выход':
        print("До свидания!")
        break
    
    result = calculate(user_input)
    print(f"Результат: {result}")
