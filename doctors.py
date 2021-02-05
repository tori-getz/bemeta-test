from config import *

import json
import psycopg2
import datetime
from loguru import logger

conn = psycopg2.connect(host=DATABASE_HOST,
                        port=DATABASE_PORT,
                        user=DATABASE_USER,
                        password=DATABASE_PASSWORD,
                        database=DATABASE_NAME)

def load_airtable_data():
    logger.debug("Загружаем последнюю таблицу из PostgreSQL")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + DATABASE_TABLE)
    uploaded_data = cursor.fetchall()
    cursor.close()                           
    return uploaded_data[-1][2]

def doctors_upload(doctors):
    logger.debug("Выгрузка данных в PostgreSQL")
    cursor = conn.cursor()          # Извнияюсь за колхоз ниже, не понял как это еще решать((
    cursor.execute("INSERT INTO " + DATABASE_TABLE + "(date, data) VALUES(%s, %s)",
                            (datetime.date.today(), json.dumps(doctors))) # А тут мне лично не хватает контатенации из JS
    conn.commit()
    logger.success("Выгрузка в БД завершена!")
    cursor.close()

def doctors_list():
    airtable_data = load_airtable_data()
    doctors = []
    for doctor in airtable_data:
        doctors.append(doctor["id"])
    return doctors


def doctors_find_by_id(doctor_id): # Название аргумента, наверное, излишне (для JS уж точно, но мне кажется тут немного другие правила нейминга переменных)                        
    airtable_data = load_airtable_data()                        
    logger.debug("Ищем нужного специалиста")                    #
    for doctor in airtable_data:                                #   Хотел бы сделать этот участок более читаемым =(
        if doctor_id == doctor["id"]:                           #
            logger.success("Специалист найден!")
            return doctor     
    logger.error("Специалист не найден!")