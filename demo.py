#author = ‘wangran0721’
#输入500000个“啪”
i = 0
for i in range(500000):
    file = open('path/test.txt','a')
    file.write("啪")
    i = i + 1
    file.close()
    
#随机输入500000个汉字
# encoding=utf8  
import sys  
  
reload(sys)  
sys.setdefaultencoding('utf8')

from random import randint as rint

i = 0 
file = open('path/test.txt','w+')
for i in range(500000):
	print>>file,unichr(rint(19968,40869)),
	i = i + 1
