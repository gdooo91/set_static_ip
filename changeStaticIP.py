## GUI the makes changing the static IP address in windows easy and quick.

import tkinter as tk # to make the GUI
import os # to excue command line funtions
from netsh_set import getInterfaceNames


intefaceList = getInterfaceNames()
for i in range(len(intefaceList)):
    print (i,": ", intefaceList[i])



## 
## command that will chagne the ip address
# netsh interface ipv4 set address name="YOUR INTERFACE NAME" static IP_ADDRESS SUBNET_MASK GATEWAY

interfaceNumb = input()
try: 
    print("you selected: ",intefaceList[int(interfaceNumb)])
except:
    print(interfaceNumb,"Error!!\n")
newIpAddress = [0,0,0,0]
newSubnetMask = [0,0,0,0]

newIpAddressStr = input ("Enter new Static IP 'saprate by .': ")
newSubnetMaskStr = input ("Enter new Subnet Mask 'saprate by .': ")
newIpAddress = newIpAddressStr.split('.')
newSubnetMask= newSubnetMaskStr.split('.')
print(newIpAddress," ", newSubnetMask)
setCMD = "netsh interface ipv4 set address name= " + intefaceList[int(interfaceNumb)] + " static " + newIpAddressStr + " " + newSubnetMaskStr + " "
print("\n",setCMD)
#"YOUR INTERFACE NAME" static IP_ADDRESS SUBNET_MASK GATEWAY
print("")