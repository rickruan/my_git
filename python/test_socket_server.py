# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Rick Ruan'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina_html','wb') as fi:
    fi.write(html)