#!/usr/bin/env pythonh
# -*- coding: utf-8 -*-
#  __  __ ____ _  __ ____ ___ __  __
#  \ \/ // __// |/ //  _// _ |\ \/ /
#   \  // _/ /    /_/ / / __ | \  / 
#   /_//___//_/|_//___//_/ |_| /_/  
# 
#   2024 Yeniay Uav Flight Control Systems
#   Research and Development Team

import time 

import northlib.ntrp.ntrp as ntrp
from northlib.ntrp.ntrpbuffer import NTRPBuffer
from northlib.ntrp.northradio import NorthRadio 
import northlib.ntrp as nt

__author__ = 'Yeniay RD'
__all__ = ['NorthPipe','NorthNRF']

class NorthPipe():

    """ 
    NorthPipe Class 
    
    >It communicates with target agent in the RF Network
    >Transmit commands
    >Receive Buffer & newdata callback

    SELF -> UART LORA MODULE 
    NRF CLASS -> NRF ROUTER
    """

    def __init__(self, pipe_id = 'X', radio = NorthRadio):
        self.id = pipe_id                    # Agent ID

        # The Pipe ID is should be same with target agent ID
        # Agent ID is represents the rf adress when use NTRP_Router Dongle
        # Agent ID identifies the target agent when use UART Lora Module
        self.radio = radio            
        self.radio.subPipe(pipe=self)

        self.rxbuffer = NTRPBuffer(10)
        self.txpck = ntrp.NTRPPacket()
        self.newPacketCallBack = None
        
    def append(self,msg):
        self.rxbuffer.append(msg)
        if self.newPacketCallBack != None:
            self.newPacketCallBack()

    def setCallBack(self, func):
        self.newPacketCallBack = func

    def waitConnection(self, timeout = 0.5):
        self.txMSG("ACK Request")
    
        timer = 0.0
        while(not self.rxbuffer.isAvailable() and timer<=timeout):
            time.sleep(0.001)
            timer +=   0.001
            
        if(self.rxbuffer.isAvailable() == False): return 0
        return timer

    def transmitPacket(self,txPacket = ntrp.NTRPPacket):
        self.radio.transmitNTRP(txPacket,self.id)     

    def txNAK(self):               
        self.txpck = ntrp.NTRPPacket('NAK')
        self.transmitPacket(self.txpck)     

    def txACK(self):
        self.txpck = ntrp.NTRPPacket('ACK')
        self.transmitPacket(self.txpck)     

    def txMSG(self,msg=str):        
        self.txpck = ntrp.NTRPPacket('MSG')
        self.txpck.data = msg.encode()
        self.txpck.dataID = len(self.txpck.data)        
        self.transmitPacket(self.txpck)     

    def txGET(self,dataid=int):
        self.txpck = ntrp.NTRPPacket('GET')
        self.txpck.dataID = dataid
        self.transmitPacket(self.txpck)

    def txSET(self,dataid=int,databytes=bytearray):
        self.txpck = ntrp.NTRPPacket('SET')
        self.txpck.dataID = dataid
        self.txpck.data = databytes   
        self.transmitPacket(self.txpck)
        
    def txCMD(self,channels=bytearray):
        self.txpck = ntrp.NTRPPacket('CMD')
        self.txpck.dataID = 0
        self.txpck.data = channels   
        self.transmitPacket(self.txpck)
        

class NorthNRF(NorthPipe):
        
    """
    NorthNRF Class

    NorthNRF represents RF module on external router. 
    No use case without router.
    """
    NRF_250KBPS  = 0
    NRF_1000KBPS = 1
    NRF_2000KBPS = 2

    def __init__(self, radioindex = 0, ch = 0, bandwidth = NRF_1000KBPS, address = "E7E7E7E304"):
        super().__init__(pipe_id='0', radio=nt.getRadio(radioindex))
    
        self.channel = ch                       #int
        self.bandwidth = bandwidth              #int[0,1,2]
        self.address = bytes.fromhex(address)   #bytearray[5]
        if(len(self.address) != 5): raise ValueError()
        
        self.isActive = True

        #If Use NRF Router module, Agents has nrf address instead of ID
        #ID needs to be defined to identify the pipe, so get new tag from radio
        self.id = self.radio.newPipeID() 
        self.txOPENPIPE()
    
    def setChannel(self,ch):
        self.channel = ch
        return True

    def setBandwidth(self,bw):
        self.bandwidth = bw
        return True
    
    def setAddress(self, address):
        self.address = bytes.fromhex(address)

    def txOPENPIPE(self):
        packet = ntrp.NTRPPacket()
        packet.header = ntrp.NTRPHeader_e.OPENPIPE
        packet.dataID = ord(self.id)
        packet.data   = self.getNrfData()
        self.radio.transmitNTRP(packet,ntrp.NTRP_ROUTER_ID)
    
    def txCLOSEPIPE(self):
        packet = ntrp.NTRPPacket()
        packet.header = ntrp.NTRPHeader_e.CLOSEPIPE
        packet.dataID = self.id
        self.radio.transmitNTRP(packet,ntrp.NTRP_ROUTER_ID)

    def getNrfData(self):
        arr = bytearray()
        arr.append(self.channel)
        arr.append(self.bandwidth)
        arr.extend(self.address)
        return arr
        
    def destroy(self):
        self.txCLOSEPIPE()
        self.radio.unsubPipe(self.id)
        self.isActive = False

