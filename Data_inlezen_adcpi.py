#%%
'''                        ADCPi plus
---------------------------------------------------------------
'''
from ADCPi import ADCPi
import time
#Maakt een ADCPi instance
adc = ADCPi(0x68,0x69,14)
#%%
'''                        ADC settings
------------------------------------------------------------------
'''

'Bit rate wordt ingesteld' 

rate = 12 #bit
adc.set_bit_rate(rate)

'conversie mode' 
adc.set_conversion_mode(1)
#%%
'''                          Main loop
------------------------------------------------------------------
'''
while True:
    #leest alle ADC channels in, in een lijst
    values = [0]*9
    for i in range(9):
        values[i] = round(adc.read_voltage(i),2)

    print('| {1:>9} | {2:>9} | {3:>9} | {4:>9} |{5:>9} | {6:>9} | {7:>9} | {8:>9} |'.format(*values))
    time.sleep(0.05)   