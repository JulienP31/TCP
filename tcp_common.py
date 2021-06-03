""" TCP common (server/client) class definition """

import socket



""" Class definition """
class TCP_Common(object):
	def __init__(self):
		self._port = 1234
		self._csocket = None
		self._msg_id_len = 1
		self._data_size_len = 2
		self._max_data_len = 8192 - (self._msg_id_len + self._data_size_len)

	def receive_msg(self):
		# Msg ID
		bytes = self._csocket.recv(self._msg_id_len)
		if bytes == b'':
			raise RuntimeError("TCP connection broken ! [msg_id]")
		msg_id = self.bytes_to_int(bytes)
		# Data size
		bytes = self._csocket.recv(self._data_size_len)
		if bytes == b'':
			raise RuntimeError("TCP connection broken ! [data_size]")
		data_size = self.bytes_to_int(bytes)
		# Data
		if data_size > self._max_data_len:
			raise ValueError("Invalid data size !")
		elif data_size > 0:
			data = self._csocket.recv(data_size)
			if data == b'':
				raise RuntimeError("TCP connection broken ! [data]")
		else: #< data_size == 0
			data = b''
		return (msg_id, data_size, data)

	def send_msg(self, msg_id, data_size=0, data=b''):
		# Msg ID
		self._csocket.sendall( self.int_to_bytes(msg_id, self._msg_id_len) )
		# Data size
		self._csocket.sendall( self.int_to_bytes(data_size, self._data_size_len) )
		# Data
		self._csocket.sendall(data)

	def int_to_bytes(self, src, len=1):
		return src.to_bytes(len, byteorder='big', signed=False)

	def bytes_to_int(self, src):
		return int.from_bytes(src, byteorder='big', signed=False)

	def str_to_bytes(self, src):
		return src.encode('ascii')

	def bytes_to_str(self, src):
		return src.decode('ascii')

	def _close_client_connection(self):
		if self._csocket:
			self._csocket.close()


