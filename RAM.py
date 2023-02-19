import math
import time
import wmi

def RAM():   
    comp = wmi.WMI()

    data1 = 0
    for i in comp.Win32_OperatingSystem():
        data1 = math.floor(int(i.FreePhysicalMemory) / 100)
    time.sleep(1)
    data2 = 0
    for i in comp.Win32_OperatingSystem():
        data2 = math.floor(int(i.FreePhysicalMemory) / 100)


    if data1 == data2:
        return True
    return False

RAM()