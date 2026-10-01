# todo: 
# 1. Преобразование age и too в число 
# age = "23"
# foo = "23abc"

age_int = "23"
#foo_int = "23abc" # не поулчится преобрзовать, т.к. содержит буквы. 

# 2. Прееобразование переменных age в Boolean 
# age = "123abc"

age = "123abc"
age_bool = bool(age)

#3. Преобрзазовние переменной flag в Boolean 
# flag = 1 

flag = 1 
flag_bool = bool(flag)

#4. Преобразование значение в Boolean 
# str_one = "Privet"
# str_two = ""

str_one = "Privet"
#str_two "" 
bool(str_one)
#bool(str_two) false

#5. Преобразование значения 0 и 1 в Boolean

bool(0) 
bool(1) 

#6. Преобрвазоние False в строку

false_val = False
false_str = str(false_val)
