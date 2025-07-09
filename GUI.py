import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from guizero import App, Text, PushButton, TextBox, Window, Box , Combo
from K3L import K3L
from O2DAI import O2DAI
from O2DAO import O2DAO 
from O3DAI import O3DAI
from O2DI import O2DI
from O2DO import O2DO
from OAT import OAT
from O3DAO import O3DAO
from ORP3DI import ORP3DI
from ORP3DO import ORP3DO
from ORP3DO import ORP3DO
from ORPI import ORPI
from ORPO import ORPO 
from S import S
from guizero import App, PushButton, Window
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import math

   


def show_matplotlib_graph(app,graph):
    #app.hide()
    app_graph = Window(app, "Matplotlib Graph in GUI", width=600, height=600)
    box = Box(app_graph)

    fig, ax = plt.subplots()
    graph()
    canvas = FigureCanvasTkAgg(plt.gcf(), master=box.tk)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    def go_back():
        app_graph.destroy()
        app.show()

    back_button = PushButton(box, go_back, text="Back")
    back_button.tk.pack()

    #app_graph.set_full_screen()


def show_matplotlib_graph3(app,graph,p,q):
   # app.hide()
    app_graph = Window(app, "Matplotlib Graph in GUI2", width=600, height=400)
    box = Box(app_graph)

    fig, ax = plt.subplots()
    graph(p,q)
    canvas = FigureCanvasTkAgg(plt.gcf(), master=box.tk)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    def go_back():
        app_graph.destroy()
        app.show()

    back_button = PushButton(box, go_back, text="Back")
    back_button.tk.pack()

    #app_graph.set_full_screen()
    
    

def show_matplotlib_graph2(app,graph,p):
   # app.hide()
    app_graph = Window(app, "Matplotlib Graph in GUI2", width=600, height=400)
    box = Box(app_graph)

    fig, ax = plt.subplots()
    graph(p)
    canvas = FigureCanvasTkAgg(plt.gcf(), master=box.tk)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    def go_back():
        app_graph.destroy()
        app.show()

    back_button = PushButton(box, go_back, text="Back")
    back_button.tk.pack()

    #app_graph.set_full_screen()


def go_back(app_graph, app):
    app_graph.destroy()
    app.show()

def O2Dopt(app):
    #app.hide()
    Orbits = Window(app,title = '2D orbit option')
    inner = PushButton(Orbits,text='Inner 5 planets',command=show_matplotlib_graph,args=[app,O2DI])
    outer = PushButton(Orbits,text='Outer 4 planets',command=show_matplotlib_graph,args=[app,O2DO])

def O2DAopt(app):
    #app.hide()
    Orbits = Window(app,title = '2D animation orbit option')
    inner = PushButton(Orbits,text='Inner 5 planets',command=O2DAopt2,args=[Orbits,O2DAI])
    outer = PushButton(Orbits,text='Outer 4 planets',command=O2DAopt2,args=[Orbits,O2DAO])

def O2DAopt2(Orbits,model):
    Orbits.hide()
    model()



def O3DAopt(app):
    #app.hide()
    Orbits = Window(app,title = '3D animation orbit option')
    inner = PushButton(Orbits,text='Inner 5 planets',command=O3DAopt2,args=[Orbits,O3DAI])
    outer = PushButton(Orbits,text='Outer 4 planets',command=O3DAopt2,args=[Orbits,O3DAO])

def O3DAopt2(Orbits,model):
    Orbits.hide()
    model()


