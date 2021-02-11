import socket
import json
 
HOST = 'localhost'
PORT = 5432
 
# สร้าง socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# client ทำการเชื่อมต่อไปยัง server
s.connect((HOST, PORT))

data = s.recv(1024)
data = data.decode('utf-8').replace("'", '"')
print('received:', data)

data = input()

# ส่งข้อมูลไปหา server // แปลงเป็น Byte ด้วย
s.sendall(bytes(data,"utf-8"))
 
# รับข้อมูลที่ส่งมาจาก server //แปลง byte แบบ object เป็น String
data = s.recv(1024)
data = data.decode('utf-8').replace("'", '"')
print('received:', data)
