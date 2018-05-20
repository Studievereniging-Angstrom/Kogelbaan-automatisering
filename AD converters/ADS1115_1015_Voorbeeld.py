import Adafruit_ADS1x15 #adafruit object wordt aangemaakt
import time
import numpy as np
import matplotlib.pyplot as plt
import csv

adc = Adafruit_ADS1x15.ADS1115() #Een ADS1115 ADC object wordt aangemaakt
##adc = Adafruit_ADS1x15.ADS1015() #Een ADS1115 ADC object wordt aangemaakt
#uncomment bij het gebruik van ADS1015 bovenstaande 
ref_time = time.time() #tijd bij het opstarten van het programma

'settings ADS
'gain instellingen' 
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
GAIN = 1 #instellen amplifier
'Data rates instellingen' 
#data rate moet een van de volgende waarden hebben:
#8, 16, 32, 64, 128, 250, 475, 860 bij de ADS1115
#128, 250, 490, 920, 2400, 3300    bij de ADS1015
DATA_RATE=[ 128,250,490,920,1600,2400,3300]
###DATA_RATE=[8, 16, 32, 64, 128, 250, 475, 860]
DATA_RATE= [-1] #sample rate 


#uncomment deze sectie en commentariseer de andere sectie als je de waarden op het scherm wilt laten printen en wilt laten opslaan 
N=1000
values = np.empty(N) #maakt een array van N elementen aan 
for i in range(N):
    values[i] = adc.read_adc(0, gain=GAIN,data_rate=rate) #maakt een lijst aan met uitgelezen waarden
stop = -ref_time + time.time()
t = np.linspace(0,stop,N)
plt.plot(t,values,'+')
plt.plot(t,values,'r-')
plt.show() #plot de uitgelezen data 

##while True:
##    tijd_s = round(time.time()-ref_time,3) #tijd array     
###Read all the ADC channel values in a list.
##    values = [0]*4
##    for i in range(4):
##        values[i] = round((adc.read_adc(i, gain=GAIN,data_rate=DATA_RATE))*4.096/32768,3)
##    with open('adclogger.csv','a') as f:
##        w = csv.writer(f)
##        w.writerow([tijd_s] + values[0:4]) #data wordt weggeschreven in het bestand adclogger.csv
##    print(tijd_s, '| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values)) #print de data in de consol 

