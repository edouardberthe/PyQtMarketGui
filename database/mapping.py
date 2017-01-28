from sqlalchemy.orm import mapper, relationship

from core import Bucket, Exchange, Stock
from .metadata import bucket, exchange, membership, stock

mapper(Stock, stock, properties={
    'exchange': relationship(Exchange),
    'buckets': relationship(Bucket, secondary=membership, back_populates='stocks')
})

mapper(Bucket, bucket, properties={
    'stocks': relationship(Stock, secondary=membership, back_populates='buckets')
})

mapper(Exchange, exchange)
