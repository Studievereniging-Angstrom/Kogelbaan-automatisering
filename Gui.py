'''in this progam the package guizero is being used to install this use pip install 
   in the anaconda prompt. an internet connection is necessary'''
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup

def Text_function():
        welcome_message.set(my_name.get())

def change_text_size(slider_value):
    welcome_message.font_size(slider_value)

'First app is initiated'
app = App(title="Hello world")

welcome_message = Text(app, text="Text with: size/font/color", size=10, font="Times new roman", color="red")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=Text_function, text="PushButton 1")
text_size = Slider(app, command=change_text_size, start=10, end=80)

app.display()
#%%
'Second app is defined'
def choice():     
    print( List_1.get() )
    print( Checkbox_1.get_value() )
    print( ButtonGroup_1.get() )
'second app is initiated'
app2 = App(title = 'Second GUI', width=300 , height=200, layout='grid')

'A list/checkbox/buttongroup are defined in a grid'
List_1 = Combo(app2, options=['List','First_item'], grid = [1,0],align='left')
List_1_text = Text(app2, text="List:", grid=[0,0], align="left")
Checkbox_1 = CheckBox(app2, text="Checkmark", grid=[0,1], align="left")
ButtonGroup_1 = ButtonGroup(app2,options=[['Front', 'Front'],['Middle', 'Middle'], ['Back', 'Back']],selected="M",                                       horizontal=True, grid=[1,3], align="left" )
row_choice_text = Text(app2, text="Which row", grid=[0,3], align="left")
show_choices = PushButton(app2, command=choice, text="Show choices", grid=[0,4], align='left')

app2.display()

