import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.patches as mpatches

import tkinter as tk
from tkinter import ttk

import pandas as pd
import numpy as np
import time as t
from time import sleep
import csv

update_interval = 1000 #in milliseconds
LARGE_FONT = ('Verdana', 12)
style.use(['ggplot'])

f = Figure(figsize=(5,5), dpi=100)
liveplot = f.add_subplot(111)


global xArray,yArray,length
length = 1000
xArray = np.zeros(length) #defining arrays
yArray = np.zeros(length) #defining arrays

global Temp,Temp1,Temp2,Temp3
Temp = 0
Temp1 = 0
Temp2 = 0 
Temp3 = 0 
        
global ref_time, tijd_s, tijd_sList
global TempList, TempList1, TempList2,TempList3
ref_time = t.time()
tijd_s = 0
tijd_sList = []
TempList = []
TempList1 = []
TempList2 = []
TempList3 = []

'Instellingen en module ophalen'
##from ADCPi import ADCPi
##adc = ADCPi(0x68,0x69,14) #ADCPI instantie wordt aangemaatk
##rate = 16 #ingestelde bit-rate
##adc.set_bit_rate(rate)
##adc.set_conversion_mode(1) #conversie mode



def animate(i):
    global  tijd_sList##,xArray, yArray
    global TempList,TempList1, TempList2,TempList3
    liveplot.plot(xArray, yArray,color='r')

##    data1 = mpatches.Patch(color = 'r', label='Kanaal 1')
##    liveplot.plot(tijd_sList, TempList, color='r')
##    data2 = mpatches.Patch(color = 'b', label='Kanaal 2')
##    liveplot.plot(tijd_sList, TempList1,color='b')
##    data3= mpatches.Patch(color = 'y', label='Kanaal 3')
##    liveplot.plot(tijd_sList, TempList2,color='y')
##    data4 = mpatches.Patch(color = 'g', label='Kanaal 4')
##    liveplot.plot(tijd_sList, TempList3, color='g')
##    liveplot.legend(handles=[data1,data2,data3,data4])
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
        

##        'Tempaturen label'  
##        self.Temperature = tk.IntVar()
##        self.Temperature1 = tk.IntVar()
##        self.Temperature2 = tk.IntVar()
##        self.Temperature3 = tk.IntVar()
##        label1 = ttk.Label(self, text='Channel 1 :',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
##        label2 = ttk.Label(self, textvariable = self.Temperature,font=LARGE_FONT).pack(pady=10, padx=10,side='left')
##        label1 = ttk.Label(self, text='Channel 2 :',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
##        label3 = ttk.Label(self, textvariable = self.Temperature1,font=LARGE_FONT).pack(pady=10, padx=10,side='left')        
##        label4 = ttk.Label(self, text='Channel 3 :',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
##        label6 = ttk.Label(self, textvariable = self.Temperature2,font=LARGE_FONT).pack(pady=10, padx=10,side='left')        
##        label5 = ttk.Label(self, text='Channel 4 :',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
##        label7 = ttk.Label(self, textvariable = self.Temperature3,font=LARGE_FONT).pack(pady=10, padx=10,side='left')        
        self.TimerInterval = 1000 # ms
        
        
        'Buttons' 
        button1 = ttk.Button(self,text='Applicatie sluiten',command=quit).pack(side='left')
        button3 = ttk.Button(self,text='Test',command=self.test).pack(side='left')
        button4 = ttk.Button(self,text='Test_sinus',command=self.array_writer).pack(side='left')
##        button4 = ttk.Button(self,text='ADC read',command=self.Read).pack(side='left')
        button4 = ttk.Button(self,text='Save data',command=self.Save).pack(side='left')
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
##        self.Temperature1.set(Temp1)
##        self.Temperature2.set(Temp2)
##        self.Temperature3.set(Temp3)
##        Temp = round(adc.read_voltage(1),1)
##        Temp1 = round(adc.read_voltage(2),1)
##        Temp2 = round(adc.read_voltage(3),1)
##        Temp3 = round(adc.read_voltage(4),1)
##
##        tijd_s += 1 #Elke rondgang tijd + 1
##        tijd_sList.append(tijd_s)
##        TempList.append(Temp)
##        TempList1.append(Temp1)
##        TempList2.append(Temp2)
##        TempList3.append(Temp3) 
##        self.after(self.TimerInterval,self.Read) # and repeat 

        
    def array_writer(self):
        for i in range(1000):
            xValue = i
            yValue = int(100*np.sin(i/100))
            xArray[i] = xValue
            yArray[i] = yValue
            print(str(int(xValue))+str(',')+str(int(yValue))+str('\n'))
            
    def Save(self):
        appendFile = open('adclogger.csv','a')
        for item in TempList:
            appendFile.write('%s,' % item)
        appendFile.close()
        
class App(tk.Tk):
    def __init__(self): #args numbers of variables en kwargs: keyboard arguments, passing through dictionaries
        tk.Tk.__init__(self)

        #set title 
        tk.Tk.wm_title(self, "Live plot")
        #definieer de grote van de app  
        self.geometry('2000x500')
        #maak en pack StartPage
        Mainframe(self).pack()
        
app = App()
ani = animation.FuncAnimation(f, animate, interval=update_interval) #updates by a specified time
app.mainloop()
