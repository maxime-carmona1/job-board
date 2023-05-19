from crypt import methods
from flask import Flask
from flask_cors import CORS
from sqlalchemy import *
from .mainDb import SessionLocal
from .MyTables import User, advertisments

db =SessionLocal()
app= Flask(__name__)
CORS(app)

@app.route('/API/USERS',methods=["GET"])
def index():
    data = db.query(User).all()
    result = []
    for user in data:
        result.append(user.as_dict())
    return{
         "result" : result
         }

@app.route('/API/ADVERTISMENTS',methods=["GET"])
def advertisment():
    data = db.query(advertisments).all()
    result = []
    for advertisment in data:
        result.append(advertisment.as_dict())
    return{
         "result" : result
         }
#@app.post('/API/ADVERTISMENTS',tags=['Advertisments'] , methods=["POST"],status_code=status.HTTP_201_CREATED )
async def add_advertisment(advertisment: advertisment):
    insert = advertisment(
        entreprise=advertisment.entreprise,
        job_title=advertisment.job_title,
        job_description=advertisment.job_description,
        online_date=advertisment.online_date,
        contratType=advertisment.contratType,
        salaire=advertisment.salaire,

    )
    data = db.query(advertisments).filter(advertisments.entreprise == insert.entreprise).first()

    #if data:
        #raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Companie already Exist')
    db.add(insert)
    db.commit()
    return {
        "success": True,
        "msg": "Entreprise store Successfully",
    }
#@app.post('/API/USERS',tags=['Users'] , methods=["POST"],status_code=status.HTTP_201_CREATED )
async def add_user(user: User):
    insert = user(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        user_description=user.user_description,
        mail_adress=user.mail_adresse,
        phone=user.phone,
        mdp=user.mdp,

    )
    data = db.query(User).filter(User.entreprise == insert.username).first()

    #if data:
        #raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already Exist')
    db.add(insert)
    db.commit()
    return {
        "success": True,
        "msg": "Successfully to creat your profile",
    }
