# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 17:58:49 2016

@author: Samuel Sellberg
"""
from  scipy import *
from  pylab import *
from JASIClass import *
from JASI_maneuvering import *
import pickle
import time
# import RPi.GPIO as GPIO
# (import all functions)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# GPIO.setup(All GPIOs)
hs=0.0015
HS=GPIO.PWM('högerservo-pin',1/(hs+0.02))
HS.start((100*hs)/(hs+0.02))
vs=0.0015
VS=GPIO.PWM('vänsterservo-pin',1/(vs+0.02))
VS.start((100*vs)/(vs+0.02))
emdirec=open('shared_emotion.pk1','rb')
rundirec=open('shared_runstatus.pk1','rb')
imdirec=open('shared_impact.pk1','rb')
RunStatus=True
while RunStatus==True:
    emotion=pickle.load(emdirec)
    speed=speedcal(emotion)      # Speed multiplier from 0 to 1 according the current emotion.
    
    if GPIO.input('högersensor-pin')==1:
        pickle.dump([1,1,0],imdirec)
        Turn=True
        while Turn==True:
            # Function for turning
            if GPIO.input('vänstersensor-pin')==1:
                pickle.dump([1,1,1],imdirec)
                Turn=False
                Reverse=True
                while Reverse==True:
                    # Function for reversing
                    if GPIO.input('backsensor-pin')==1:
                        # Function for getting out
                    if GPIO.input('vänstersensor-pin')==0:
                        Reverse=False
            if GPIO.input('högersensor-pin')==0:
                Turn=False
        pickle.dump([0,0,0],imdirec)
    
    if GPIO.input('vänstersensor-pin')==1:
        # Almoast same as for h
    
    RunStatus=pickle.load(rundirec)     # Last
# Turn off the program