def OATopt(app):
    #app.hide()
    Orbits = Window(app,title = 'Orbit angle vs Time option')
    intro = Text(Orbits,text='choose a planet to view the orbit angle vs time')
    planets = Combo(Orbits,options=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'],command=OATopt2)

def OATopt2(planet):
    show_matplotlib_graph2(app,OAT,planet)

def Sopt(app):
    global Orbits
    Orbits = Window(app,title = 'Choose first planet')
    intro = Text(Orbits,text='choose first planet')
    planet = Combo(Orbits,options=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'],command=Sopt2)

def Sopt2(planet):
    global planet1
    planet1 = planet
    intro = Text(Orbits,text='choose second planet')
    planet2 = Combo(Orbits,options=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'],command=Sopt3)

def Sopt3(planet2):
    Orbits.hide()
    S(planet1,planet2)

def ORPopt(app):
    #app.hide()
    Orbits = Window(app,title = 'Choose Planet to orbit around')      
    inner = PushButton(Orbits,text='Inner 5 planets',command=ORPopt2,args=[app,ORPI])
    outer = PushButton(Orbits,text='Outer 4 planets',command=ORPopt2,args=[app,ORPO])

def ORPopt2(app,plan):
    global plans
    plans = plan
    print(plans)
    global Orbits
    Orbits = Window(app,title = 'Choose planet to orbit')
    intro = Text(Orbits,text='choose centre planet')
    if plans == ORPI:
        planet = Combo(Orbits,options=['Mercury','Venus','Earth','Mars','Jupiter'],command=ORPpt3)
    else:
        planet = Combo(Orbits,options=['Saturn','Uranus','Neptune','Pluto'],command=ORPpt3)

        
def ORPpt3(planet):
    Orbits.hide()
    show_matplotlib_graph2(app,plans,planet)

def ORP3Dopt(app):
    #app.hide()
    Orbits = Window(app,title = 'Choose Planet to orbit around')    
    inner = PushButton(Orbits,text='Inner 5 planets',command=ORP3Dopt2,args=[app,ORP3DI])
    outer = PushButton(Orbits,text='Outer 4 planets',command=ORP3Dopt2,args=[app,ORP3DO])

def ORP3Dopt2(app,plan):
    global plans
    plans = plan
    print(plans)
    global Orbits
    Orbits = Window(app,title = 'Choose planet to orbit')
    intro = Text(Orbits,text='choose centre planet')
    if plans == ORP3DI:
        planet = Combo(Orbits,options=['Mercury','Venus','Earth','Mars','Jupiter'],command=ORP3Dopt3)
    else:
        planet = Combo(Orbits,options=['Saturn','Uranus','Neptune','Pluto'],command=ORP3Dopt3)

        
def ORP3Dopt3(planet):
    Orbits.hide()
    show_matplotlib_graph2(app,plans,planet)





def mainMenu():
    global app
    app = App(layout='grid', title='Main Menu')

    intro = Text(app, text='Hello, This project was created by Ujesh Sakariya and Harry Atkin', grid=[1, 0])
    intro2 = Text(app, text='Below are the options to view the required tasks for the BPHO', grid=[1, 2])
    intro3 = Text(app, text='We have gone a step further and created a GUI where users can change the parameters to view different models', grid=[1, 3])

    button_width = 30  # Set a common width for all buttons

    K3L1 = PushButton(app, command=show_matplotlib_graph, args=[app, K3L], text='Keplars third law', grid=[0, 4], width=button_width)
    O2D1 = PushButton(app, command=O2Dopt, args=[app], text='2D orbits', grid=[0, 5], width=button_width)
    O2DA1 = PushButton(app, command=O2DAopt, args=[app], text='2D animation orbits', grid=[0, 6], width=button_width)
    O3DA1 = PushButton(app, command=O3DAopt, args=[app], text='3D animation orbits', grid=[0, 7], width=button_width)
    OAT1 = PushButton(app, command=OATopt, args=[app], text='Orbit Angle vs Time', grid=[0, 8], width=button_width)
    S1 = PushButton(app, command=Sopt, args=[app], text='Spirographs', grid=[0, 9], width=button_width)
    ORP1 = PushButton(app, command=ORPopt, args=[app], text='Orbits relative to different planets in 2D', grid=[0, 10], width=button_width)
    ORP3D1 = PushButton(app, command=ORP3Dopt, args=[app], text='Orbits relative to different planets in 3D', grid=[0, 11], width=button_width)

    app.set_full_screen()

    exit_button = PushButton(app, app.destroy, text="Exit", grid=[11, 0])

    app.display()

mainMenu()
