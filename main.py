
import sys
import time

import northlib.ntrp as radioManager
from northlib.ncmd.northcom import NorthCOM

uri = "radio:/0/76/2/E7E7E7E301"

"""
class NTX main

"""

if __name__ == '__main__':

    radioManager.radioSearch(baud=2000000) #Arduino DUE (USB Connection) has no Baudrate
    if not len(radioManager.availableRadios) > 0: sys.exit()
    
    time.sleep(1)
    
    uavcom = NorthCOM(uri=uri)
    uavcom.connect()
    uavcom.synchronize()
    
    timer = 0.0
    
    time.sleep(1)
    nx = uavcom.paramtable.getByName("calib.test2")
    print("Found : " + str(nx.name) + " : " + "index: " + str(nx.index))
    
    while uavcom.radio.isRadioAlive():
        uavcom.txGET(nx.index) #Want it From COM 
        print(nx.value)
        #timer+=1
        time.sleep(0.01)
        pass

    print("app exit")
    radioManager.closeAvailableRadios()
    sys.exit()
