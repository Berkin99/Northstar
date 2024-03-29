#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  __  __ ____ _  __ ____ ___ __  __
#  \ \/ // __// |/ //  _// _ |\ \/ /
#   \  // _/ /    /_/ / / __ | \  / 
#   /_//___//_/|_//___//_/ |_| /_/  
# 
#   2024 Yeniay Uav Flight Control Systems
#   Research and Development Team

from enum import Enum
import struct

import northlib.ncmd.nrx as nrx
from northlib.ntrp.northpipe import NorthNRF
from northlib.ntrp.ntrpbuffer import NTRPBuffer
import northlib.ntrp.ntrp as ntrp

__author__ = 'Yeniay RD'
__all__ = ['Nrx','NrxType_e','NrxType']

NRX_BYTES_MASK  = 0x03
NRX_1BYTE       = 0x00
NRX_2BYTES      = 0x01
NRX_4BYTES      = 0x02
NRX_8BYTES      = 0x03

NRX_TYPE_MASK   =  0x0F
NRX_TYPE_INT    = (0x00<<2)
NRX_TYPE_FLOAT  = (0x01<<2)

NRX_SIGNED 	    = (0x00<<3)
NRX_UNSIGNED 	= (0x01<<3)

NRX_CORE 	= (1<<5)
NRX_RONLY 	= (1<<6)

NRX_START = 1
NRX_STOP  = 0

NRX_VARIABLE= (0x00<<7)
NRX_GROUP   = (0x01<<7)

NRX_PERSISTENT =(1<<8)

class NrxType_e(Enum):
    UINT8      = 0
    INT8       = 1
    UINT16     = 2
    INT16      = 3
    UINT32     = 4
    INT32      = 5
    FLOAT      = 6
    GROUPSTART = 7
    GROUPSTOP  = 8

class NrxType():

    def __init__(self,rawtype):
        self.varType  = nrx.NrxTypeParse(rawtype)
        self.varBytes = 2**(rawtype&NRX_BYTES_MASK)
        self.readOnly = False
        self.group    = False
      
        if rawtype&NRX_RONLY: self.readOnly = True
        if rawtype&NRX_GROUP: self.group = True

class Nrx:
    #CMD,1,#index1,type1,name
    def __init__(self,index=0,rawtype=None,name=str):
        self.index = index
        self.type  = NrxType(rawtype)
        self.name  = name
        self.value = None
    
    def setValue(self,raw):
        if self.type.group: return
        self.value = nrx.NrxValueParse(raw,self.type.varType)

    def append(self,nrx):
        self.nrxList.append(nrx)

def NrxParse(rawarray = bytearray):
    nrxindex = rawarray[0]
    nrxtype = rawarray[1]
    nrxname = bytearray()
    for i in range(len(rawarray)-2):
        nrxname.append(rawarray[i+2])    
    nrxname = bytearray()
    return Nrx(nrxindex,nrxtype,nrxname.decode(errors='ignore'))

def NrxTypeParse (rawtype):
    if rawtype&NRX_GROUP:
        if rawtype&NRX_START: return NrxType_e.GROUPSTART
        return NrxType_e.GROUPSTOP

    if rawtype&NRX_TYPE_FLOAT: return NrxType_e.FLOAT

    bytesize = 2**(rawtype&NRX_BYTES_MASK)

    if rawtype&NRX_UNSIGNED:
        if   bytesize==1: return NrxType_e.UINT8
        elif bytesize==2: return NrxType_e.UINT16
        elif bytesize==4: return NrxType_e.UINT32
    else:
        if   bytesize==1: return NrxType_e.INT8
        elif bytesize==2: return NrxType_e.INT16
        elif bytesize==4: return NrxType_e.INT32    

def NrxValueParse (rawvalue,vartype):
        parser = {
            NrxType_e.UINT8: lambda arr:struct.unpack( 'B', arr[0:1])[0],
            NrxType_e.UINT16:lambda arr:struct.unpack('<H', arr[0:2])[0],
            NrxType_e.UINT32:lambda arr:struct.unpack('<I', arr[0:4])[0],
            NrxType_e.INT8:  lambda arr:struct.unpack( 'b', arr[0:1])[0],
            NrxType_e.INT16: lambda arr:struct.unpack('<h', arr[0:2])[0],
            NrxType_e.INT32: lambda arr:struct.unpack('<i', arr[0:4])[0],
            NrxType_e.FLOAT: lambda arr:struct.unpack('<f', arr[0:4])[0],
        }
        return parser.get(vartype)(rawvalue)


def NrxLog (nx=nrx.Nrx):
    print("[" + str(nx.index) + "] : " + nx.name + " : " + str(nx.value))

NRX_UINT8  = (NRX_1BYTE  | NRX_TYPE_INT | NRX_UNSIGNED)
NRX_INT8   = (NRX_1BYTE  | NRX_TYPE_INT | NRX_SIGNED)
NRX_UINT16 = (NRX_2BYTES | NRX_TYPE_INT | NRX_UNSIGNED)
NRX_INT16  = (NRX_2BYTES | NRX_TYPE_INT | NRX_SIGNED)
NRX_UINT32 = (NRX_4BYTES | NRX_TYPE_INT | NRX_UNSIGNED)
NRX_INT32  = (NRX_4BYTES | NRX_TYPE_INT | NRX_SIGNED)

NRX_FLOAT  = (NRX_4BYTES | NRX_TYPE_FLOAT | NRX_SIGNED)
