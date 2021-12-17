import random
try:
    n = int(input('Здравствуйте, выберите диапозон для того чтобы вытаскивать бочёнки, от 1 до :'))
    print("Нажмите ENTER чтобы вытащить боченок")
    l = list(range(1, n)) #Диапозон
    random.shuffle(l)
    for i in range(len(l)): #Цикл списка
        print(l[i])
        a = input()
except ValueError: #Проверка на ввод символов
    print("Ошибка ввода! Перезапустите программу! Введите натуральное число")
