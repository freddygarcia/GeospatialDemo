from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from geoalchemy2 import Geometry, WKTElement
from app.core.db import SessionLocal, Base


class GroceryStore(Base):
    __tablename__ = 'groceries'

    id = Column("OBJECTID", Integer, primary_key=True, autoincrement=True)
    name = Column("STORENAME", String)
    addr = Column("ADDRESS", String)
    phone = Column("PHONE", BigInteger)
    notes = Column("NOTES", String)
    active = Column("ACTIVE", Boolean)
    zipcode = Column("ZIPCODE", Integer)
    location = Column("geometry", Geometry('POINT', srid=4326))

    @staticmethod
    def get_all_stores():
        session = SessionLocal()
        stores = session.query(GroceryStore).all()
        session.close()
        return stores

    @staticmethod
    def get_store(id):
        session = SessionLocal()
        store = session.query(GroceryStore).get(id)
        session.close()
        return store

    @staticmethod
    def add_store(store):
        session = SessionLocal()
        session.add(store)
        session.commit()
        session.refresh(store)
        return store

    @staticmethod
    def dict_to_point(location: dict) -> WKTElement:
        return WKTElement('POINT({} {})'.format(location['lng'],
                                                location['lat']))

    def __str__(self) -> str:
        return f'<GroceryStore id={self.id} name={self.name}>'

    def __repr__(self) -> str:
        return self.__str__()
