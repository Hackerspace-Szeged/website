from flask import Flask, request
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

devices = []
alldevices = {}

try:
	f = open("devices.txt")
	for l in f.readlines():
		hash, name, dname = l.strip().split(":")
		alldevices[hash] = [name, dname]
	f.close()
except:
	pass

@socketio.on("connect")
def num_to_ws():
	emit("num", len(devices))

@app.route('/')
def num_to_page():
	return str(len(devices))

def dev_list():
	people = {}
	people["guest"] = 0
	for d in devices:
		try:
			if alldevices[d][0] not in people:
				people[alldevices[d][0]] = [alldevices[d][1]]
			else:
				people[alldevices[d][0]].append(alldevices[d][1])
		except:
			people["guest"] += 1
	return json.dumps(people)

@socketio.on("getClients")
def list_to_ws():
	emit("clients", dev_list())

@app.route('/list')
def list_to_page():
	return dev_list()

@app.route('/connect', methods=['POST'])
def connect():
	machash = request.form["device"]
	devices.append(machash)
	return str(True)

@app.route('/disconnect', methods=['POST'])
def disconnect():
	machash = request.form["device"]
	try:
		devices.remove(machash)
		return str(True)
	except:
		return str(False)

socketio.run(app, debug=False, host="0.0.0.0")