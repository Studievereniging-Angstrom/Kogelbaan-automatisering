import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.patches as mpatches

import tkinter as tk
from tkinter import *
from tkinter import ttk

import pandas as pd
import numpy as np
import time as t
from time import sleep
import csv

update_interval = 1000 #in milliseconds
LARGE_FONT = ('Verdana', 12)
style.use(['ggplot'])

f = Figure(figsize=(9,7), dpi=100)
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

        self.TimerInterval = 1000 # ms
        windowframe = tk.Frame.__init__(self,master,*args,**kwargs) #creating the mainframe

        #-------
        
        #frame for the buttons and labels (left)
        butlabframe = Frame(windowframe)
        butlabframe.pack(side='left')
        
        #frame fot the live plot (right)
        plotframe = Frame(windowframe)
        plotframe.pack(side='right')

        #-------

        #defining plot
        live_plot = FigureCanvasTkAgg(f, self)
        live_plot.get_tk_widget().pack(side='right')      
        #toolbar = NavigationToolbar2TkAgg(live_plot, self)
        #toolbar.update()
        live_plot._tkcanvas.pack(side='right')
        live_plot.show()

        #defining buttons
        butt_w = 10
        bg_color = 'SystemButtonFace'
        fg_color = 'black'

        
        but_test = Button(butlabframe,text='TEST',command=self.test,
                          width=butt_w, font=LARGE_FONT,
                          bg=bg_color, fg=fg_color)
        but_test.pack(side='top', fill=X)
        self.hovering(but_test, bg_color, fg_color)


        but_sine = Button(butlabframe,text='SINE',command=self.array_writer,
                          width=butt_w, font=LARGE_FONT,
                          bg=bg_color, fg=fg_color)
        but_sine.pack(side='top', fill=X)
        self.hovering(but_sine, bg_color, fg_color)

        but_save_data = Button(butlabframe,text='SAVE DATA',command=self.save,
                          width=butt_w, font=LARGE_FONT,
                          bg=bg_color, fg=fg_color)
        but_save_data.pack(side='top', fill=X)
        self.hovering(but_save_data, bg_color, fg_color)

        but_save_graph = Button(butlabframe,text='SAVE GRAPH',command=self.graph_save(f),
                          width=butt_w, font=LARGE_FONT,
                          bg=bg_color, fg=fg_color)
        but_save_graph.pack(side='top', fill=X)
        self.hovering(but_save_graph, bg_color, fg_color)
        
        but_exit = Button(butlabframe,text='EXIT',command=quit,
                          width=butt_w, font=LARGE_FONT,
                          bg=bg_color, fg=fg_color)
        but_exit.pack(side='top', fill=X)
        self.hovering(but_exit, bg_color, fg_color)
    
        #defining labels
        self.Temperature1 = tk.IntVar()
        self.Temperature2 = tk.IntVar()
        self.Temperature3 = tk.IntVar()
        self.Temperature4 = tk.IntVar()
        
        labC1A = Label(butlabframe, text='Channel 1 :',font=LARGE_FONT).pack(pady=10, padx=10,side='top')
        labC1B = Label(butlabframe, textvariable = self.Temperature1, font=LARGE_FONT).pack(pady=10, padx=10,side='top')

        labC2A = Label(butlabframe, text='Channel 2 :',font=LARGE_FONT).pack(pady=10, padx=10,side='top')
        labC2B = Label(butlabframe, textvariable = self.Temperature2, font=LARGE_FONT).pack(pady=10, padx=10,side='top')        

        labC3A = Label(butlabframe, text='Channel 3 :',font=LARGE_FONT).pack(pady=10, padx=10,side='top')
        labC3B = Label(butlabframe, textvariable = self.Temperature3, font=LARGE_FONT).pack(pady=10, padx=10,side='top')        

        labC4A = Label(butlabframe, text='Channel 4 :',font=LARGE_FONT).pack(pady=10, padx=10,side='top')
        labC4B = Label(butlabframe, textvariable = self.Temperature4, font=LARGE_FONT).pack(pady=10, padx=10,side='top')        

    def hovering(self, button, bg_color, fg_color):
        button.bind("<Enter>", lambda event, h=button: h.configure(bg="white",fg="black"))
        button.bind("<Leave>", lambda event, h=button: h.configure(bg=bg_color, fg=fg_color))      

    def test(self):
        print('test')

    def nothing(self):
        pass
        
    def read(self):
        global Temp,Temp1, Temp2, Temp3, ref_time, tijd_s
        self.Temperature.set(Temp)
        self.Temperature1.set(Temp1)
        self.Temperature2.set(Temp2)
        self.Temperature3.set(Temp3)
        Temp = round(adc.read_voltage(1),1)
        Temp1 = round(adc.read_voltage(2),1)
        Temp2 = round(adc.read_voltage(3),1)
        Temp3 = round(adc.read_voltage(4),1)

        tijd_s += 1 #Elke rondgang tijd + 1
        tijd_sList.append(tijd_s)
        TempList.append(Temp)
        TempList1.append(Temp1)
        TempList2.append(Temp2)
        TempList3.append(Temp3) 
        self.after(self.TimerInterval,self.read) # and repeat

    def array_writer(self):
        for i in range(250):
            xValue = i
            yValue = int(100*np.sin(i/10))
            xArray[i] = xValue
            yArray[i] = yValue
            ##t.sleep(1)
            print(str(int(xValue))+str(',')+str(int(yValue))+str('\n'))
            
    def save(self):
        appendFile = open('adclogger.csv','a')
        for item in TempList:
            appendFile.write('%s,' % item)
        appendFile.close()

    def graph_save(self, figure):
        tname = t.time()
        figure.savefig("GRAPH"+str(tname)[:10]+str(tname)[11:]+".png")
        
class App(tk.Tk):
    def __init__(self): #args numbers of variables en kwargs: keyboard arguments, passing through dictionaries
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Live plot of Voltage over Time (By Paulus & Luc)")
        self.geometry('1024x640')
        Mainframe(self).pack()
        
app = App()
ani = animation.FuncAnimation(f, animate, interval=update_interval) #updates by a specified time
app.mainloop()
