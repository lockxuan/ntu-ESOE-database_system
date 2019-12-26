import uuid
import logging
import sqlite3

class userUidGenerator():
    def __init__(self):
        self.uid=str(uuid.uuid1())
        while self.checkUserID(self.uid) != ():
            self.uid=str(uuid.uuid1())

    def checkUserID(self, userUid):
        conn = sqlite3.connect('./test.db')
        cursor = conn.cursor()
        result = cursor.execute(f"select * from member where `member_id`='{self.uid}'")
        for row in result:
            logging.info(row[0])
            conn.close()
            return row[0]
        result = cursor.execute(f"select * from event where `event_id`='{self.uid}'")
        for row in result:
            logging.info(row[0])
            conn.close()
            return row[0]
        result = cursor.execute(f"select * from sales where `sales_id`='{self.uid}'")
        for row in result:
            logging.info(row[0])
            conn.close()
            return row[0]
        conn.close()
        return ()