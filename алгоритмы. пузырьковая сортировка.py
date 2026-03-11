# пузырьковая сортировка
numbers = [5,3,9,1,6,2123]
n = len(numbers)
trade = 0
for i in range(n):
    for j in range(n - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1],numbers[j]
            trade += 1
print(numbers)
print(trade)
