from ADCPi import ADCPi #Aanroepen Adlogger
import time
import csv

adc = ADCPi(0x68,0x69,14) #Maakt een ADCPi instance
ref_time = time.time() - 1 

'instellingen' 
rate = 16 #bit rate instellen
adc.set_bit_rate(rate)
adc.set_conversion_mode(1) 

'main loop'
while True:
    #leest alle ADC channels in, in een lijst
    #en schrijft deze weg 
    tijd_s = round(time.time()-ref_time,3) 
    values = round(adc.read_voltage(0),8)
    with open('adclogger.csv','a') as f:
            w = csv.writer(f)
            w.writerow([tijd_s] + [values])
    print(values)

#uncomment deze sectie en commentariseer de andere sectie als je de waarden op het scherm wilt laten printen 
##while True:
##    #leest alle channels in
##    #en print deze
##    values = [0]*9
##    for i in range(9):
##        values[i] = round(adc.read_voltage(i),2)
##    print('| {1:>9} |{2:>9} |{3:>9} |{4:>9} |{5:>9} |{6:>9} |{7:>9} | {8:>9} |'.format(*values))
 
