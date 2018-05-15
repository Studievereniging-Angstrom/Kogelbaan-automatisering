import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import pandas as pd
import numpy as np
import time as t
from time import sleep
import csv

update_interval = 1000 #in milliseconds
LARGE_FONT = ('Verdana', 12)
style.use(['seaborn'])

f = Figure(figsize=(5,5), dpi=100)
liveplot = f.add_subplot(111)


global xArray,yArray,length
length = 1000
xArray = np.zeros(length) #defining arrays
yArray = np.zeros(length) #defining arrays

global Temp#,Temp1,Temp2,Temp3
Temp = 0
global ref_time, tijd_s, tijd_sList, TempList
ref_time = t.time()
tijd_s = 0
tijd_sList = []
TempList = []

'Instellingen en module ophalen'
##from ADCPi import ADCPi
##adc = ADCPi(0x68,0x69,14) #ADCPI instantie wordt aangemaatk
##rate = 16 #ingestelde bit-rate
##adc.set_bit_rate(rate)
##adc.set_conversion_mode(1) #conversie mode



def animate(i):
    global xArray, yArray, tijd_sList, TempList
    pullData = open('adclogger.csv', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(x)
            yList.append(y)
    liveplot.clear()
##    liveplot.plot(xList, yList)
    liveplot.plot(xArray, yArray)
    liveplot.plot(tijd_sList, TempList)
    liveplot.set_xlabel('tijd [s]')
    liveplot.set_ylabel('Voltage [V]')

    
class Mainframe(tk.Frame):
    #contains the widgets
    def __init__(self,master,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
    # *args packs positional arguments into tuple args
    # **kwargs packs keyword arguments into dict kwargs

        'Widgets worden gedefinieerd'
        'Labels' 
        label1 = ttk.Label(self, text='Voltage:',font=LARGE_FONT).pack(pady=10, padx=10,side='left')

##        'Tempaturen label'  
##        self.Temperature = tk.IntVar()
##        label2 = ttk.Label(self, textvariable = self.Temperature,font=LARGE_FONT).pack(pady=10, padx=10,side='left')        
##        self.TimerInterval = 1000 # ms
##        Temp1 = 0
##        Temp2 = 0 
##        Temp3 = 0 
        
        
        'Buttons' 
        button1 = ttk.Button(self,text='Applicatie sluiten',command=quit).pack(side='left')
####        button3 = ttk.Button(self,text='Test',command=self.test).pack(side='left')
        button4 = ttk.Button(self,text='array_writer',command=self.array_writer).pack(side='left')
        'Live plot' 
        live_plot = FigureCanvasTkAgg(f, self)
        live_plot.get_tk_widget().pack(side='left', fill='both')
        'Toolbar' 
        toolbar = NavigationToolbar2TkAgg(live_plot, self)
        toolbar.update()
        live_plot._tkcanvas.pack(side='left',fill='both')
        live_plot.show()


    def test(self):
        print('test')
        
##    def Read(self):
##        global Temp,Temp1, Temp2, Temp3,ref_time,tijd_s
##        self.Temperature.set(Temp)        
##        Temp = round(adc.read_voltage(0),1)
####        Temp1 = round(adc.read_voltage(0),8)
####        Temp2 = round(adc.read_voltage(0),8)
####        Temp3 = round(adc.read_voltage(0),8)
##        tijd_s += 1 #Elke rondgang tijd + 1
##        tijd_sList.append(tijd_s)
##        TempList.append(Temp) 
##        self.after(self.TimerInterval,self.Read) # and repeat 

        
    def array_writer(self):
        for i in range(1000):
            xValue = i
            yValue = int(100*np.sin(i/100))
            xArray[i] = xValue
            yArray[i] = yValue
            print(str(int(xValue))+str(',')+str(int(yValue))+str('\n'))

            
class App(tk.Tk):
    def __init__(self): #args numbers of variables en kwargs: keyboard arguments, passing through dictionaries
        tk.Tk.__init__(self)

        #set title 
        tk.Tk.wm_title(self, "Live plot")
        #definieer de grote van de app  
        self.geometry('1000x500')
        #maak en pack StartPage
        Mainframe(self).pack()
        
app = App()
ani = animation.FuncAnimation(f, animate, interval=update_interval) #updates by a specified time
app.mainloop()
