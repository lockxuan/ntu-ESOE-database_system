from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class EventID(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventID', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['eventID']

        if (ID==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        ans = []
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            result = cursor.execute(f"SELECT * FROM event WHERE event_id = '{ID}';")
            conn.commit()
            for i in result:
                ans.append({"eventID" : i[0], "eventName" : i[1], "eventType" : i[2],
                    "eventTypeDescription" : i[3], "eventDescription" : i[4],
                    "eventDate" : i[5], "startingTime" : i[6], "saleRoles" : i[7],
                    "salesLimit" : i[8], "salesPerMember" : i[9]})

            conn.close()
            return ans[0], 200
        except:
            conn.close()
            return "ERROR, wrong event ID.", 400


