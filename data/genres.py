from sqlalchemy import Integer, String, Column
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Genre(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'genres'

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    book = orm.relationship("Book", back_populates='genre')
