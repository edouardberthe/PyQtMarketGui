from sqlalchemy.orm.exc import NoResultFound

from core import Exchange, Stock
from database import Session

session = Session()

try:
    PA = session.query(Exchange).filter_by(ticker='PA').one()
except NoResultFound:
    PA = Exchange(ticker='PA', name='Paris Market')
    session.add(PA)

if not session.query(Stock).count():
    for ticker in ['CAC', 'BNP', 'BN']:
        session.add(Stock(ticker=ticker, exchange=PA))
    session.commit()
