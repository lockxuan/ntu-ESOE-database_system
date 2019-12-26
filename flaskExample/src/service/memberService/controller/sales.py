from flask_restful import Resource, reqparse
from params import params
from src.service.memberService.utils import userUidGenerator
import sqlite3
import logging
from datetime import datetime


class buyTicket(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('memberID', type=str,required=True)
        parser.add_argument('eventID', type=str,required=True)
        parser.add_argument('numberOfTicket', type=int,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        memID = args['memberID']
        eveID = args['eventID']
        num = args['numberOfTicket']

        if (memID=='' or eveID=='' or num==''):
            return "ERROR", 400

        # generator uuid
        uid = userUidGenerator().uid
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            try:
                maxn = cursor.execute(f"SELECT sales_per_member FROM event WHERE `event_id`='{eveID}';")
                maxnum=''
                for i in maxn:
                    maxnum = i[0]
                if maxnum=='':
                    maxnum = 99999999
                if num>maxnum:
                    rt = "You can't buy more than " + str(maxnum) + ' tickets.'
                    return  rt,400
            except:
                return "ERROR",400
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            result = cursor.execute(f"INSERT INTO sales VALUES ('{uid}', '{memID}', '{num}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', '{eveID}');")
            conn.commit()

            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR", 400

class cancelTicket(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('salesID', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        ID = args['salesID']

        if (ID==''):
            return "ERROR", 400
        
        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            #cursor.execute(f"INSERT INTO event (`event_id`, `event_name`, `event_type`, `event_description`, `event_date`, `starting_time`, `ending_time`, `sale_roles`, `salesLimit`, `sales_per_member`) values ('{}');")
            result = cursor.execute(f"DELETE FROM sales WHERE `sales_id`='{ID}';")
            conn.commit()
            conn.close()
            return "OK", 200
        except:
            conn.close()
            return "ERROR, wrong sales ID.", 400

class Sales(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('startTime', type=str,required=True)
        parser.add_argument('endTime', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        stime = args['startTime']
        etime = args['endTime']
        try:
            # connect database
            conn = sqlite3.connect('./test.db')
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM sales WHERE `time_of_sales` BETWEEN '{stime}' AND '{etime}';")
            conn.commit()
            
            ans = []
            for i in result:
                ans.append({"salesID" : i[0], "memberID" : i[1], "eventID" : i[2],
                    "numberOfTicket" : i[3], "timeOfSales" : i[4]})
            conn.close()
            return ans, 200
        except:
            return "ERROR",400

class SalesID(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('startTime', type=str,required=True)
        parser.add_argument('endTime', type=str,required=True)
        parser.add_argument('memberID', type=str,required=True)
        args = parser.parse_args()
        logging.info(f'{args}')
        stime = args['startTime']
        etime = args['endTime']
        ID = args['memberID']

        # connect database
        conn = sqlite3.connect('./test.db')
        try:
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT * FROM sales WHERE `member_id`='{ID}' AND `time_of_sales` BETWEEN '{stime}' AND '{etime}';")
            conn.commit()
            
            ans = []
            for i in result:
                ans.append({"salesID" : i[0], "memberID" : i[1], "eventID" : i[2],
                    "numberOfTicket" : i[3], "timeOfSales" : i[4]})
            conn.close()
            return ans, 200
        except:
            conn.close()
            return "ERROR", 400



