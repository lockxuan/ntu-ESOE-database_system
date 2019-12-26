from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class eventType(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventID', type=str,required=True)
        parser.add_argument('typeDescription',type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['eventID']
        tdes = args['typeDescription']


        if (ID=='' or tdes==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            codes = cursor.execute(f"SELECT `event_type` FROM event WHERE `event_id`='{ID}';")
            role = ''
            for i in codes:
            	code = i[0]
            cursor.execute(f"INSERT OR REPLACE INTO eventtype VALUES ({code}, '{tdes}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400