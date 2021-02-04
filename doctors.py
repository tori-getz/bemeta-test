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

def doctors_upload(doctors):
    logger.debug("Выгрузка данных в PostgreSQL")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.airtable(date, data) VALUES(%s, %s)",
                            (datetime.date.today(), json.dumps(doctors))) # А тут мне лично не хватает контатенации из JS
    conn.commit()
    logger.success("Выгрузка в БД завершена!")
    cursor.close()

def doctors_find_by_id(doctor_id): # Название аргумента, наверное, излишне (для JS уж точно, но мне кажется тут немного другие правила нейминга переменных)
    logger.debug("Загружаем последнюю таблицу из PostgreSQL")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.airtable REVERSE")
    uploaded_data = cursor.fetchall()                           
    airtable_data = uploaded_data[-1][2]                        
    logger.debug("Ищем нужного специалиста")                    #
    for doctor in airtable_data:                                #   Хотел бы сделать этот участок более читаемым =(
        if doctor_id == doctor["id"]:                           #
            logger.success("Специалист найден!")
            return json.dumps(doctor)            
    logger.error("Специалист не найден!");            