# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:14:28 2016

@author: Samuel Sellberg
"""
from scipy import *
from pylab import *
from JASIClass import *
import pickle
import time
# import RPi.GPIO as GPIO
# (import all functions)

while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup('knapp-pin',GPIO.IN)
    # GPIO.setup(All GPIOs)
    if GPIO.input('knapp-pin')==GPIO.HIGH:
        time.sleep(2)                                      # Delay and start indication
        GPIO.output(('r-pin','g-pin','b-pin'),GPIO.HIGH)   # ---
        time.sleep(1)                                      # ---
        GPIO.output(('r-pin','g-pin','b-pin'),GPIO.LOW)    # ---
        time.sleep(1)                                      # ---
        GPIO.output(('r-pin','g-pin','b-pin'),GPIO.HIGH)   # ---
        time.sleep(1)                                      # ---
        GPIO.output(('r-pin','g-pin','b-pin'),GPIO.LOW)    # ---
        time.sleep(2)                                      # ---
        emdirec=open('shared_emotion.pk1','wb')       # Creating and pickling of shared values
        rundirec=open('shared_runstatus.pk1','wb')    # ---
        imdirec=open('shared_impact.pk1','wb')        # ---
        emotion=JASI(0.25,0.25,0.25,0.25,part=1000)   # ---
        pickle.dump([emotion],emdirec)                # ---
        RunStatus=True                                # ---
        pickle.dump(RunStatus,rundirec)               # ---
        impact=[0,0,0]                                  # ---
        pickle.dump(impact,imdirec)                   # ---
        # Start JASI_drive.py
        red=GPIO.PWM('r-pin','frequency')          # Initial starting values for LEDs
        red.start(25)                              # ---
        green=GPIO.PWM('g-pin','frequency')        # ---
        green.start(25)                            # ---
        blue=GPIO.PWM('b-pin','frequency')         # ---
        blue.start(25)                             # ---
        if GPIO.input('lowlight-pin')==1:                    # Determination of brightness at start
            if GPIO.input('midlight-pin')==1:                # ---
                if GPIO.input('highlight-pin')==1:           # ---
                    oldlightlevel=4                          # ---
                else:                                        # ---
                    oldlightlevel=3                          # ---
            else:                                            # ---
                oldlightlevel=2                              # ---
        else:                                                # ---
            oldlightlevel=1                                  # ---
        while RunStatus==True:
            
            red.ChangeDutyCycle((emotion.A*100))      # Changing LED values according to JASI
            green.ChangeDutyCycle((emotion.J*100))    # ---
            blue.ChangeDutyCycle((emotion.S*100))     # ---
            
            if GPIO.input('lowlight-pin')==1:                    # Determination of brightness
                if GPIO.input('midlight-pin')==1:                # ---
                    if GPIO.input('highlight-pin')==1:           # ---
                        lightlevel=4                             # ---
                    else:                                        # ---
                        lightlevel=3                             # ---
                else:                                            # ---
                    lightlevel=2                                 # ---
            else:                                                # ---
                lightlevel=1                                     # ---
            if oldlightlevel>lightlevel:                         # ---
                emotion.addS('balance')                          # ---
            if oldlightlevel<lightlevel:                         # ---
                emotion.addJ('balance')                          # ---
            oldlightlevel=lightlevel                             # ---
            pickle.dump([emotion],emdirec)                       # ---
            
            impact=pickle.load(imdirec)              # Checks for impact and adjusts JASI-value
            if impact[0]==0:                         # ---
                if GPIO.input('accel-x-pin')==1:     # ---
                    emotion.addA('balance-less')     # ---
            if impact[1]==0:                         # ---
                if GPIO.input('accel-y-pin')==1:     # ---
                    emotion.addA('balance-more')     # ---
            if GPIO.input('accel-z-pin')==1:         # ---
                emotion.addJ('balance')              # ---
            pickle.dump([emotion],emdirec)           # ---
            
            impact=pickle.load(imdirec)                 # Checks back sensor and adjusts JASI-value
            if impact[2]==0:                            # ---
                if GPIO.input('backsensor-pin')==1:     # ---
                    emotion.subJ('balance')             # ---
            pickle.dump([emotion],emdirec)              # ---
            
            emotion.addI('balance-very-small')   # Changes JASI-value due to end of cycle
            pickle.dump([emotion],emdirec)       # ---
            
            if GPIO.input('knapp-pin')==1        : # Last  # Turns off the while loop
                RunStatus=False                            # ---
                pickle.dump(RunStatus,rundirec)            # ---
                time.sleep(5)
                GPIO.cleanup()                             # ---