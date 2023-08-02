#!/usr/bin/python 
#-*-coding:utf-8-*- 
import binascii
from termcolor import colored,cprint
from colorama import init
init(autoreset=True)

i = open("out.txt","r")
cprint("[日志]文件打开成功...","yellow")
#读取全部内容
Bud = i.read()
cprint("[日志]文件读取内容成功...","yellow")
i.close

#以下为解密部分：
Bud = Bud.replace("释迦牟尼曾言曰：","")
def dec(a,b):
	global Bud
	Bud = Bud.replace(b, a)
	cprint("[日志]"+b+"部分转换完成","yellow")
dec('0','阿')
dec('1','叶')
dec('2','多')
dec('3','伽')
dec('4','行')
dec('5','日')
dec('6','土')
dec('7','加被')
dec('8','南无')
dec('9','般若')
dec('A','他')
dec('B','法')
dec('C','隅')
dec('D','系念')
dec('E','楼观')
dec('F','无间地狱')
dec(' ','，')
cprint("[日志]全部字符转换完成","yellow")

data = binascii.unhexlify(Bud.replace(" ",""))
fp = open("2.mp4","wb")
fp.write(data)
fp.close()
