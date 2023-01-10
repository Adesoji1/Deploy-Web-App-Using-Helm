from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from flask_bcrypt import Bcrypt
import logging as LOGGER
from models import Post


def all_post(session:Session):
    try:
        posts = session.query(Post).all()
        return posts #.as_dict()
    except IntegrityError as e:
        LOGGER.error(e.orig)


def create(session:Session, post:Post, response):
    try:
        session.add(post)  # Add the post 
        session.commit()  # Commit the change
        
        return {'message':'created!'} 
    except Exception as e:
        raise e 


        




