from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
from decouple import config


try: 
    # DB_USERNAME = config("DB_USERNAME")
    # DB_PASSWORD = config("DB_PASSWORD")
    # DB_HOTE = config("DB_HOTE")
    # DB_NAME = os.environ.get("DB_NAME")
    # DB_PORT = os.environ.get("DB_PORT")

    # engine = create_engine(
    #     f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOTE}:{DB_PORT}/{DB_NAME}",
    #     connect_args={'check_same_thread': False}
    # )

    engine = create_engine(
        'sqlite:///db.sqlite',
        # echo=True,
        connect_args={'check_same_thread': False}
    )

    Session = sessionmaker(bind=engine)
    session = Session() 

except:
    raise "database error"


