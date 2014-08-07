#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 7/08/2014

import sys
import unittest
import math
import cmath

########################################################################
class AVR(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        self.tap_step=1.25
        self.present_tap=4
        self.nominal_tap=4
        self.accumulated_tap_change={}
        self.nominal_percent=10.0
        self.nominal_HV=33.0
        self.nominal_LV=11.0
        self.MVA=20.0
        self.XovrR=20
        self.tap_max=15
        self.tap_min=-5
        self.setpoint=1.0
        self.current=0+0j
        self.percentdeadband=2
        
    def nominal_impedance(self):
        zbase=math.pow((self.nominal_LV*1000),2)/(self.MVA*1000000)
        angle=math.atan(self.XovrR)
        nominal_impedance=cmath.rect((zbase*self.nominal_percent),angle)
        return nominal_impedance
        
    def get_impedance(self):
        buckboost=(100-(self.present_tap-self.nominal_tap)*self.tap_step)/100.0
        
                    
        self.impedance=self.nominal_impedance()*math.pow(buckboost,2)
        
        return self.impedance
    
    def set_current(self,current):
        self.current=current
    
    
    def get_seconds_to_tap_up(self,busvoltage,voltage):
        
        '''See comment below, do we need an accumulator'''
        '''Some controllers have a next tap delay, that is after the first tap change is made, if the '''
        
        if voltage > busvoltage-(self.percentdeadband/100*self.nominal_LV):
            time_to_tap_up=120
        else:
            time_to_tap_up=1000000
            
        '''Perhaps we run the power flow again and find if the bus voltage is still out'''
            
        return time_to_tap_up
    
    def get_seconds_to_tap_down(self,busvoltage,voltage):
        
        '''Do we need to include an accumulator here
        we need some understanding of if a tap changer still wants to make another tap change after already making a tap change'''
        
        if voltage < busvoltage+(self.percentdeadband/100*self.nominal_LV):
            time_to_tap_down=120
        else:
            time_to_tap_down=1000000
            
            

        return time_to_tap_down
    
    
    
    def __cmp__():
        pass
    
    def tap_up(self):
        self.accumulated_tap_change[self.tap,self.current]
        return False
    
    def tap_down():
        return False
    
########################################################################
class PowerFlow(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, tx1, tx2):
        """Constructor"""
        
        self.total_impedance(tx1, tx2)
        
    def total_impedance(tx1,tx2):
        pass
        

def main():
    tx1=AVR()
    tx2=AVR()
    
    powerflow=(tx1,tx2)
    
    powerflow.total
    
    print('here we go')


if __name__=='__main__':
    main()