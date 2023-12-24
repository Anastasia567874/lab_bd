from data import db_session
from data.db_session import create_session, global_init
from data.books import Book
from data.genres import Genre
import os

db_session.global_init("db/book_store.db")


def create_book(form):
    db_sess = db_session.create_session()
    db_sess = db_session.create_session()
    if form['genreother']:
        new_genre = form['genreother']
        db_sess = db_session.create_session()
        genre = Genre(
            title=form['genreother']
        )
        db_sess.add(genre)
        db_sess.commit()
        db_sess = db_session.create_session()
        genre_oth = db_sess.query(Genre).filter(Genre.title == new_genre).first().id
    else:
        genre_oth = form['genre']
    book = Book(
        title=form['title'],
        author=form['author'],
        age_limit=form['age_limit'],
        annotation=form['annotation'],
        genre_id=genre_oth,
        reviews=''
    )
    db_sess.add(book)
    db_sess.commit()
    return "Успешно"


def del_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(Book).get(book_id)
    db_sess.delete(book)
    db_sess.commit()
    return "Успешно"

def get_books():
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    for book in books:
        print('---------')
        print(f'{book.author} - {book.title}. Ограничение по возрасту: {book.age_limit}+.')
        print(book.annotation)
        genre = db_sess.query(Genre).get(book.genre_id)
        print(f'Книга написана в жанре "{genre.title}"')
    return books


form1 = {'title':'KGBT+',
         'author':'Апостол Павел',
         'age_limit': 18,
            'annotation': """Книга представляет собой нечто среднее между мемуарами,
             тренингом по достижению успеха и сборником мемов. 
             Все это щедро приправлено фирменной авторской психоделикой, 
             без которой не обходится ни одно произведение Пелевина.""",
'genreother': 'Роман'
         }


print(create_book(form=form1))
print(get_books())