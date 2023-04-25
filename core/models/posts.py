from app.core.settings import Base
from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import relationship



class Posts(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(Integer, unique=True)
    body = Column(Text)
    date_publication = Column(DateTime)

    # relations
    posts_user = relationship("Users", back_populates="user_posts")
    posts_topic = relationship("Topics", back_populates="topic_posts")
