from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models import Exchange, Stock
from models.declarative_base import Base

engine = create_engine("sqlite:///tmp_db.db", echo='debug')
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

try:
    PA = session.query(Exchange).filter(Exchange.ticker == 'PA').one()
except NoResultFound:
    PA = Exchange(ticker='PA', name='Paris Market')
    session.add(PA)

if not session.query(Stock).count():
    for ticker in ['CAC', 'BNP', 'BN']:
        session.add(Stock(ticker=ticker, exchange=PA))
    session.commit()
