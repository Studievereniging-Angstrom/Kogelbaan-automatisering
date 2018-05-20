ADC ADS1115 en ADS1015 
(De ADS1015 is nagenoeg hetzelfde als ADS1115 behalve dat de sample rates wat hoger zijn en de resolutie wat lager is)

Kopen:
http://adafru.it/1085

Tutorial voor Configuratie
https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ds1115

Voor voorbeeld code bij deze converter:
https://github.com/adafruit/Adafruit_Python_ADS1x15

een goede tutorial voor data logging is: 
http://openlabtools.eng.cam.ac.uk/Resources/Datalog/RPi_ADS1115/

Specifications ADS1115
16 Bit |860samples/second| I2C
 
- 4 single-ended input channels
- 2 differential input channels

-Programmable amplifier Amax = 16x 
Power supply from 2 - 5 Dc voltage 

Interface gaat via I2C

Aansluitingen
Ground to ground
VDD to logic power supply (2 to 5 DC voltage)
SCL/SDA to I2C  Pin 

single ended meet tussen a0-a3 en ground

Let op! bij het gebruik van python 3.5 moet je  
pip3 install <package> gebruiken
bij het gebruik van python 2.7
(dit is belangrijk bij het installeren van de pakketten in python voor deze sensor) 

Output ADC
De output van de sensor is een getal tussen +-32768. 0 betekent de ground
signaal max +-4.096 

Handige tabel:
table 9 config register(sps) in datasheet

Tot nu toe wordt de gespecificeerde snelheid van deze AD loggers niet gehaald. Hier moet meer onderzoek naar worden gedaan!








