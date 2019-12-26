from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class modifyEvent(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventID', type=str,required=True)
        parser.add_argument('eventName', type=str,required=True)
        parser.add_argument('eventType',type=int,required=True)
        parser.add_argument('eventTypeDescription',type=str,required=True)
        parser.add_argument('eventDescription',type=str,required=False)
        parser.add_argument('eventDate',type=str,required=True)
        parser.add_argument('startingTime',type=str,required=True)
        parser.add_argument('endingTime',type=str,required=True)
        parser.add_argument('saleRoles',type=str,required=False)
        parser.add_argument('salesLimit',type=str,required=False)
        parser.add_argument('salesPerMember',type=str,required=False)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['eventID']
        name = args['eventName']
        etype = args['eventType']
        tdes = args['eventTypeDescription']
        des = args['eventDescription']
        date = args['eventDate']
        stime = args['startingTime']
        etime = args['endingTime']
        roles = args['saleRoles']
        limit = args['salesLimit']
        permem = args['salesPerMember']

        if (ID=='' or name=='' or etype=='' or tdes=='' or date=='' or stime=='' or etime==''):
            return "ERROR !", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `sales_limit`, `sales_per_member`) values ('{}');")
            cursor.execute(f"UPDATE event SET `event_name`='{name}', `event_type`='{etype}', `event_description`='{des}', `event_date`='{date}', `starting_time`='{stime}', `ending_time`='{etime}', `sale_roles`='{roles}', `sales_limit`='{limit}', `sales_per_member`='{permem}' WHERE `event_id`='{ID}';")

            cursor.execute(f"INSERT OR REPLACE INTO eventtype VALUES ('{etype}', '{tdes}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400


