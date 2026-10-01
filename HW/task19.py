#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#             "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

with open('algoritm.csv', 'w', encoding='utf-8') as file:
    for index, value in enumerate(algoritm, start=1):
        line = f"{index}) {value}\n"
        file.write(line)
with open('algoritm.csv', 'r', encoding='utf-8') as file:
    # Читаем все строки из файла в список
    lines = file.readlines()
    
for line in lines:
    print(line.strip())  # strip() убирает лишний пробел или перенос строки в конце

        