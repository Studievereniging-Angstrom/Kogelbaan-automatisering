ADC Pi Plus
https://www.abelectronics.co.uk/p/56/ADC-Pi-Plus-Raspberry-Pi-Analogue-to-Digital-converter

Verdere documentatie kan gevonden worden op: 
https://github.com/abelectronicsuk/ABElectronics_Python_Libraries/tree/master/ADCPi

8 channels with 17 conversie 
Deze inputs zijn geschikt van 0 tot 5 V, en zijn single ended input. 
Deze acht channels hebben beide een Microchip MCP3424 A/D converter met vier analoge inputs. 

Deze ADC heeft verbinding met de raspberry pi via het I2C protecol. 

Extra opties van dit bord zijn: 
Er kan een hat bovenop de raspberry pi gezet worden! Er kunnen dus ook andere hats op gezet worden dat niet zozeer een adc converter is! Denk aan de SenseHat
Om het mogelijk te maken om meerdere borden op elkaar te stapelen zijn er adres pinnen (I2C) voor de verschillende analogen kanalen. 

op het board is een referentie voltage van 2.048 volt. 

Versterker
Programmeerbare versterker op het board aanwezig!

De sample rate van dit board is afhankelijk van de ingestelde conversie in bits: 
Bij: 
12 bit - 240 Samples per second (SPS)
13 bit - 60 SPS
16 bit - 15 SPS
18 bit - 3,75 SPS

Verder kan men kiezen uit: enkele en continue conversie
Dit bord maakt het mogelijk om 5Volt I2C apparaten te gebruiken door een buffered 5 V port. 

De README.md staat standaard open in deze repositorys hierin wordt onder andere het gebruik van deze repository uitgelegd. 
Voor het gebruik van de acd moet het pakket smbus zijn geinstalleerd

De code die nodig is om de ADC aan te sturen kan direct van github worden gedownload met 'PIP'. Let op! als men wilt werken in python3 en hoger moet men 'pip3' gebruiken

Enkele nuttige functies zijn: 

read_voltage(channel) (channel 1 to 8) geeft waarden tussen 0 en 5 
set_pga(gain) (1,2,4,8) 
setBitRate(rate) (12,13,16,18???)
set_conversion_mode(mode) (0,1) one-shot of continue 

