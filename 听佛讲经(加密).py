#-*- coding: UTF-8 -*-
from termcolor import colored,cprint
from colorama import init
init(autoreset=True)
import time
#打开二进制文件
i = open("1.mp4","rb")
cprint("[日志]文件打开成功...","yellow")
#读取全部内容
binarySystem = i.read()
cprint("[日志]文件读取内容成功...","yellow")
#关闭文件
i.close


cprint("[日志]文件已关闭...","yellow")
cprint("[提示]将于3秒后开始16进制转化...","green")
time.sleep(3)
#转大写十六进制格式
lin = ['%02X' % i for i in binarySystem]
textstr=" ".join(lin)


#写入
#data = binascii.unhexlify(textstr.replace(" ",""))
#fp = open("2.mp4","wb")
#fp.write(data)
#fp.close()
cprint("[日志]转换完成","yellow")


#以下为加密部分：
def enc(a,b):
	global textstr
	textstr= textstr.replace(a, b)
	cprint("[日志]"+a+"部分转换完成","yellow")
enc('0','阿')
enc('1','叶')
enc('2','多')
enc('3','伽')
enc('4','行')
enc('5','日')
enc('6','土')
enc('7','加被')
enc('8','南无')
enc('9','般若')
enc('A','他')
enc('B','法')
enc('C','隅')
enc('D','系念')
enc('E','楼观')
enc('F','无间地狱')
enc(' ','，')
cprint("[日志]全部字符转换完成","yellow")

fp = open("out.txt","w")
fp.write("释迦牟尼曾言曰："+textstr)
fp.close()
cprint("[日志]转换完成","yellow")