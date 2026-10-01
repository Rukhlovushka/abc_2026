# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах

number = int(input("введите номер единицы массы : "))
mass = float(input("ввeдите массу : "))

mass_in_kg = 0

if number == 1:
    mass_in_kg == mass
elif number == 2:
    mass_in_kg == mass / 1000000
elif number == 3:
     mass_in_kg == mass / 1000
elif number == 4:
     mass_in_kg == mass * 1000
elif number == 5:
     mass_in_kg = mass * 100
else:
    print("Ошибка" )
    mass_in_kg = None

if mass_in_kg is not None:
    print("Масса  в килограммах ",  mass_in_kg )