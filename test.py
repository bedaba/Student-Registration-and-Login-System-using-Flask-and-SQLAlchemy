from maypackage import db, app
from maypackage.model import User, Post, Subject
import sys


# create DB
def create_db():
    with app.app_context():
        db.create_all()


def create_users():
    with app.app_context():
        user = User(username='bedaba', email="asd@gmail.com", password='147')
        db.session.add(user)
        db.session.commit()


def read_users():
    with app.app_context():
        print(User.query.all())


def update_users():
    with app.app_context():
        user = User.query.filter_by(username='bedaba').first()
        user.username = "ASD"
        db.session.commit()
        print(User.query.filter_by(username='ASD').first())


def delete_users():
    with app.app_context():
        user = User.query.filter_by(username='bedaba').first()
        db.session.delete(user)
        db.session.commit()


def create_post():
    with app.app_context():
        user = User.query.first()
        post = Post(title='P1', content="P1Con", user_id=user.id)
        db.session.add(user)
        db.session.commit()


def read_usersWithPost():
    with app.app_context():
        user = User.query.first()
        print(user.posts)

def read_sub():
    with app.app_context():
        sub = Subject.query.first()
        print(sub)
        print(sub.user_id)

if __name__ == '__main__':
    globals()[sys.argv[1]]()



