import random as r
import time as t
import numpy as np

text = ''
saveFile = open('adclogger.csv', 'w')
saveFile.write(text)
saveFile.close()

length = 1000
xArray = np.zeros(length) #defining arrays
yArray = np.zeros(length) #defining arrays
def array_writer(length):
    for i in range(length):
        xValue = i
        yValue = int(100*np.sin(i/100))

        xArray[i] = xValue
        yArray[i] = yValue

    for i in range(length):
        xValue = xArray[i]
        yValue = yArray[i]
        
        newData = str(int(xValue))+str(',')+str(int(yValue))+str('\n')
        appendMe = newData
        appendFile = open('adclogger.csv','a')
        appendFile.write(appendMe)
        appendFile.close()

        t.sleep(0.1)
        print(newData)
array_writer(length)
            
