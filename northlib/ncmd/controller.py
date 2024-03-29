#!/usr/bin/env pythonh
# -*- coding: utf-8 -*-
#  __  __ ____ _  __ ____ ___ __  __
#  \ \/ // __// |/ //  _// _ |\ \/ /
#   \  // _/ /    /_/ / / __ | \  / 
#   /_//___//_/|_//___//_/ |_| /_/  
# 
#   2024 Yeniay Uav Flight Control Systems
#   Research and Development Team

import threading
import pygame
import time

__author__ = 'Yeniay RD'
__all__ = ['Controller']

class Controller():
    """ 
    NTRP Joystick Controller 
    """
    
    def __init__(self):
        self.isAlive = False
        self.axis = [0,0,0,0]
        pygame.init()
        pygame.joystick.init()
        if not self.findController(): 
            print("NPX:/> Joystick Not Found.")
    
    def findController(self):
        if pygame.joystick.get_count() > 0:
                self.joystick = pygame.joystick.Joystick(0)  # First Founded JOYSTICK 
                self.joystick.init()
                self.ctrlThread = threading.Thread(target=self.ctrlProcess,daemon=False)
                self.ctrlThread.start()
                return True
        else:
            return False 
        
    def ctrlProcess(self):
        self.isAlive = True
        while self.isAlive:
            for event in pygame.event.get(pygame.JOYAXISMOTION):
                for i in range(4):
                    self.axis[i] = (int)(((self.joystick.get_axis(i)+1)*255)/2)
            
            #print(self.axis)
        print("NPX:/> CTRL Process end.")

    def getAxis(self):
        return bytearray(self.axis)

    def destroy(self):
        self.isAlive = False