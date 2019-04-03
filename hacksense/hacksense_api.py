from flask import Flask, request
import json

app = Flask(__name__)
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

@app.route('/')
def num():
	return str(len(devices))

@app.route('/list')
def list():
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

app.run()
