# (МОДУЛЬ 3) В проекте создать новый модуль bornday.py
# Написать программу или модернизировать предыдущую используя условные операторы:
# Спросить у пользователя год рождения А.С. Пушкина
# Если пользователь ввел верный год спросить у него день рождения
# Если день рождения введен верно вывести 'Верно'
# Если день рождения введен неверно вывести 'Неверный день рождения'
# Если неверно введен год, то сразу вывести 'Неверный год
# рождения', а день рождения не спрашивать

bornyear = int(input('Введите год рождения А.С. Пушкина:'))
if bornyear == 1799:
    bornday = float(input('Введите день рождения А.С. Пушкина (дд.мм):'))
    if bornday == 06.06:
        print('Верно')
    else:
        print("Неверный день рождения")
else:
     print("Неверный год рождения")