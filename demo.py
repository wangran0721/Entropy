#输入500000个“啪”
i = 0
for i in range(500000):
    file = open('path/test.txt','a')
    file.write("啪")
    i = i + 1
    file.close()
    
