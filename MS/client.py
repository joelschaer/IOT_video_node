#!/usr/bin/env python3

from flask import Flask, json, request, g
from flask_restplus import Resource, Api
from flask_restplus import Resource, Api
from values import Configuration
from streamLocal import Stream
from recordLocal import Record
from time import sleep
import threading
import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='PiVideoAPI',
    description='Expose the PiVideo functionality interraction',
)

ns = api.namespace('pivideo', description='Interraction with the PiVideo')


class base(Resource):
  
  def get(self):
    response = app.response_class(
      response=json.dumps({'routes':{'/':'endpoint list', '/param/record':'change record times', '/param/backend':'change backend address', '/record':'record', '/stream': 'stream'}}),
      status=200,
      mimetype='application/json'
    )
    return response

class paramRecord(Resource):
  """interracting with configuration file"""

  @api.response(200, 'Successing')
  def get(self):
    config = Configuration()
    config.load()
    record_values = {}
    record_values['t_before'] = config.get("record", "t_before")
    record_values['t_after'] = config.get("record", "t_after")

    return json.dumps(record_values), 200
  
  @api.response(201, 'Key created successfully')
  def post(self):
    config = Configuration()
    config.load()

    # TODO: check sent value is an integer
    try:
      t_before = request.form['t_before']
    except:
      t_before = None
    try:
      t_after = request.form['t_after']
    except:
      t_after = None

    if t_before != None:
      config.set(route='record', key='t_before', value=t_before)
    if t_after != None:
      config.set(route='record', key='t_after', value=t_after)
    config.store()
    
    return None, 201

class paramBackend(Resource):
  """interracting with configuration file"""

  @api.response(200, 'Successing')
  def get(self):
    config = Configuration()
    config.load()
    record_values = {}
    record_values['backend_address'] = config.get("backend", "address")

    return json.dumps(record_values), 200
  
  @api.response(201, 'Key created successfully')
  def post(self):
    config = Configuration()
    config.load()

    try:
      backend_address = request.form['backend_address']
    except:
      backend_address = None

    if backend_address != None:
      config.set(route='backend', key='address', value=backend_address)
    config.store()
    
    return None, 201

class RecordEndpoint(Resource):  

  api.response(200, 'record started')   
  def get(self):
    global t1
    t1.storeVideo('video_'+str(datetime.datetime.now()))

    return None, 200

class StreamEndpoint(Resource):  
  api.response(200, 'stream started')   
  def get(self):
    global t1
    if (request.args.get('start') == "true") :
        t1 = Stream()
        t1.start()
        print("starting")
        print(t1)
        
    elif (request.args.get('start') == "false"):
        print("stopping")
        print(threading.enumerate())
        sleep(3)
        t1.stop()
        t1.join()
        print("done")

    return None, 200
            
api.add_resource(base, '/')
api.add_resource(RecordEndpoint, '/record', methods=['GET']) # Route_Record
api.add_resource(StreamEndpoint, '/stream')
api.add_resource(paramRecord, '/param/record')
api.add_resource(paramBackend, '/param/backend')


if __name__ == "__main__":
    global t1
    t1 = None
    config = Configuration()
    config.load() 
    t_before = config.get('record', 't_before')
    t_after = config.get('record', 't_after')
    t1 = Record(t_before, t_after)
    t1.start()
    app.run(host='0.0.0.0', port='2001')

