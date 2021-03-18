import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
port = int(input('Введите номер порта: '))
host = input('Введите хост: ')

print("Соединение с сервером", file=open("log.txt", "a"))
sock.connect((host, port))
while True:
    msg = input('Введиты строку для передачи или exit для выхода: ')
    if msg == 'exit':
        break
    print("Отправка данных серверу", file=open("log.txt", "a"))
    sock.send(msg.encode())

    print("Прием данных от сервера", file=open("log.txt", "a"))
    data = sock.recv(1024)
    print(data.decode())

print("Разрыв соединения с сервером", file=open("log.txt", "a"))