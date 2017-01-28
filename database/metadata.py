from sqlalchemy import Column, DDL, Date, ForeignKey, Integer, MetaData, Numeric, String, Table, UniqueConstraint
from sqlalchemy.event import listen

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

bucket = Table(
    'bucket', metadata,
    Column('id',   Integer,    primary_key=True),
    Column('name', String(20), unique=True)
)

membership = Table(
    'membership', metadata,
    Column('stock_id',  Integer, ForeignKey('stock.id'),  primary_key=True),
    Column('bucket_id', Integer, ForeignKey('bucket.id'), primary_key=True)
)

adj_close = Table(
    'adj_close', metadata,
    Column('stock_id', Integer, ForeignKey('stock.id'), primary_key=True),
    Column('date', Date, primary_key=True),
    Column('value', Numeric(10, 4), index=True, nullable=False)
)

upsert_valuation = DDL("""
CREATE FUNCTION upsert_valuation() RETURNS trigger
    LANGUAGE plpgsql
AS $$
    BEGIN
        IF NEW.date IS NOT NULL AND NEW.stock_id IS NOT NULL THEN
            DELETE FROM adj_close WHERE stock_id = NEW.stock_id AND date = NEW.date;
        END IF;

        RETURN NEW;
    END;
$$;
CREATE TRIGGER upsert_valuation
BEFORE INSERT ON adj_close
FOR EACH ROW EXECUTE PROCEDURE upsert_valuation()
""")
drop_upsert_valuation = DDL("""
DROP FUNCTION IF EXISTS upsert_valuation();
""")
listen(adj_close, 'after_create', upsert_valuation)
listen(adj_close, 'after_drop', drop_upsert_valuation)
