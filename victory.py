# Годы рожедения:
# Никола Тесла = 1856
# Акрама Кхана = 1974
# Юрий Шевчук = 1957
# Федор Достоевский = 1821
# Винсент ван Гог = 1853

rightAnswers = ['1856', '1974', '1957', '1821', '1853']
names = ["Никоы Тесла", "Акрама Кхана", "Юрия Шевчука", "Федора Достоевскаго", "Винсента ван Гога"]
questionsCount = len(rightAnswers)
rightAnswersCount = 0

i = 0
print("Добро пожаловать на викторину!")
isGoOn = True
while isGoOn:
    print("Попробуйте вспомнить дни рождения следующих 5ти человек.")
    for i in range(len(rightAnswers)):
        if input(f"{i + 1}. Введите год рождения {names[i]}: ") == rightAnswers[i]:
            rightAnswersCount += 1
    rightPercent = rightAnswersCount * 100 / questionsCount
    wrongAnswers = questionsCount - rightAnswersCount
    wrongPercent = wrongAnswers * 100 / questionsCount
    print(f"Вы дали {rightAnswersCount} правильных ответов ({rightPercent}%), допустили {wrongAnswers} ошибок ({wrongPercent})")
    while True:
        restart = input("Хотите повторить? (да/нет): ")
        if restart == "да":
            break
        elif restart == "нет":
            isGoOn = False
            break
print('Было приятно поиграть с вами!')
