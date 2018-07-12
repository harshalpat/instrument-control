import visa
import numpy as np
import time
import cv2
s=visa.instrument('USB0::0x0699::0x0353::1613189::INSTR')
def establishconnection(s):
            try :
             print s.ask('*IDN?')
             print ("connection established")
            except Exception as ex:
                
                print "exception raised"
                print (ex)
                
def set_amplitude(s):
            try:
                amp=float(input('enter the amplitude:'))
                while amp>10 or amp<0:
                 if amp>10:
                    print ('enter the amplitude less than 10')
                 elif amp<0:
                    print ('enter the amplitude greater  than 0')
                    amp=float(input('enter the amplitude:'))
                s.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+str(amp)+'Vpp')
                print ("amplitude set to"+str(amp)+"Vpp")
            except Exception as ex:
                        print (ex)
                        
def set_frequency(s):
                        
              try:
                  fre=float(input("enter the frequency:"))
                  while fre>60 or fre<0:
                      if fre>60:
                          print ('enter the frequency less than 60Mhz')
                      elif fre<0:
                          print ('enter the frequency greater  than 0')
                      fre=float(input('enter the frequency:'))
                  s.write('SOURce1:FREQUENCY '+str(fre))
                  print ("frequency set to "+str(fre)+"Mhz")
              except Exception as ex:
                        print (ex)
                        
#sets CH1 source of modulating signal to internal

def set_sinusoidalwaveform():
            try:
                 s.write('SOURce1:FUNCtion SINusoid')
                 print ("sine wave form generated")
            except Exception as ex:
                  print (ex)      

def set_squarewaveform():
             try:
                   s.write('SOURce1:FUNCtion SQUare')     
                   print ("square wave form generated")
             except Exception as ex:
                  print (ex)   

def set_rampwaveform():
             try:
                   s.write('SOURce1:FUNCtion RAMP')     
                   print ("RAMP wave form generated")
             except Exception as ex:
                  print (ex)   

def set_pulsewaveform():
             try:
                   s.write('SOURce1:FUNCtion PULSe')     
                   print ("pulse wave form generated")
             except Exception as ex:
                  print (ex)   
def reset_values():

            s.write('*RST')
            s.write('SOURce1:AM:SOURce INTernal')

def choice():
    print (' 1 for sine wave')
    print (' 2 for square wave')
    print (' 3 for RAMP')
    print (' 4 for Noise')
    ch=int(input('enter your choice:'))
    s.write('SOURce1:AM:SOURce INTernal')
 
 
    if ch==2:
            set_squarewaveform()
    elif ch==1:
            set_sinusoidalwaveform()
    elif ch==3:
            set_rampwaveform()
    elif ch==4:
            set_pulsewaveform()


 

 
 
 
