import pandas as pd

# Проверка: создаём DataFrame и печатаем его
df = pd.DataFrame({
    'Имя': ['Анна', 'Борис', 'Виктор'],
    'Возраст': [25, 30, 35]
})

print("Pandas успешно подключён!")
print("Версия:", pd.__version__)
print("\nПример DataFrame:")
print(df)
