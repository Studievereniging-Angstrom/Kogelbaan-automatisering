# Kogelbaan automatisering

Om de kogelbaan te automatiseren wordt er gebruik gemaakt van 2 foto diodes en een oscilloscoop. 

Om dit te automatiseren wordt er gebruik gemaakt van de Raspberry Pi. 

De Raspberry Pi is een mini computer met mogelijkheden om data in te lezen!
Omdat de Raspberry Pi alleen beschikt over een set digitale pinnen moet de analoge signalen van de foto diodes omgezet worden 
naar een digitaal signaal via een AD converter. 

Op dit moment kan er gebruik worden gemaakt van twee verschillende AD converters om het signaal te digitaliseren, met name de:
- ADS1115
- ADC Pi Plus

Voor elk van deze converters staat er een Python script in de repository. 
Voor het verwerken en intepreteren van deze data wordt het zogenaamde 'Functie' bestand gebruikt
