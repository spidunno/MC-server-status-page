from flask import Flask
from mcstatus import MinecraftServer
from pprint import pprint

htmlOnline = open("online.html").read()
htmlOffline = open("offline.html").read()
js = open("script.js").read()
css = open("style.css").read()

server = MinecraftServer("mc.spidunno.gq", 25565)
pprint((server.host))
onlinePlayers = ''
motd = ''

arr = []
arr2 = []
onlinePlayers = ''

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.

status = server.status()
pprint((status.description['extra']))
if status.players.sample == None:
	onlinePlayers = 'None'
else:
	for i in range(len(status.players.sample)):
  	  arr.append(str(status.players.sample[i].name))
	onlinePlayers = ', '.join(arr)

print(onlinePlayers)
app = Flask('app')

@app.route('/')
def hello_world():
	onlinePlayers = ''
	arr = []
	arr2 = []
	motd = ''
	onlinePlayers = ''
  # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
	status = server.status()
  # pprint((status.description['extra'][0]['text']))
	if status.players.sample == None:
		onlinePlayers = 'None'
	else:
		for i in range(len(status.players.sample)):
	  	  arr.append(str(status.players.sample[i].name))
		onlinePlayers = ', '.join(arr)
  # print(onlinePlayers)
	return htmlOnline.replace('%image', status.favicon).replace('%css', css).replace('%ammountOnline', str(status.players.online)).replace('%currentlyOnline', onlinePlayers).replace('%javascript', js)

app.run(host='0.0.0.0', port=3000)