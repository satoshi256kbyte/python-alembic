from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import boto3
import json


@contextmanager
def Session():

    # パラメータストアから値を取得
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name='MyAppDBConnection', WithDecryption=True)
    db_connection_dict = json.loads(response['Parameter']['Value'])
    db_host = db_connection_dict['db_host']
    db_port = db_connection_dict['db_port']
    db_user = db_connection_dict['db_username']
    db_pass = db_connection_dict['db_password']
    db_schema = db_connection_dict['db_schema']

    engine = create_engine(
        url=f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_schema}",
        echo=True,
    )
    try:
        session = sessionmaker(bind=engine, autocommit=True, autoflush=True)
        with session() as sess:
            with sess.begin():
                yield sess
    finally:
        engine.dispose()
