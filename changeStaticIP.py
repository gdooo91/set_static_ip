## GUI the makes changing the static IP address in windows easy and quick.

import tkinter as tk # to make the GUI
from tkinter import ttk
import os # to excue command line funtions
from netsh_set import getInterfaceNames


class selectedInterface:
    def __init__(self, Name= None, ID = None, IP = None):
        self.Name = Name
        self.ID = ID
        self.IP = IP

    def setName(self,newName): # ToDo: safe to remove ?
        self.Name = newName
        print(self.Name)

    def setID(self, newID): # ToDo: safe to remove ?
        self.ID = newID
    def setIP(self, newName, newIP):
        self.Name = newName
        self.IP = newIP
        defaultSubnetMaskStr = "255.255.255.0"

        setCMD = "netsh interface ipv4 set address name= " + self.Name + " static " +self.IP+ " " + defaultSubnetMaskStr + " "
        print(setCMD)

        


interface = selectedInterface()

intefaceList = getInterfaceNames()
for i in range(len(intefaceList)):
    print (i,": ", intefaceList[i])



## 
## command that will chagne the ip address
# netsh interface ipv4 set address name="YOUR INTERFACE NAME" static IP_ADDRESS SUBNET_MASK GATEWAY

# interfaceNumb = input("Select interface number: ")
# try: 
#     print("you selected: ",intefaceList[int(interfaceNumb)])
# except:
#     print(interfaceNumb,"Error!!\n")
# newIpAddress = [0,0,0,0]
# newSubnetMask = [0,0,0,0]

# newIpAddressStr = input ("Enter new Static IP 'saprate by .': ")
# newSubnetMaskStr = input ("Enter new Subnet Mask 'saprate by .': ")
# newIpAddress = newIpAddressStr.split('.')
# newSubnetMask= newSubnetMaskStr.split('.')
# print(newIpAddress," ", newSubnetMask)
# setCMD = "netsh interface ipv4 set address name= " + intefaceList[int(interfaceNumb)] + " static " + newIpAddressStr + " " + newSubnetMaskStr + " "
# print("\n",setCMD)
#"YOUR INTERFACE NAME" static IP_ADDRESS SUBNET_MASK GATEWAY
print("")
## Start the GUI

root = tk.Tk()
root.title("Static IP Setup")
root.geometry('470x370')        # Window Size
root.resizable(False, False)    # Force the window to a fixed size
fontStyle = ("Courier", 11)
xPad = 10
yPad = 10

RAWnum = 0 

print(root.winfo_width())
lb_interface = tk.Listbox()
lb_interface.configure(width = 50)
lb_interface.grid(columnspan = 5,pady = yPad, padx = xPad,sticky = (tk.E,tk.S))
for i in range(len(intefaceList)):
    lb_interface.insert(i,intefaceList[i])

lb_interface.grid(column = 0)
for i in range(0,len(intefaceList),2):
     lb_interface.itemconfigure(i, background='#f0f0ff')

RAWnum+=1
btn_SetIP = tk.Button(root, text = 'Select interface' , command = lambda:interface.setIP(lb_interface.selection_get(),var_IP.get()))#,font = fontStyle)
btn_SetIP.grid(row = RAWnum , column = 2, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
btn_SetIP.config( height = 1, width = 15 )

RAWnum+=1
lbl_IP = tk.Label(root, text ="New IP address", font = fontStyle)
lbl_IP.grid(row = RAWnum, column = 0, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
var_IP = tk.StringVar()
entry_IP = tk.Entry(root, textvariable =var_IP, width = 15 , font = fontStyle)
entry_IP.grid(row = RAWnum, column = 2, pady=yPad, padx = xPad, sticky=tk.E+tk.W)

RAWnum+=1
lbl_GW = tk.Label(root, text ="New gateway", font = fontStyle)
lbl_GW.grid(row = RAWnum, column = 0, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
var_GW = tk.StringVar()
entry_GW = tk.Entry(root, textvariable =var_GW, width = 15 , font = fontStyle)
entry_GW.grid(row = RAWnum, column = 2, pady=yPad, padx = xPad, sticky=tk.E+tk.W)

root.mainloop( )