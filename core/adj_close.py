from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric
from sqlalchemy.ext.declarative import declared_attr

from metadata.declarative_base import Base


class ValuationMixin:

    @declared_attr
    def stock_id(self):
        return Column(Integer, ForeignKey('stock.id'), primary_key=True)

    date = Column(Date, primary_key=True)

    value = Column(Numeric(precision=10, scale=4), index=True)


class AdjustedClose(ValuationMixin, Base):

    __tablename__ = 'adj_close'
