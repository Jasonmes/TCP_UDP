#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess
#coding=utf-8

# 函数 socket.socket 创建一个 socket，该函数带有两个参数：
# Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
# Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

import socket
# 创建tcp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ...这里是使用套接字的功能（省略）...
# 不用的时候，关闭套接字
s.close()



# 创建一个udp socket（udp套接字）
# 创建udp的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  ...这里是使用套接字的功能（省略）...
# 不用的时候，关闭套接字
s.close()