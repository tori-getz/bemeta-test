from config import *

import json
import psycopg2
import datetime
import atexit
from loguru import logger

conn = psycopg2.connect(host=DATABASE_HOST,
                        port=DATABASE_PORT,
                        user=DATABASE_USER,
                        password=DATABASE_PASSWORD,
                        database=DATABASE_NAME)

def doctors_load():
    logger.debug("Загружаем последнюю таблицу из PostgreSQL")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + DATABASE_TABLE)
    uploaded_data = cursor.fetchall()
    cursor.close()                           
    return uploaded_data[-1][2]

# Не знаю насколько данное решение подойдет для хайлоада, но здесь я думаю в самый раз.
# И заморачиваться особо не надо =)
def doctors_upload(doctors):
    logger.debug("Выгрузка данных в PostgreSQL")
    cursor = conn.cursor()          # Извнияюсь за колхоз ниже, не понял как это еще решать((
    cursor.execute("INSERT INTO " + DATABASE_TABLE + "(date, data) VALUES(%s, %s)",
                            (datetime.date.today(), json.dumps(doctors))) # А тут мне лично не хватает контатенации из JS
    conn.commit()
    logger.success("Выгрузка в БД завершена!")
    cursor.close()

# Прочитал что так делать хорошо, но не уверен насколько правильно я это делаю
# Не хочу выносить этот момент из doctors.py, т.к. читаемость--
def close_connection():
    conn.close()

atexit.register(close_connection)