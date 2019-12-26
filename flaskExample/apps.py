import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import logging
import sys
from params import params
from src.service.memberService.controller.signup import Singup
from src.service.memberService.controller.login import Login
from src.service.memberService.controller.event import Event, EventID, modifyEvent, deleteEvent, addEvent
from src.service.memberService.controller.sales import buyTicket, cancelTicket, Sales, SalesID
from src.service.memberService.controller.membertype import memberType
from src.service.memberService.controller.eventtype import eventType
sys.dont_write_bytecode = True #disable __pycache__
param=params()
app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)

api.add_resource(Singup,"/member/signup")
api.add_resource(Login,"/member/login")

api.add_resource(addEvent,"/event/addEvent")
api.add_resource(Event,"/event/event")
api.add_resource(EventID,"/event/eventID")
api.add_resource(modifyEvent,"/event/modifyEvent")
api.add_resource(deleteEvent,"/event/deleteEvent")
api.add_resource(buyTicket,"/sales/buyTicket")
api.add_resource(cancelTicket,"/sales/cancelTicket")
api.add_resource(Sales,"/sales/sales")
api.add_resource(SalesID,"/sales/sales/{memberID}")
api.add_resource(memberType,"/memberType/memberType")
api.add_resource(eventType,"/eventType/eventType")



if __name__ == "__main__":
    #app.run(host='0.0.0.0:8008', threaded=True, debug=True)
    #CORS(app)

    if '--debug' in sys.argv:
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
    else:
        logging.basicConfig(level=logging.INFO , format='[%(levelname)s] %(message)s')
    logging.info(f'Inanalysis running at port {param.port}')
    app.run(debug='--debug' in sys.argv,port=param.port,host=param.host)
