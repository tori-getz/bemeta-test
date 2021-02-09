from doctors import airtable_in_db, doctors_upload
from config import AIRTABLE_API_KEY, AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME

import psycopg2 # Когда я прочитал что можно использовать SQLAlchemy было поздно...
import json
from airtable import Airtable
from loguru import logger

def upload_from_airtable():
    logger.debug("Загрузка психотерапевтов из Airtable")
    table = Airtable(AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
    return table.get_all()

def main():
    doctors_data = upload_from_airtable()

    airtable_in_db(doctors_data)
    doctors_upload(doctors_data)

if __name__ == "__main__": # так непривычно пользоваться такими if, даже табуляция показалась привычнее =)
    main()