import json
import datetime
import atexit
from db import session, AirtableData, Doctor, db
from loguru import logger

def doctors_load():
    logger.debug("Загружаем последнюю таблицу из PostgreSQL")
    uploaded_data = session.query(AirtableData).order_by('id').first().data
    return uploaded_data
    
def airtable_in_db(doctors):
    logger.debug("Выгрузка сырых данных в PostgreSQL")
    airtable_data = AirtableData(date=datetime.datetime.utcnow(), data=json.dumps(doctors))
    session.add(airtable_data)
    session.commit()

def doctors_upload(doctors):
    logger.debug("Выгрузка данных о врачах в PostgreSQL")
    Doctor.__table__.drop(db)
    Doctor.__table__.create(db)
    for doctor in doctors:
        new_doctor = Doctor(
            name=doctor["fields"]["Имя"],
            methods=doctor["fields"]["Методы"],
            photo=doctor["fields"]["Фотография"][0]["url"]
        )
        session.add(new_doctor)
    session.commit()