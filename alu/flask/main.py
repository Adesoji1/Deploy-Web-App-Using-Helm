import uvicorn, os, logging
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from pydantic import BaseModel
from decouple import config
from fastapi.middleware.cors import CORSMiddleware


from database import session
from orm import all_post
from models import Post 

import sqlite3


app = FastAPI(
    title="AluX",
    description="""**AluX Holding**""",
    version="0.0.1",
    contact={
        "name": "AluX",
        "email": "team@alux.com",
    },
)


origins = [
    "*"
]
# "http://127.0.0.1:3000",
#     "http://localhost:3000",
#     "http://127.0.0.1:31015",
#     "http://localhost:31015"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# db = SQLAlchemy() 




class UserRegisterModel(BaseModel):
    username: str
    firstname: str
    lastname:str
    email: str
    password: str

class UserLoginModel(BaseModel):
    email: str
    password: str 




@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.get('/status')
def status(response:Response):
    return {'status':'ok'}



@app.get("/posts")
def posts(response:Response):
    
    return all_post(session) 




if __name__ == "__main__":
    try:
        # from sqlalchemy.orm import Session
        database = r"db.sqlite"

        # create a database connection
       
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        # try:
        #     cur.execute("DROP TABLE post")
        #     print("Table dropped... ")
        #     conn.commit()
        # except:
        #     pass 

        data = [
            {'title':'title1', 'sub_title':'sub_title1', 'content':'content1'},
            {'title':'title2', 'sub_title':'sub_title2', 'content':'content2'},
            {'title':'title3', 'sub_title':'sub_title2', 'content':'content3'}
        ]

        for d in data:
            sql = ''' 
                INSERT INTO post(title,sub_title,content)
                VALUES('{title}','{sub_title}','{content}')
            '''.format(title=d['title'], sub_title=d['sub_title'], content=d['content'])

            print(sql)

            cur.execute(sql)
            conn.commit()

    except Exception as e:
        print(e)


    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=2) 
    

