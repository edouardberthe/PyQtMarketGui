from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, UniqueConstraint
from sqlalchemy.orm import mapper, relationship

from core.exchange import Exchange
from core.security import Stock

metadata = MetaData()

stock = Table(
    'stock', metadata,
    Column('id',       Integer, primary_key=True),
    Column('ticker',   String(5), nullable=False, index=True),
    Column('name',     String(20)),
    Column('exchange', String(2), ForeignKey('exchange.ticker'), nullable=False),
    UniqueConstraint('ticker', 'exchange')
)

country = Table(
    'country', metadata,
    Column('name', String(20), primary_key=True)
)

exchange = Table(
    'exchange', metadata,
    Column('ticker', String(2), primary_key=True),
    Column('name', String(20))
)

mapper(Stock, stock, properties={
    'exchange': relationship(Exchange)
})

mapper(Exchange, exchange)
