from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class memberType(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userID', type=str,required=True)
        parser.add_argument('typeDescription',type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['userID']
        tdes = args['typeDescription']


        if (ID=='' or tdes==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            roles = cursor.execute(f"SELECT `member_roles` FROM member WHERE `member_id`='{ID}';")
            role = ''
            for i in roles:
            	role = i[0]
            cursor.execute(f"INSERT OR REPLACE INTO membertype VALUES ('{role}', '{tdes}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400