import socket
import json
 
HOST = 'localhost'
PORT = 5432
 
# จากข้อ 1 : สร้าง socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# จากข้อ 4 : client ทำการเชื่อมต่อไปยัง server
s.connect((HOST, PORT))

print('Input PATH to data (status,humanity,sound,temperature,time,true temp) ->> ')
data = input()

# ส่งข้อมูลไปหา server
s.sendall(bytes(data,"utf-8"))
 
# รับข้อมูลที่ส่งมาจาก server
data = s.recv(1024)
data = data.decode('utf-8').replace("'", '"')
print('received:', data)
