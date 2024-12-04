from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
import datetime as dt
import os

Base = declarative_base()

class Order(Base):

    __tablename__ = "Orders"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    customer_name = Column("customer_name", String, nullable=False)
    orders = Column("orders", String, nullable=False)
    order_number = Column("table_number", Integer, nullable=False)
    date_created = Column("date_created", Date, nullable=False, default=dt.datetime.now(dt.timezone.utc))
