import socket
print("Запуск сервера", file=open("log.txt", "a"))
sock = socket.socket()
sock.bind(('', 9090))
print("Начало прослушивания порта", file=open("log.txt", "a"))
sock.listen(0)
msg = ''

while True:
	conn, addr = sock.accept()
	print("Подключение клиента", file=open("log.txt", "a"))
	print(addr)
	while True:
		print("Прием данных от клиента", file=open("log.txt", "a"))
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		print("Отправка данных клиенту", file=open("log.txt", "a"))
		conn.send(data)
	print(msg, file=open("log.txt", "a"))
	print("Отключение клиента", file=open("log.txt", "a"))
	conn.close()