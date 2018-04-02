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

update_interval = 1000 #in milliseconds


LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open('sampleData.txt', 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)

class Velocity_App(tk.Tk):

    def __init__(self, *args, **kwargs):
        '''When you call upon the class, this will be ALWAYS running.
           args: any number of variables
           kwargs: keyboard arguments, its like your passing through dictionaries.'''

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Velocity Measurement!")

        container = tk.Frame(self) #its basically the frame of the window of the GUI
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} #empty dictionary, you can stuff frames in here

        for F in (StartPage, GraphPage):

            frame = F(container, self) #the first frame you open

            #the frame on top of self.frames is the frame we interact with

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
            #north/east/south/west, it'll stick everything from the center to the size of the window

        #you assign some frame to the grid. you can specify things inside the grid.
        #the grid will be as big as you need it to be

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def load_data(self):
        return animation.FuncAnimation(f, animate, interval=update_interval) #updates every 0.100 seconds

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text='HOME', font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = ttk.Button(self, text='GRAPH',
                            command=lambda: controller.show_frame(GraphPage))
        button1.pack()

        button2 = ttk.Button(self, text='EXIT',
                            command=quit)
        button2.pack()
        
class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label1 = ttk.Label(self, text='GRAPH', font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text='HOME',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        #button2 = ttk.Button(self, text='START READING',
        #                    command=lambda: controller.load_data())
        #button2.pack()
        
        button3 = ttk.Button(self, text='EXIT',
                            command=quit)
        button3.pack()

        label2 = ttk.Label(self, text='v: ... m/s', font=LARGE_FONT)
        label2.pack(pady=10, padx=10)
     
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

app = Velocity_App()
ani = animation.FuncAnimation(f, animate, interval=update_interval) #updates every 0.100 seconds
app.mainloop() 









    
        
        
