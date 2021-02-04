from doctors import *
from config import *

import sys
import psycopg2
import json
import datetime
from airtable import Airtable
from loguru import logger

def insert_to_db(doctors):
    logger.debug("Выгрузка данных в PostgreSQL")
    conn = psycopg2.connect(host=DATABASE_HOST,
                            port=DATABASE_PORT,
                            user=DATABASE_USER,
                            password=DATABASE_PASSWORD,
                            database=DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.airtable(date, data) VALUES(%s, %s)",
                            (datetime.date.today(), json.dumps(doctors))) # А тут мне лично не хватает контатенации из JS
    conn.commit()

    logger.success("Выгрузка в БД завершена!")

    cursor.close()
    conn.close()

def upload_from_airtable():
    logger.debug("Загрузка психотерапевтов из Airtable")
    table = Airtable(AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
    return table.get_all()

def main():
    doctorsData = upload_from_airtable()
    doctors_upload(doctorsData)

if __name__ == "__main__": # так непривычно пользоваться такими if, даже табуляция показалась привычнее =)
    main()