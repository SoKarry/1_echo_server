import socket
print("Запуск сервера")
sock = socket.socket()
sock.bind(('', 9090))
print("Начало прослушивания порта")
sock.listen(0)
conn, addr = sock.accept()
print("Подключение клиента")
print(addr)

msg = ''

while True:
	print("Прием данных от клиента")
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	print("Отправка данных клиенту")
	conn.send(data)

print(msg)
print("Отключение клиента")
conn.close()
print("Остановка сервера")