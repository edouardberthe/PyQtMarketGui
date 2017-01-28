from sqlalchemy.orm.exc import NoResultFound

from core import Bucket, Exchange, Stock
from database import Session, engine, metadata

metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)

session = Session()
try:
    PA = session.query(Exchange).filter_by(ticker='PA').one()
except NoResultFound:
    PA = Exchange(ticker='PA', name='Paris Market')
    session.add(PA)

CAC40Tickers = ['AC', 'ACA', 'AI', 'AIR', 'BN', 'BNP', 'CA', 'CAP', 'CS', 'DG', 'EI', 'EN', 'ENGI', 'FP', 'FR', 'GLE', 'KER', 'LHN', 'LI', 'LR', 'MC', 'ML', 'MT', 'NOKIA', 'OR', 'ORA', 'PUB', 'RI', 'RNO', 'SAF', 'SAN', 'SGO', 'SOLB', 'SU', 'SW', 'TEC', 'UG', 'UL', 'VIE', 'VIV']
CAC40 = Bucket([Stock(ticker=ticker, exchange=PA) for ticker in CAC40Tickers], name='CAC 40')
for stock in CAC40:
    session.add(stock)
session.add(CAC40)

session.commit()

