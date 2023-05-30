import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.types import Date

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(70), nullable= False, unique= True)
    phone = Column(String, nullable= False, unique= True)
    password = Column(String(50), nullable= False)
    birthday = Column(Date, nullable= False)
    # profile_pic = Column(String(100), ForeignKey('profilepic.id')) 
    


class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable= False, unique=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable= False, unique=True)



class ProfilePic(Base):
    __tablename__ = 'profilepic'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    url = Column(String(250), nullable=False)
    


class VideoPost(Base):
    __tablename__= 'videopost'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    description = Column(String(250))
    # likes_id = Column(Integer, ForeignKey('videolikes.post_id'))
    # comments_id = Column(String(500), ForeignKey('videocomments.post_id'))
    postDate = Column(DateTime, nullable=False)
    user = relationship(User)


class ImagePost(Base):
    __tablename__= 'imagepost'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    description = Column(String(250))
    # likes_id = Column(Integer, ForeignKey('imagelikes.post_id'))
    # comments_id = Column(String(500), ForeignKey('imagecomments.post_id'))
    postDate = Column(DateTime, nullable=False)

class Video(Base):
    __tablename__='video'
    id=Column(Integer, primary_key=True, unique=True)
    videoURL = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('videopost.id'), nullable=False)

class Image(Base):
    __tablename__='image'
    id=Column(Integer, primary_key=True, unique=True)
    imageURL = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey('imagepost.id'), nullable=False)

class VideoLikes(Base):
    __tablename__='videolikes'
    id = Column(Integer, primary_key=True, unique=True)
    post_id = Column(Integer, ForeignKey('videopost.id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)

class VideoComments(Base):
    __tablename__='videocomments'
    id = Column(Integer, primary_key=True, unique=True)
    post_id = Column(Integer, ForeignKey('videopost.id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    comments = Column(String(500), nullable=False)
    #string NO nulo

class ImageLikes(Base):
    __tablename__='imagelikes'
    id = Column(Integer, primary_key=True, unique=True)
    post_id = Column(Integer, ForeignKey('imagepost.id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)

class ImageComments(Base):
    __tablename__ = 'imagecomments'
    id = Column(Integer, primary_key=True, unique=True)
    post_id = Column(Integer, ForeignKey('imagepost.id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    comments = Column(String(500), nullable=False)

    #string NO nulo


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
