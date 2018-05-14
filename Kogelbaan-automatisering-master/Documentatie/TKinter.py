'''Tkinter staat voor Tk interface en Tk is een GUI extensie.
In Tkinter heb je een heel arsenaal aan widgets zoals:
- Button
- Canvas
- checkbutton
- combobox
- entry
- frame
- label
- labelframe
- progressbar

etc. etc. Ook kent tkinter verschillende commands waarbij een nieuwe window wordt
geopend zoals:
- tk_getOpenFile waarmee de gebruiker een bestand kan selecteren
- tk_getSaveFile waarmee de gebruiker een bestand kan opslaan

Ook kent Tkinter 3 geometrie managers:
- Place
- Grid  
- Pack
'''

'We beginnnen met Hello world dit doen we doormiddel van de label widget'
##import tkinter as tk #importeren module
##root = tk.Tk()#parent window
##label1 = tk.Label(root,text='Hello world') #label met parent root
##label1.pack() #fit de grote van de window aan de label
##root.mainloop() #window bestaat tot het scherm wordt afgesloten

'laten we eens een afbeelding toevoegen' 
import tkinter as tk 

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
    
root = tk.Tk()
label1 = tk.Label(fg='green')
label1.pack()
counter_label(label1)
button = tk.Button(text='stop',width=25,command=root.destroy)
button.pack()
root.mainloop()








