#! /usr/bin/env python
# -*-coding:Utf-8 -*
"""
AUTEUR : SOW THIERNO HAMIDOU
IRC Serveur Chat
1-  Accepter les connexions entrantes multiples pour le client. 
2-  Lire les messages entrants de chaque client et de les diffuser à tous les autres clients connectés.

"""
import socket, select

def diffussion_msg(sock, message):
	for socket in liste_connect:
		if socket != server_socket and socket != sock :
			try:
				socket.send(message)
			except :
				socket.close()
				liste_connect.remove(socket)


if __name__ == '__main__':
	
	liste_connect = []
	buff = 4096
	port = 50000

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("0.0.0.0",port))
	server_socket.listen(10)

	liste_connect.append(server_socket)

	print "Chat server sur le port %d " %(port)

	while 1:

		read_sockets, write_sockets,error_sockets = select.select(liste_connect, [], [])

		for sock in read_sockets:

			if sock == server_socket:
				sockfd, addr, = server_socket.accept()
				liste_connect.append(sockfd)
				print "Client (%S, %s) connected "%(addr)

				diffussion_msg(sockfd, "[%s:%s] est dans la discussion\n" % addr)
			else :
				try:
					data = sock.recv(buff)
					if data:
						diffussion_msg(sock, "\r" + '<' + str(sock.getpeername()) + '>' + data)

				except :
					diffussion_msg(sock, "Client (%s,%s) est horsligne" % addr)
					print "Client (%s,%s) hors ligne" % addr
					sock.close()
					liste_connect.remove(sock)
					continue

	server_socket.close()
