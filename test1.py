#! /usr/bin/python
# -*-coding: UTF-8 -*-

import socket
import sys


# 判断端口是否开放
def is_open(ip, port):
    s = socket.socket()
    try:
        s.connect(ip, port)
        return True
    except:
        return False


# 默认扫描的函数
def scan(ip, portlist):
    for x in portlist:
        if is_open(ip, x):
            print("%s的主机 %s 端口 open"%(ip,x))
        else:
            print("%s的主机 %s 端口 close"%(ip,x))
    pass

#范围扫描
def rscan(ip,r,e):
    for x in range(int(r),int(e)):
        if is_open(ip,x):
            print("%s的主机 %s 端口 open"%(ip,x))
        else:
            print("%s的主机 %s 端口 close"%(ip,x))
    pass



def main():
    defaultport = ['145','139','445','1433','3306','3389','6379','80','8080','7001','22','21','23','25']

    #寻求帮助或者看版本
    if len(sys.argv)==2:

        if sys.argv[1]=='--help' or sys.argv[1]=='-h':
            print("python test1.py [ip] ----默认扫描")
            print("python test1.py [ip] [port:80,81,82或者port:80-90] ----自定义端口扫描")

        elif sys.argv[1]=='--version' or sys.argv[1]=='-v':
            print("程序版本为1.0")
            sys.exit()

        else:
            #若使用默认扫描：python test1.py 127.0.0.1
            scan(sys.argv[1],defaultport)

    #参数有逗号的情况
    elif len(sys.argv)==3:
        if ',' in sys.argv[2]:
            port_1 = sys.argv[2]
            port_1 = port_1.split(',')
            a = []
            for x in port_1:
                a.append(int(x))

            scan(sys.argv[1],a)

        #带‘-’范围扫描的情况
        elif '-' in sys.argv[2]:
            rport = sys.argv[2]
            rport = rport.split('-')
            r = rport[0]
            e = rport[1]

            rscan(sys.argv[1],r,e)







    pass


if __name__ == '__main__':
    main()
