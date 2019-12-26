from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging

class Event(Resource):
    def get(self):
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM event LEFT JOIN eventtype ON eventtype.type_code=event.event_type;")
            conn.commit()
            
            ans = []
            for i in result:
                ans.append({"eventID" : i[0], "eventName" : i[1], "eventType" : i[2], "eventTypeDescription" : i[13],
                    "eventDescription" : i[3], "eventDate" : i[4],
                    "startingTime" : i[5], "endingTime" : i[6], "saleRoles" : i[7],
                    "salesLimit" : i[8], "salesPerMember" : i[9], "price" : i[10]
                    , "image" : i[11]})
            conn.close()
            return ans, 200
        except:
            conn.close()
            return "ERROR", 400

class EventID(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('eventID', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['eventID']
        print("------- id ",ID)
        if (ID==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        ans = ""
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            result = cursor.execute(f"SELECT * FROM event WHERE event_id = '{ID}';").fetchall()
            conn.commit()
            for i in result:
                ans=({"eventID" : i[0], "eventName" : i[1], "eventType" : i[2],
                    "eventTypeDescription" : i[3], "eventDescription" : i[4],
                    "eventDate" : i[5], "startingTime" : i[6], "saleRoles" : i[7],
                    "salesLimit" : i[8], "salesPerMember" : i[9], "price" : i[10]
                    , "image" : i[11]})
            conn.close()
            if ans=="":
                return "ERROR, wrong event ID.", 400
            return ans, 200
        except:
            print("---------------")
            conn.close()
            return "ERROR, wrong event ID.", 400

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
        parser.add_argument('salesLimit',type=int,required=False)
        parser.add_argument('salesPerMember',type=int,required=False)
        parser.add_argument('price',type=int,required=False)
        parser.add_argument('image',type=str,required=False)
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
        pri = args['price']
        img = args['image']
        if pri=="":
            pri=0
        if permem=="":
            pri=10
        if limit=="":
            pri=100000

        if (ID=='' or name=='' or etype=='' or tdes=='' or date=='' or stime=='' or etime==''):
            return "ERROR !", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `sales_limit`, `sales_per_member`) values ('{}');")
            cursor.execute(f"UPDATE event SET `event_name`='{name}', `event_type`='{etype}', `event_description`='{des}', `event_date`='{date}', `starting_time`='{stime}', `ending_time`='{etime}', `sale_roles`='{roles}', `sales_limit`='{limit}', `sales_per_member`='{permem}', `price`='{pri}', `image`='{img}' WHERE `event_id`='{ID}';")

            cursor.execute(f"INSERT OR REPLACE INTO eventtype VALUES ('{etype}', '{tdes}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400

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
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values 
            result = cursor.execute(f"SELECT * FROM event WHERE event_id = '{ID}';")
            rows = result.fetchall()
            if (rows==[]):
                conn.close()
                return "ERROR, wrong event ID.", 400
            conn.close()
            conn = sqlite3.connect('./test.db')
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM event WHERE event_id = '{ID}';")

            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR, wrong event ID.", 400

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
        parser.add_argument('price',type=int,required=False)
        parser.add_argument('image',type=str,required=False)

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
        pri = args['price']
        img = args['image']

        if (name=='' or etype=='' or date=='' or stime=='' or etime==''):
            return "ERROR", 400

        if pri=="":
            pri=0
        if permem=="":
            pri=10
        if limit=="":
            pri=100000

        # generator uuid
        uid = userUidGenerator().uid
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            cursor.execute(f"INSERT INTO event values ('{uid}', '{name}', '{etype}', '{des}', '{date}', '{stime}', '{etime}', '{roles}', '{limit}', '{permem}', '{pri}', '{img}');")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400



