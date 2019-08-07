# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 02:07:20 2016

@author: Samuel Sellberg
"""

def drive(S,s):
    S.ChangeFrequency(1/(s+0.02))
    S.ChangeDutyCycle((100*s)/(s+0.02))

def speedcal(emotion):
    if not isinstance(emotion,JASI):
        raise TypeError("Input must be 'JASI'.")
    return (1+(emotion.J+emotion.A)-(emotion.S+emotion.I))/2

def hscal(speed):    # May be called vscal
    if not isinstance(speed,(int,float)):
        raise TypeError("Speed must be 'int' or 'float'.")
    if not 0<=speed<=1:
        raise ValueError("Speed must be in interval from 0 to 1.")
    return 0.0005+(speed*0.0020)    # Needs exact values

def vscal(speed):    # May be called hscal
    if not isinstance(speed,(int,float)):
        raise TypeError("Speed must be 'int' or 'float'.")
    if not 0<=speed<=1:
        raise ValueError("Speed must be in interval from 0 to 1.")
    return 0.0025-(speed*0.0020)    # Needs exact values

