from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class addEvent(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventName', type=str,required=True)
        parser.add_argument('eventType',type=int,required=True)
        parser.add_argument('eventDescription',type=str,required=False)
        parser.add_argument('eventDate',type=str,required=True)
        parser.add_argument('startingTime',type=str,required=True)
        parser.add_argument('endingTime',type=str,required=True)
        parser.add_argument('saleRoles',type=str,required=False)
        parser.add_argument('salesLimit',type=str,required=False)
        parser.add_argument('salesPerMember',type=str,required=False)
        args = parser.parse_args()
        logging.info(f'{args}')
        name = args['eventName']
        etype = args['eventType']
        des = args['eventDescription']
        date = args['eventDate']
        stime = args['startingTime']
        etime = args['endingTime']
        roles = args['saleRoles']
        limit = args['salesLimit']
        permem = args['salesPerMember']

        if (name=='' or etype=='' or date=='' or stime=='' or etime==''):
            return "ERROR", 400

        # generator uuid
        uid = userUidGenerator().uid
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            cursor.execute(f"INSERT INTO event values ('{uid}', '{name}', '{etype}', '{des}', '{date}', '{stime}', '{etime}', '{roles}', '{limit}', '{permem}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400


