from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from core.exchange import Exchange
from core.security import Stock
from metadata import metadata

engine = create_engine("sqlite:///tmp_db.db", echo='debug')
metadata.create_all(engine)

session = sessionmaker(bind=engine)()

try:
    PA = session.query(Exchange).filter_by(ticker='PA').one()
except NoResultFound:
    PA = Exchange(ticker='PA', name='Paris Market')
    session.add(PA)

if not session.query(Stock).count():
    for ticker in ['CAC', 'BNP', 'BN']:
        session.add(Stock(ticker=ticker, exchange=PA))
    session.commit()
