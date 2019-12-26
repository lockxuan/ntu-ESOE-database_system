from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging
import hashlib 

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userAccount', type=str,required=True)
        parser.add_argument('userPassword',type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        account = args['userAccount']
        password = args['userPassword']

        if (account=='' or password==''):
            return "ERROR", 400
        # generator uuid
        uid = userUidGenerator().uid
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            memID = cursor.execute(f"SELECT member_id FROM member WHERE (`member_account` = '{account}' AND `member_password` = '{password}');")
            conn.commit()
            ID = ""
            for i in memID:
                ID = i
            token = hashlib.sha224(str(ID[0]).encode()).hexdigest()
            conn.close()
            return {"memberID": ID[0], "token":token}, 200
        except:
            conn.close()
            return "ERROR", 400



        