from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, UniqueConstraint
from sqlalchemy import DDL
from sqlalchemy import Date
from sqlalchemy import Numeric
from sqlalchemy import event
from sqlalchemy.orm import mapper, relationship

from core.exchange import Exchange
from core.security import Stock

metadata = MetaData()

stock = Table(
    'stock', metadata,
    Column('id',       Integer, primary_key=True),
    Column('ticker',   String(5), nullable=False, index=True),
    Column('name',     String(20)),
    Column('exchange_ticker', String(2), ForeignKey('exchange.ticker'), nullable=False),
    UniqueConstraint('ticker', 'exchange_ticker')
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

adj_close = Table(
    'adj_close', metadata,
    Column('stock_id', Integer, ForeignKey('stock.id'), primary_key=True),
    Column('date', Date, primary_key=True),
    Column('value', Numeric(10, 8), index=True, nullable=False)
)

upsert_valuation = DDL("""
CREATE FUNCTION upsert_valuation() RETURNS trigger
    LANGUAGE plpgsql
AS $$
    BEGIN
        IF NEW.date IS NOT NULL AND NEW.stock_id IS NOT NULL THEN
            DELETE FROM valuation WHERE stock_id = NEW.stock_id AND date = NEW.date;
        END IF;

        RETURN NEW;
    END;
$$;
CREATE TRIGGER upsert_valuation
BEFORE INSERT ON adj_close
FOR EACH ROW EXECUTE PROCEDURE upsert_valuation()
""")
event.listen(adj_close, 'after_create', upsert_valuation)

mapper(Stock, stock, properties={
    'exchange': relationship(Exchange)
})

mapper(Exchange, exchange)
