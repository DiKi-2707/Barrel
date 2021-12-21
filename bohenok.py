import random
import logging
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger()
try:
    n = int(input('Здравствуйте, выберите диапозон для того чтобы вытаскивать бочонки, от 1 до :'))
    if n == 0 or n == 1:
        print("Ошибка")
    print("Нажмите ENTER чтобы вытащить бочонок")
    l = list(range(1, n+1)) #Диапозон
    random.shuffle(l)
    log.info("Создан список со случайным положением чисел от 1 до %s - %s" % (n, l))
    for i in range(len(l)): #Цикл списка
        print(l[i])
        a = input()
    log.info("Бочонки закончились")

except ValueError: #Проверка на ввод символов
    print("Ошибка ввода! Перезапустите программу! Введите натуральное число")
    log.error("Введено не число!")
