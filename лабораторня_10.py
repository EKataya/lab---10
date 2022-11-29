#Диалог с пользователем
print('Привет! Я посчитаю наименьшее количество купюр, которое тебе необходимо')

from collections import Counter
while True:
    try:
        money = int(input('Введи сумму в рублях: '))
        break
    except ValueError:
        print('Число должно быть больше 0! Попробуйте еще раз')

list = [64, 32, 16, 8, 4, 2, 1]
ans = []

while money>0:
    for i in list:
        if money >= i:
            money -= i
            ans.append(i)
            break


print(f'Понадобится {len(ans)}шт. купюр, а именно:')
print(ans)

c=Counter(ans)
print('количество каждого элемента', c)




