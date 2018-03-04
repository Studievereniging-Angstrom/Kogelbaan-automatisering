import time
from sense_hat import SenseHat
import matplotlib.pyplot as plt

sense = SenseHat()

tijden = []

for i in  range(3):
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']    
        x = round(x,2)
    
    
        if x >= 0.99:
            start = time.time()
            print(start)
            
        
            while True:
                acceleration = sense.get_accelerometer_raw()
                x = acceleration['x']
                x = round(x,2)
            
            
                if x == -0.95:
                    eind = time.time()
                
                    print(eind)
                  
                    break
            
            tijden.append(round((eind- start),2))        
            break
    
plt.figure(1)    
plt.plot(tijden, '.')
plt.ylabel('Tijden [s]')
plt.grid(True)
plt.show()
        
mean = mean(tijden)


        


