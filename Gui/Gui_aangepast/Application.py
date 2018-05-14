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
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(x)
            yList.append(y)
    liveplot.clear()
    liveplot.plot(xList, yList)
    liveplot.set_xlabel('tijd [s]')
    liveplot.set_ylabel('Voltage [V]')
    
def uitlezen_ADCPI(Print=False):
    from ADCPi import ADCPi
    adc = ADCPi(0x68,0x69,14) #ADCPI instantie wordt aangemaatk
    rate = 16 #ingestelde bit-rate
    adc.set_bit_rate(rate)
    adc.set_conversion_mode(1) #conversie mode
    ref_time = t.time()
        
    while Print==True:
        #leest alle adc channels in
        values = [0]*9
        for i in range(9):
            values[i] = round(adc.read_voltage(i),2)
        print('| {1:>9} |{2:>9} |{3:>9} |{4:>9} |{5:>9} |{6:>9} |{7:>9} | {8:>9} |'.format(*values))
    while Print==False:
        #leest alle ADC channels in, in een lijst
        tijd_s = round(t.time()-ref_time,3) 
        values = round(adc.read_voltage(0),8)
        with open('adclogger.csv','a') as f:
                w = csv.writer(f)
                w.writerow([tijd_s] + [values])
class Main(tk.Tk):
    def __init__(self, *args, **kwargs): #args numbers of variables en kwargs: keyboard arguments, passing through dictionaries
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Live plot")

        main_container = tk.Frame(self) #its basically the frame of the window of the GUI
        main_container.pack(side='top', fill='both', expand = True)
        
        
        ##top_frame = tk.Frame(self, background='green').pack(side='top', fill='x', expand=False)
        ##bottom_frame = tk.Frame(self, background='yellow').pack(side='bottom', fill='both', expand=True)

        self.frames = {} #empty dictionary, you can stuff frames in here
        
        for F in (StartPage, GraphPage):
            frame = F(main_container, self) #the first frame you open
            self.frames[F] = frame #frame you interact with 
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        'Widgets worden gedefinieerd'
        'Labels' 
        label1 = ttk.Label(self, text='Voltage:',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
        label2 = ttk.Label(self, text='Update',font=LARGE_FONT).pack(pady=10, padx=10,side='left')
        'Buttons' 
        button1 = ttk.Button(self,text='2e frame',command=lambda: controller.show_frame(GraphPage)).pack(side='left')
        button2 = ttk.Button(self,text='Applicatie sluiten',command=quit).pack(side='left')
        button3 = ttk.Button(self,text='wave form',command=uitlezen_ADCPI).pack(side='left')
        'Live plot' 
        live_plot = FigureCanvasTkAgg(f, self)
        live_plot.get_tk_widget().pack(side='left', fill='both')
        'Toolbar' 
        toolbar = NavigationToolbar2TkAgg(live_plot, self)
        toolbar.update()
        live_plot._tkcanvas.pack(side='bottom',fill='both')
        live_plot.show()        

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):

        'Widgets worden gedefinieerd'
        tk.Frame.__init__(self,parent)
        'labels' 
        label1 = ttk.Label(self, text='2e frame', font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        'buttons' 
        button1 = ttk.Button(self, text='1e frame',command=lambda: controller.show_frame(StartPage)).pack()
        button2 = ttk.Button(self, text='Applicatie sluiten',command=quit).pack()
        
app = Main()
ani = animation.FuncAnimation(f, animate, interval=update_interval) #updates by a specified time
app.mainloop()
