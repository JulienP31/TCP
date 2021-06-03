""" TCP client class definition """

from tcp_common import *



""" Class definition """
class TCP_Client(TCP_Common):
	def __init__(self):
		super(TCP_Client, self).__init__()

	def initialize(self):
		self._csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._csocket.setblocking(1)
		self._csocket.settimeout(None)
		self._csocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)

	def connect_to_server(self, host="localhost"):
		self._csocket.connect( (host, self._port) )

	def close_connection(self):
		self._close_client_connection()



""" Testing """
if __name__ == '__main__':
	try:
		print('initialize')
		tcp_client = TCP_Client()
		tcp_client.initialize()
		print('connect_to_server')
		tcp_client.connect_to_server()
		# Communicate with server continuously...
		mylist = []
		for i in range(10):
			data = bytearray(mylist)
			tcp_client.send_msg(i, len(data), data)
			msg = tcp_client.receive_msg() #< Receive back sent msg
			print(msg)
			mylist.append(i)
	except Exception as e:
		print(e)
	finally:
		print('close_connection')
		tcp_client.close_connection()


