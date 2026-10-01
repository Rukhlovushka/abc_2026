# todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
#  нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
app_name    = "?"
version     = "?"
debug       = "?"

# # Настройки базы данных
db_host     = "?"
db_port     = "?"
db_name     = "?"
db_user     = "?"
db_password = "?"

 #  Настройки API
api_key     = "?"
api_secret  = "?"
base_url    = "?"

# Пути
log_file    = "?"
data_dir    = "?"
temp_dir    = "?"


config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
app_name    =  "NextGen"
version     =  '1.0.0'
debug       =  True

# Настройки базы данных
db_host     =  5432


# Словарь с новыми значениями для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    # ... остальные значения из твоего списка
}

with open('config_default.txt', 'r', encoding='utf-8') as template:
    lines = template.readlines()

with open('config.txt', 'w', encoding='utf-8') as config_file:
    for line in lines:
        if '=' in line:
            key = line.split('=')[0].strip()
            if key in config_values:
                new_line = f"{key} = {config_values[key]}\n"
                config_file.write(new_line)
        else:
            config_file.write(line)
            config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
}

with open('config_default.txt', 'r', encoding='utf-8') as template:
    lines = template.readlines()

print("Всего строк в файле:", len(lines))

with open('config.txt', 'w', encoding='utf-8') as config_file:
    for line in lines:
        if '=' in line:
            key = line.strip().split('=')[0].strip()
            print("Найденный ключ в файле:", key)
            if key in config_values:
                new_line = f"{key} = {config_values[key]}\n"
                config_file.write(new_line)
            else:
                print("Ключа нет в словаре:", key)
        else:
            config_file.write(line)

print("нужно проверить файл config.txt в папке ")

