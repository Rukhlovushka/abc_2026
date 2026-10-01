# todo: База данных пользователя.
# Задан массив объектов пользователя

#users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#         {'login': 'Ivan',  'age': 10, 'group': "guest"},
#         {'login': 'Dasha', 'age': 30, 'group': "master"},
#         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

#тип сортировки: 1

#Затем сообщение для ввода
#Ввидите критерии поиска: 16

#Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"


users = [
        {'login': 'Piter', 'age': 23, 'group': "admin"},
        {'login': 'Ivan',  'age': 10, 'group': "guest"},
        {'login': 'Dasha', 'age': 30, 'group': "master"},
        {'login': 'Fedor', 'age': 13, 'group': "guest"}
         ]
print("Выберите тип поиска :")
print(" 1. По возрасту ")
print(" 2. По первой букве логина ")
print(" 3. По группе ")

choice = input(" Тип сортировки ")

if choice == "1":
    age = int(input (" Введите критерий поиска (возраст) :"))
    result = [user for user in users if user ["age"] > age]
    result.sort(key=lambda user: user["age"])
    
elif choice =="2":
    letter = input (" Введите критерий поиска (первую букву имени) :")
    result = [
        user for user in users
        if user["login"] [0].lower ()== letter
    ]
    result.sort(key=lambda user: user ["login"].lower())
elif choice == "3":
    group = input (" Введите критерий поиска (группу): ").strip().lower()
    result = [
        user for user in users
        if user["group"].lower() == group
    ]
    result.sort(key=lambda user: (user [" пользователь "],user["login"]))
    if result:
        print("\nРезультат:")
        for user in result:
            print(
                f"Пользователь: {user['login']}'"
                f"возраст: {user['age']} года, "
                f"группа: {user['group']}"
            )
else:
    print("\nПодходящие пользователи не найдены.")
