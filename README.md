De Raspberry Pi is een mini computer met mogelijkheden om data in te lezen!
Omdat de Raspberry Pi alleen beschikt over een set digitale pinnen moet het analoge signaal afkomstig van de sensoren 
eerst geconverteerd worden via een AD converter
 
Op dit moment kan er gebruik worden gemaakt van 3 verschillende AD converters om het signaal te digitaliseren, met name de:
- ADS1115
- ADS1015
- ADC Pi Plus

Voor elk van deze converters staat er wat voorbeeld code om de converter uit te lezen 

Het uiteindelijk gerealiseerde product van de automatisering is een interactief programma een zogenaamde Gui 
(Graphical user interface) 

Deze functies worden gebruikt in een Interactief programma: 'Applicatie.py' 

Deze applicatie kan op dit moment de ADC Pi Plus uitlezen en real time plotten. 
Ook kan de data die binnenkomt opgeslagen worden in een csv bestand. 
In principe zou ook gebruik gemaakt kunnen worden van de ADS1115 en ADS1015. Dit is nog niet gerealiseerd. 

Dit geheel kan gebruikt	worden voor het moniteren van metingen. Met name redelijk statische metingen (25-40 Hz). 
Bij dit soort snelheden met je denken aan temperatuur metingen etc. 
 
Volgens de datasheets van de AD loggers zijn hogere snelheden haalbaar. Dit bleek echter nog niet haalbaar. 
Hier wordt nader onderzoek naar gedaan 