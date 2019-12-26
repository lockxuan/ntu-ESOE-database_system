from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class deleteEvent(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventID', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['eventID']

        if (ID==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            result = cursor.execute(f"DELETE FROM event WHERE event_id = '{ID}';")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR, wrong event ID.", 400


