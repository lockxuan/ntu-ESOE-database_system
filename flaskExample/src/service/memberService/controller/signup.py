from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class Singup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userAccount', type=str,required=True)
        parser.add_argument('userPassword',type=str,required=True)
        parser.add_argument('userRoles',type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        account = args['userAccount']
        password = args['userPassword']
        role = args['userRoles']

        if (account=='' or password=='' or role==''):
            return "ERROR", 400

        # generator uuid
        uid = userUidGenerator().uid
        
        # connect database
        conn = sqlite3.connect('./test.db')
        cursor = conn.cursor()
        cursor.execute(f"insert into member (`member_id`,`member_account`,`member_password`,`member_roles`) values ('{uid}','{account}','{password}','{role}');")
        conn.commit()
        conn.close()

        return {"status": "success"}, 200
        