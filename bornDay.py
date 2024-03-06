#Год рождения Пушкина 1799.06.06

rightYear = '1799'
rightDate = '06.06'

userYear = input("Введите год рождения Пушкина: ")

if userYear == rightYear:
    userDate = input("Введите день рождения Пушкина в формате MM.DD: ")
    if userDate == rightDate: print("Верно!")
    else: print("Неверная дата...")
else: print("Неверный год...")
