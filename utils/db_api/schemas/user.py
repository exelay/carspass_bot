from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    phone = Column(String(20), primary_key=True)
    pass_code = Column(String(20))

    query: sql.Select

