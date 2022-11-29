#Диалог с пользователем
print('Привет! Я посчитаю наименьшее количество купюр, которое тебе необходимо')
#подключаем counter
from collections import Counter
#обработка ошибок ввода
while True:
    try:
        money = int(input('Введи сумму в рублях: '))
        break
    except ValueError:
        print('Число должно быть больше 0! Попробуйте еще раз')
#составляем список
list = [64, 32, 16, 8, 4, 2, 1]
ans = []
#работаем со списком
while money>0:
    for i in list:
        if money >= i:
            money -= i
            ans.append(i)
            break

#вывод нового списка
print(f'Понадобится {len(ans)}шт. купюр, а именно:')
print(ans)
#вывод количества используемых купюр при помощи counter
c=Counter(ans)
print('количество каждого элемента', c)




