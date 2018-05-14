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
import csv

update_interval = 1000 #in milliseconds
LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

f = Figure(figsize=(5,5), dpi=100)
liveplot = f.add_subplot(111)

def animate(i):
    pullData = open('adclogger.csv', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    zList = []
    iList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(x)
            yList.append(y)
    liveplot.clear()
    liveplot.plot(zList,iList)
    liveplot.plot(xList, yList)
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

        self.Temperature = tk.IntVar()
        label2 = ttk.Label(self, textvariable = self.Temperature,font=LARGE_FONT).pack(pady=10, padx=10,side='left')        
        self.TimerInterval = 500 # ms
        self.Temp = 0 #dummy
        self.GetTemp() # wordt aangeroepen
        
    def GetTemp(self):
##        from ADCPi import ADCPi
##        adc = ADCPi(0x68,0x69,14) #ADCPI instantie wordt aangemaatk
##        rate = 16 #ingestelde bit-rate
##        adc.set_bit_rate(rate)
##        adc.set_conversion_mode(1) #conversie mode
##        ref_time = t.time()
    
        # replace this with code to read sensor
        self.Temperature.set(self.Temp)
##        self.Temp = round(adc.read_voltage(0),8)
        self.Temp +=1        
        
        # Now repeat call
        self.after(self.TimerInterval,self.GetTemp)
    
        
        'Buttons' 
        button1 = ttk.Button(self,text='Applicatie sluiten',command=quit).pack(side='left')
        ##button2 = ttk.Button(self,text='wave form',command=uitlezen_ADCPI).pack(side='left')
        button3 = ttk.Button(self,text='Test',command=self.test).pack(side='left')
        'Live plot' 
        live_plot = FigureCanvasTkAgg(f, self)
        live_plot.get_tk_widget().pack(side='left', fill='both')
        'Toolbar' 
        toolbar = NavigationToolbar2TkAgg(live_plot, self)
        toolbar.update()
        live_plot._tkcanvas.pack(side='bottom',fill='both')
        live_plot.show()        

    def test(self):
        print('test')

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
