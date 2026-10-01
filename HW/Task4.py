# todo:
#Заданы три числа в переменных x y z 

x = 10
y = 15
z = 20

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y 
else:
    largest = z
print (f"Наибольшее число: {largest}") # 20