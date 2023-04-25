from app.core.settings import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Topics(Base):

    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date_publication = Column(DateTime)

    # relations
    topics_user = relationship("Users", back_populates="user_topics")
    topic_posts = relationship("Posts", back_populates="posts_topic")
