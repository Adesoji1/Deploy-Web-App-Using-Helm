# models.py

# from hello import db
from email.policy import default
from sqlalchemy.sql import func

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement="auto")

    title = Column(String(100), nullable=False)
    sub_title = Column(Text(100), nullable=True)

    content = Column(Text(100), nullable=True)
    
    created_at = Column(DateTime(timezone=True),server_default=func.now()) 
    updated_at = Column(DateTime(timezone=True),server_default=func.now()) 
    

    def __repr__(self):
        return f'<Post {self.title}>'

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)

