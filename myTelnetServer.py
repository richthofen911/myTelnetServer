import gevent, gevent.server
from telnetsrv.green import TelnetHandler, command
import time
import os

class MyTelnetHandler(TelnetHandler):
	WELCOME = "\nHello, I'm Yichao. Welcome to my telnet server! Input 'resume' to continue\n"

	@command(['resume'])
	def command_echo(self, params):
		
		self.writeresponse('--------------------------------------------\n')		
		self.writeresponse('\t\t\t   MY RESUME\n')
		self.writeresponse('Name: Yichao Li\t\tEmail: yichaoli.richthofen@gmail.com\nPhone: 647-299-1076\tAddr: 210 Bathurst St. Toronto\n')
		self.writeresponse('\t\t\t   MY SKILLS:')
		self.writeresponse('Java:\t ===================>\t\tPython: ================>')
		self.writeresponse('Android: =====================>\t\tSocket: ================>')
		self.writeresponse('Linux:\t =========================>\n')


server = gevent.server.StreamServer(('192.168.10.102', 8000), MyTelnetHandler.streamserver_handle)
server.serve_forever()

