import socket
import ssl

# УСТАНОВИТЬ ПЕРЕМЕННЫЕ
packet = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"
HOST, PORT = 'www.google.com', 443

# СОЗДАТЬ СООКЕТ
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

# ОБЕРТЫВАНИЕ РОЗЕТКИ
wrappedSocket = ssl.wrap_socket(sock=sock)

# ПОДКЛЮЧИТЬСЯ И НАпечатать ОТВЕТ
wrappedSocket.connect((HOST, PORT))
wrappedSocket.send(packet)
rec = wrappedSocket.recv(15)

# ЗАКРЫТЬ РАЗЪЕМНОЕ СОЕДИНЕНИЕ
wrappedSocket.close()

# ВЫВОД НА ПЕЧАТЬ

out = rec.decode('utf-8')
print("SSL test output: {}".format(out))
assert out == 'HTTP/1.1 200 OK'
