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
from sys import argv
from os import name, system
#FOR::DEPENDENCIES::RUN-># from os import system;system('pip install matplotlib')

#Detect OS
if name == '\x6e\x74': oss = 0
else: oss = 1
    

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

def main(host, amount, sleep_in_seconds, bg_color, b_grid):
    count = 0;timer = [];probe = []
    amount = int(amount)
    sleep_in_seconds = float(sleep_in_seconds)

    #Prepare both lists
    for x in range(0, amount  + 1): probe.append(x)
    for x in range(0, amount): timer.append(0.00)
    probe.pop(0)

    #Create/Show Initial Plot
    plt.rcParams['axes.facecolor'] = bg_color
    plt.title(f"~VisualPing~\n\n{host} @ {sleep_} Seconds Per Probe x {amount}")
    plt.xlabel('\x50\x72\x6f\x62\x65\x20\x23')
    plt.ylabel('\x52\x65\x73\x70\x6f\x6e\x73\x65\x20\x54\x69\x6d\x65\x20\x28\x6d\x73\x29')
    if b_grid == True:
        plt.grid()
    plt.plot(probe, timer)
    plt.show(block=False)
    plt.pause(sleep_in_seconds)

    #Run Loop
    for x in range(0, amount):
        timer.insert(x, int(ping(host)) * 1.00)
        timer.pop(amount)
        
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
    

#ARG-PARSING    
try:
    host = argv[1]
except:
    x = input("Missing Host Argument! Usage: python visualping.py example.com or python visualping.py -h\nHit Enter To Exit...")
    exit()
if host.lower() == "-h":
    x = input("Usage:\n[1] - Basic: python visualping.py <Host>\n[2] - Advanced: python visualping.py <Host> <Probe Amount> <Sleep (In Seconds)> <Background Color> <0=No Grid, 1=Grid>\nHit Enter To Exit...")
    exit()    
try:
    amount = argv[2]
except:
    amount = 12
try:
    sleep_ = argv[3]
except:
    sleep_ = .1
try:
    bg_color = argv[4]
except:
    bg_color = "black"
try:
    b_grid = argv[5]
    if b_grid == "0": b_grid == False
    else: b_grid  = True
except: b_grid = False
    
#IF ALL IS GOOD...
print(f"Pinging {host} @ {sleep_} Seconds Per Break  x {amount}...")    
    
main(host, amount, sleep_, bg_color, b_grid)    
