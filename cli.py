from config import *

import sys
from airtable import Airtable
from loguru import logger
import psycopg2

def insert_to_db(doctors):
    logger.debug("Выгрузка данных в PostgresSQL")
    conn = psycopg2.connect(host=DATABASE_HOST,
                            port=DATABASE_PORT,
                            user=DATABASE_USER,
                            password=DATABASE_PASSWORD,
                            database=DATABASE_NAME)
    cursor = conn.cursor()

def upload_from_airtable():
    logger.debug("Загрузка психотерапевтов из Airtable")
    table = Airtable(AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME, sys.argv[1]) # Так делать чрезвычайно плохо =( данные из разных мест это плохо(((
    return table.get_all()

def main():
    doctors = upload_from_airtable()
    insert_to_db(doctors)

if __name__ == "__main__": # так непривычно пользоваться такими if, даже табуляция показалась привычнее =)
    main()