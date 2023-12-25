from sqlalchemy import Integer, String, ForeignKey, Column, Text
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Book(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'books'

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    author = Column(String, nullable=True)
    age_limit = Column(Integer, nullable=True)
    annotation = Column(Text, nullable=True)
    genre_id = Column(Integer, 
                      ForeignKey("genres.id"))
    genre = orm.relationship('Genre')
