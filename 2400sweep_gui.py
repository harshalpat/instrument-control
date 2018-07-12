# Import necessary packages
from pymeasure.instruments.keithley import Keithley2400
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from time import sleep
from Tkinter import *

top=Tk()


Label_1=Label(top,text='port num:')
Label_2=Label(top,text='compliance voltage:')
Label_3=Label(top,text='datapoints:')
Label_4=Label(top,text='minimum current:')
Label_5=Label(top,text='maximum current:')

Label_1.grid(row=0,sticky=E)
Label_2.grid(row=1,sticky=E)
Label_3.grid(row=2,sticky=E)
Label_4.grid(row=3,sticky=E)
Label_5.grid(row=4,sticky=E)


e1=Entry(top)
e2=Entry(top)
e3=Entry(top)
e4=Entry(top)
e5=Entry(top)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)

b1=Button(top,text='SUBMIT',width=10, command=main)
b1.grid(row=5,columnspan=2)


# Set the input parameters
p=int(e1.get())   #port number
c=float(e2.get())  #compliance voltage
d=int(e3.get())   #datapoints
imin=float(e4.get())  #minimum current
imax=float(e5.get())   #maximum current

def main():
   fp=open("sweepi.txt","w") 
  keithley = Keithley2400("GPIB::"+p)
  keithley.reset()
  keithley.use_front_terminals()
  keithley.apply_current()                # Sets up to source current
  keithley.measure_voltage(auto_range=True)
  ##keithley.source_current_range = 1e-6   # Sets the source current range to 10 mA
  keithley.compliance_voltage = c        # Sets the compliance voltage to 10 V
  keithley.enable_source()
  currents = np.linspace(imin, imax, num=d)
  voltages = np.zeros_like(currents)

keithley.shutdown()# Ramps the current to 0 mA and disables output

  
  fp.write("current voltage\n")
  for i in range(d):
     keithley.source_current = currents[i]
     voltages[i] = keithley.voltage
     fp.write(currents[i])
     fp.write(" ")
     fp.write(voltages[1])
     fp.write("\n")
fp.close()

   
for i in range(d):
  x1.append(voltages[i])       
  print(currents[i])

plt.plot(x1,currents,label = "line 1")
 
# naming the x axis
plt.xlabel('VOLTAGE')
# naming the y axis
plt.ylabel('CURRENT')

# setting x and y axis range
plt.ylim(0,1)
plt.xlim(0,10)

# giving a title to my graph
plt.title('sweep IV graph')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()


top.mainloop()




   
