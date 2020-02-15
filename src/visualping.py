#!/usr/bin python3

"""
LICENSE

Copyright 2020 [Aerobot Development]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#Meta
__author__ = "AeroBot Development"
__copyright__ = "Copyright 2020, Creative Commons"
__credits__ = ["AeroBot Development"]
__license__ = "MIT, CC"
__version__ = "1.0.0"
__maintainer__ = "AeroBot"
__email__ = "aerobotprofessional@gmail.com"
__status__ = "Open-Source"

import matplotlib.pyplot as plt
import subprocess
from time import sleep
from tkinter import messagebox
from os import name, system, getcwd
from tkinter import *
import tkinter as tk
#FOR::DEPENDENCIES::RUN-># from os import system;system('pip install matplotlib')

#Detect OS
if name == '\x6e\x74': oss = 0
else: oss = 1

class glbls:
    host = None
    amount = None
    sleep_ = None
    bg_color = None
    b_grid = None
    b_label = None
    lbl_clr = None
    bool_ready = None

def flush_globals():
    glbls.host = None
    glbls.amount = None
    glbls.sleep_ = None
    glbls.bg_color = None
    glbls.b_grid = None
    glbls.b_label = None
    glbls.lbl_clr = None
    glbls.bool_ready = None
    

def ping(host):
    global oss
    if oss == 0: ping = subprocess.run(["\x70\x69\x6e\x67",host], stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True, shell=False, creationflags=0x00000008)
    else:
        try:
            ping = subprocess.run(["\x70\x69\x6e\x67","\x2d\x63","\x31",host], stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True, shell=False)
        except Exception as r:
            xx = input(f"Fatal Error: {r}")
            exit()
    try:
        ms = int(ping.stdout.split("\x74\x69\x6d\x65\x3d")[1].split("\x6d\x73")[0])
    except:
        ms = 999
        sleep(1)
    return ms

def main(host, amount, sleep_in_seconds, bg_color, b_grid, b_label, lbl_clr):
    count = 0;timer = [];probe = []
    amount = int(amount)
    sleep_in_seconds = float(sleep_in_seconds)

    #Prepare both lists
    for x in range(0, amount  + 1): probe.append(x)
    for x in range(0, amount): timer.append(0.00)
    probe.pop(0)

    #Create/Show Initial Plot
    try: plt.rcParams['axes.facecolor'] = bg_color
    except: plt.rcParams['axes.facecolor'] = "white"
    plt.title(f"~VisualPing~\n\n{host} @ {sleep_in_seconds} Seconds Per Probe x {amount}")
    plt.xlabel('\x50\x72\x6f\x62\x65\x20\x23')
    plt.ylabel('\x52\x65\x73\x70\x6f\x6e\x73\x65\x20\x54\x69\x6d\x65\x20\x28\x6d\x73\x29')
    
    if b_grid == True: plt.grid()
        
    plt.plot(probe, timer)     
    plt.show(block=False)
    plt.pause(sleep_in_seconds)

    #Run Loop
    for x in range(0, amount):
        timer.insert(x, int(ping(host)) * 1.00)
        timer.pop(amount)
        
        if b_label == True:
            try: plt.text(probe[count],timer[count],f'{timer[count]}\x6d\x73',horizontalalignment='\x72\x69\x67\x68\x74',color=lbl_clr)
            except: plt.text(probe[count],timer[count],f'{timer[count]}\x6d\x73',horizontalalignment='\x72\x69\x67\x68\x74',color="blue")
        plt.plot(probe, timer)
        plt.show(block=False)
        plt.pause(sleep_in_seconds)
        
        count += 1
        if count == amount: break
        
    #Complete, Notify!    
    a = 0    
    for x in range(0, amount): a += timer[x]
    a = round(a / amount, 2)
    f = str(host.replace(".","_").replace("-","_")) + ".png"
    plt.savefig(f)
    messagebox.showinfo("VisualPing", f"Complete!\nProbes Sent: {amount}\nAverage Ping: {a}ms\nImage Saved As {f}")
    plt.plot(probe, timer)
    plt.show(block=True)
    





def start():
    try: host = str(glbls.host.get())
    except Exception as d:
        recover(f"Error: {d}")
        return
    if len(host) <= 3:
        bool_ready = False
        recover("No Input!")
    else: bool_ready = True    
    try: amount = int(glbls.amount.get())
    except: amount = 12
    try: sleep_ = float(glbls.sleep_time.get())
    except: sleep_ = .1
    try: bg_color = glbls.bg_color.get()
    except: bg_color = "white"
    try: label_color = glbls.label_color.get()
    except: label_color = "blue"
    try: b_grid = glbls.bool_grid.get()
    except: b_grid = 0
    try: b_labels = glbls.bool_labels.get()
    except: b_labels = 0
    if bool_ready == True:
        main(host, amount, sleep_, bg_color, b_grid, b_labels, label_color)
        initialize()
    else:
        return

def recover(message):
    initialize(message)

def initialize(message=None):
    flush_globals()
    glbls.bool_grid = IntVar()
    glbls.bool_labels = IntVar()

    #SET ICON / TILE
    master.iconbitmap(f'{getcwd()}\\img\\fav.ico')
    master.title("VisualPing")
    master.configure(bg='grey')

    #SET HEADER IMG'S
    
    tk.Label(master, image=bg_image).grid(row=0, column=0)

    tk.Label(master, text="Host", bg="grey").grid(row=1)
    tk.Label(master, text="Amount", bg="grey").grid(row=2)
    tk.Label(master, text="Sleep Time", bg="grey").grid(row=3)
    tk.Label(master, text="Background Color", bg="grey").grid(row=4)

    glbls.b_grid = Checkbutton(master, text="Use Grid", bg="grey", variable=glbls.bool_grid)
    glbls.b_grid.grid(row=5)

    glbls.b_label = Checkbutton(master, text="Use Labels", bg="grey", variable=glbls.bool_labels)
    glbls.b_label.grid(row=6)

    tk.Label(master, text="Label Color", bg="grey").grid(row=7)

    glbls.host = tk.Entry(master)
    glbls.amount = tk.Entry(master)
    glbls.sleep_time = tk.Entry(master)
    glbls.bg_color = tk.Entry(master)
    glbls.label_color = tk.Entry(master)

    glbls.host.grid(row=1, column=1)
    glbls.amount.grid(row=2, column=1)
    glbls.sleep_time.grid(row=3, column=1)
    glbls.bg_color.grid(row=4, column=1)

    glbls.label_color.grid(row=7, column=1)

    tk.Label(master, text="""===============""", bg="grey").grid(row=8)

    b = tk.Button(master, text="Start", command=start)
    b.grid(row=9, column=0)
    
    if message != None: tk.Label(master, text=f"Logging:\n{message}",justify=LEFT, bg="grey", fg="red").grid(row=9, column=1)
        
    tk.Label(master, text="""===============""", bg="grey"
             ).grid(row=10)

    
master = tk.Tk()
bg_image = PhotoImage(file=getcwd()+"\\img\\bg.png")
initialize()
master.mainloop()

