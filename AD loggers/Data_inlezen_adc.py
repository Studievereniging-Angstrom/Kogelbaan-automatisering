import time
import numpy as np
import csv
#import matplotlib.pyplot as plt
#%%
'''                           Adafruit_ADS1x15
-----------------------------------------------------------------
'''

import Adafruit_ADS1x15
'Eigen modules' 
from Functies import tijd_verschil,plot,inlezen

adc = Adafruit_ADS1x15.ADS1115() #Een ADS1115 ADC object wordt aangemaakt
ref_time = time.time() #tijd bij het opstarten van het programma
#%%

'''                   ADC   SETTINGS
----------------------------------------------------------
'''
'gain settings' 
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
GAIN = 1
'data_rate settings'
DATA_RATE= 860

#%%
'''                       Main loop
------------------------------------------------------------
'''

while True:
    tijd_s = round(time.time()-ref_time,3)
    
#Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        values[i] = round((adc.read_adc(i, gain=GAIN,data_rate=DATA_RATE))*4.096/32768,3)

#data wordt opgeslagen in het bestand adclogger.csv
    '''with open('adclogger.csv','a') as f:
        w = csv.writer(f)
        w.writerow([tijd_s] + values[0:2])'''
    ###print(tijd_s, '| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))        
    tijd_verschil(values[0],values[1])
time.sleep(0.0001) 
