from sqlalchemy import Column, BigInteger, VARCHAR
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column('id', BigInteger, primary_key=True)
    username = Column('username', VARCHAR(255))
    password = Column('password', VARCHAR(255))

    def __repr__(self):
        return str([getattr(self, c.name, None) for c in self.__table__.c])

    @staticmethod
    def find_one(username):
        return db.session.query(User.id, User.username, User.password).filter(User.username == username).first()

    @staticmethod
    def match(username, password):
        user = User.find_one(username)
        if not user:
            return False

        # TODO: Compare password hashed
        return user.password == password



