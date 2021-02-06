from doctors import *
from config import *

import psycopg2 # Когда я прочитал что можно использовать SQLAlchemy было поздно...
import json
from airtable import Airtable
from loguru import logger

def upload_from_airtable():
    logger.debug("Загрузка психотерапевтов из Airtable")
    table = Airtable(AIRTABLE_BASE_KEY, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
    return table.get_all()

def main():
    doctorsData = upload_from_airtable()
    doctors_upload(doctorsData)

if __name__ == "__main__": # так непривычно пользоваться такими if, даже табуляция показалась привычнее =)
    main()