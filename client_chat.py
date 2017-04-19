#! /usr/bin/env python
# -*-coding:Utf-8 -*

"""
AUTEUR: SOW THIERNO HAMIDOU
IRC Cleint Chat
1. Ecouter les messages entrants a partir du serveur
2.Verifier l'entrée de l'utilisateur.
"""
import socket, select, string, sys

def prompt():
	sys.stdout.write('<You>')
	sys.stdout.flush()


if __name__ == '__main__':
	
	if(len(sys.argv) < 3) :
		print("Utilisation : python client_chat.py hostname port")
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	#COnnection a lhost
	try:
		s.connect((host, port))
	except :
		print ("Connection etabli")
		sys.exit()

	print("Connecter a lhost, debut d'envoi des messages")
	prompt()

	while 1:
		socket_list = [sys.stdin, s]

		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

		for sock_ready in read_sockets:

			if sock_ready == s:
				data = sock_ready.recv(4096)
				if not data :
					print("\nDeconnection du chat server")
					sys.exit()
				else :

					sys.stdout.write(data)
					prompt()

			else :
				msg = sys.stdin.readline()
				s.send(msg)
				prompt()


