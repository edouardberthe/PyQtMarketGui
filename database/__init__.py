from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config
from .mapping import *
from .metadata import metadata

engine = create_engine('{:s}://{:s}:{:s}@{:s}:{:d}/{:s}'.format(
    config['db_pdo'],
    config['db_user'],
    config['db_password'],
    config['db_host'],
    config['db_port'],
    config['db_name']
), echo=config['db_debug'])

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
