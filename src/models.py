import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id=Column(Integer(), primary_key=True)
    username=Column(String(50), nullable=False, unique=True)
    first_name=Column(String(30), nullable=False)
    last_name=Column(String(30), nullable=False)
    email=Column(String(50), nullable=False, unique=True)
    post=relationship("Post", uselist=True, backref="user")
    comment=relationship("Comment", uselist=True, backref="user")
    like=relationship("Like", uselist=True, backref="user")
    Follows=relationship("Follow", uselist=True, backref="user")

class Post(Base):
    __tablename__="post"
    id=Column(Integer(), primary_key=True)
    user_id=Column(Integer(), ForeignKey("user.id"))
    post_media=relationship("Post_media", uselist=True, backref="post")
    comments=relationship("Comment", uselist=True, backref="post")
    likes=relationship("Like", uselist=True, backref="post")
    


class Post_media(Base):
    __tablename__="post_media"
    id=Column(Integer(), primary_key=True)
    media_url=Column(String(250), nullable=False, unique=True)
    post_id=Column(Integer(), ForeignKey("post.id"))

class Comment(Base):
    __tablename__="comment"
    id=Column(Integer(), primary_key=True)
    comment_text=Column(String(250), nullable=False, unique=True)
    post_id=Column(Integer(), ForeignKey("post.id"))
    userfrom_id=Column(Integer(), ForeignKey("user.id"))

class Like(Base):
    __tablename__="like"
    id=Column(Integer(), primary_key=True)
    post_id=Column(Integer(), ForeignKey("post.id"))
    userfrom_id=Column(Integer(), ForeignKey("user.id"))

class Follow(Base):
    __tablename__="follow"
    id=Column(Integer(), primary_key=True)
    userfrom_id=Column(Integer(), ForeignKey("user.id"))
    userto_id=Column(Integer(), ForeignKey("user.id"))






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
