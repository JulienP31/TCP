""" TCP server class definition """

from tcp_common import *



""" Class definition """
class TCP_Server(TCP_Common):
	def __init__(self):
		super(TCP_Server, self).__init__()
		self._ssocket = None

	def initialize(self):
		self._ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._ssocket.bind( ('', self._port) )

	def wait_for_client(self):
		self._ssocket.listen(1)
		( self._csocket, (ip, port) ) = self._ssocket.accept()
		self._csocket.setblocking(1)
		self._csocket.settimeout(None)
		self._csocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
		#print( (ip, port) )

	def close_client_connection(self):
		self._close_client_connection()

	def close_server_connection(self):
		if self._ssocket:
			self._ssocket.close()



""" Testing """
if __name__ == '__main__':
	try:
		print('initialize')
		tcp_server = TCP_Server()
		tcp_server.initialize()
		# Run server continuously...
		while True:
			try:
				print('-----\nwait_for_client')
				tcp_server.wait_for_client()
				# Communicate with client continuously...
				while True:
					msg = tcp_server.receive_msg()
					print(msg)
					tcp_server.send_msg(*msg) #< Send back received msg
			except Exception as e:
				print(e)
			finally:
				print('close_client_connection')
				tcp_server.close_client_connection()
	except Exception as e:
		print(e)
	finally:
		print('close_server_connection')
		tcp_server.close_server_connection()


