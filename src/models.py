import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum
Base = declarative_base()

class User(Base):
    __tablename__='user'
    Id = Column(Integer, primary_key=True)
    Username = Column(String(20), nullable = False, unique = True)
    Email = Column(String(20), nullable = False, unique = True)

class Follower(Base):
    __tablename__='follower'
    Id = Column(Integer, primary_key=True)
    UserFromId = Column(Integer, ForeignKey('user.Id'))
    UserToId = Column(Integer, ForeignKey('user.Id'))
    user = relationship(User)

class Post(Base):
    __tablename__='post'
    Id = Column(Integer, primary_key=True)
    UserFromId = Column(Integer, ForeignKey('user.Id'))
    UserToId = Column(Integer, ForeignKey('user.Id'))
    user = relationship(User)

class Media(Base):
    __tablename__='media'
    Id = Column(Integer, primary_key=True)
    Type = Column(Enum('admin', 'user', name='user_type'))
    Url = Column(String(50), nullable=True)
    PostId = Column(Integer, ForeignKey('post.Id'))
    UserToId = Column(Integer, ForeignKey('post.Id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__='comment'
    Id = Column(Integer, primary_key=True)
    comment_text = Column(String(30), nullable=True)
    author_id = Column(Integer, ForeignKey('user.Id'))
    post_id = Column(Integer, ForeignKey('post.Id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
