from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        MetaData, Numeric, String, Table, Text, create_engine, UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()


# user = Table('user', metadata,
#              Column('id', Integer(), primary_key=True),
#              Column('name', String(30), nullable=False),
#              Column('surname', String(40), nullable=False),
#              Column('email', Text(), nullable=False),
#              Column('password', Text()),
#              )

class Users(Base):
    __tablename__ = 'users'
    id = Column('id', Integer(), primary_key=True)
    name = Column('name', String(30), nullable=False)
    surname = Column('surname', String(40), nullable=False)
    email = Column('email', Text(), nullable=False)
    password = Column('password', Text())
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    @validates("email")
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("failed simple email validation")
        return address

    __table_args__ = (
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )
