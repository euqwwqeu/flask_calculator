# Импортируем модули
from flask import Flask, render_template, request
import logging
import datetime

# Получаем логгер
logger = logging.getLogger(__name__)

# Создаём хендлер для файла лога
fileHandler = logging.FileHandler(filename='application_log.log', encoding='utf-8')

# Задаём конфигурацию логирования
logging.basicConfig(format='[%(levelname)-10s] %(asctime)-25s - %(message)s', handlers=[fileHandler], level=logging.INFO)
days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
now_dt = datetime.datetime.now()
current_weekday = days[now_dt.weekday()]
date_format = "%d.%m.%Y %H:%M:%S.%f"

# Логируем запуск программы
logging.info(">>> Программа запущена. %s", now_dt.strftime(date_format))

# Создаём инстанс Flask
app = Flask(__name__)

# Обработчик для главной страницы
@app.route('/')
def main():
    return render_template("app.html")

# Обработчик для формы расчета
@app.route("/calculate", methods=['POST'])

def calculate():
    # Получаем числа и операцию из формы
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    # Логируем полученные числа
    logger.info("Первое число: %s, второе число: %s", num1, num2)

    # Проверяем, являются ли введённые числа цифрами
    if num1.isnumeric() and num2.isnumeric():
        logger.info("Пользовательский ввод корректен")

        # Выполняем операцию
        if operation == 'add':
            result = float(num1) + float(num2)
            logger.info("Результат сложения: %s", result)
            return render_template('app.html', result=result)

        elif operation == 'subtract':
            result = float(num1) - float(num2)
            logger.info("Результат вычитания: %s", result)
            return render_template('app.html', result=result)

        elif operation == 'multiply':
            result = float(num1) * float(num2)
            logger.info("Результат умножения: %s", result)
            return render_template('app.html', result=result)

        elif operation == 'divide':
            result = float(num1) / float(num2)
            logger.info("Результат деления: %s", result)
            return render_template('app.html', result=result)
        else:
            return render_template('app.html')
    else:
        # Если пользователь ввёл не число, то логируем ошибку в файл лога и выводим ошибку на консоль
        logger.error("Ошибка ввода: пользователь ввёл нечисловое значение.")