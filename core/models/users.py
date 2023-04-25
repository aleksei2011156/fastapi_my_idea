from app.core.settings import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship



class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    # relations
    user_topics = relationship("Topics", back_populates="topics_user")
    user_posts = relationship("Posts", back_populates="posts_user")

