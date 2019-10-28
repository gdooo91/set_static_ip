## GUI the makes changing the static IP address in windows easy and quick.

import tkinter as tk                    ## to make the GUI
from tkinter import ttk                 ## << !
import os                               ## to excue command line funtions
from netsh_set import getInterfaceNames, sendCMD, makeBackup

class selectedInterface:
    def __init__(self, Name= None, ID = None, IP = None, gateWay = '255.255.255.0'):
        self.Name = Name
        self.ID = ID
        self.IP = IP
        self.gateWay = gateWay
    
    def setName(self,newName): # ToDo: safe to remove ?
        self.Name = newName
        print(self.Name)

    def setIpAddress(self, newIP):
        ipList = newIP.split('.')
        if len(ipList) < 4:
            return False
        else :
            for i in range (len(ipList)):
                if int(ipList[i])>255:
                    return False
        self.IP = newIP
        return(True)

    def setID(self, newID): # ToDo: safe to remove ?
        self.ID = newID
    def setInterface(self, newName, newIP, newGW):
        self.Name = newName
        self.IP = newIP
        self.gateWay
    
        Error = False
        if newName == None or newName == '':
            Error = True
        if newIP == None or newIP == '':
            Error = True
        if newGW == None or newGW == '':
            newGW = "255.255.255.0"
        #print("seleected interface :", newName)
        if (not(Error)):
            if (self.setIpAddress(newIP)== True):
                setCMD = "netsh interface ipv4 set address name= " + self.Name + " static " +self.IP+ " " + newGW + " "
                #
                # setCMD = "echo: HAHA this works!"
                if(sendCMD(setCMD) == True):
                    print("SET!")
                else :
                    print("sendCMD Error!")
            else:
                print("Error!")

        else:
            print("error!\n")

        


interface = selectedInterface()
intefaceList = getInterfaceNames()


makeBackup() # makes a backup at start of the program

## 
## command that will chagne the ip address
# netsh interface ipv4 set address name="YOUR INTERFACE NAME" static IP_ADDRESS SUBNET_MASK GATEWAY

## Start the GUI

root = tk.Tk()
root.title("Static IP Setup")
root.geometry('370x350')        # Window Size
root.resizable(False, False)    # Force the window to a fixed size
fontStyle = ("Courier", 11)
xPad = 20
yPad = 10

RAWnum = 0 

# print(root.winfo_width())
lb_interface = tk.Listbox(root,exportselection = False)
lb_interface.configure(width = 50)
lb_interface.grid(columnspan = 5,pady = yPad, padx = xPad,sticky = (tk.E,tk.S))
numbUsableInterface = 0 
for i in range(len(intefaceList)):
    if "Loopback" in intefaceList[i]:
        print("NO!")
    else :
        numbUsableInterface+=1
        lb_interface.insert(numbUsableInterface,intefaceList[i])
lb_interface.grid(column = 0)
for i in range(0,numbUsableInterface,2):
    lb_interface.itemconfigure(i, background='#f0f0ff')
if numbUsableInterface > 1:
    lb_interface.select_set(0)   # select first item
RAWnum+=1
lbl_IP = tk.Label(root, text ="New IP address", font = fontStyle)
lbl_IP.grid(row = RAWnum, column = 0, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
var_IP = tk.StringVar()
entry_IP = tk.Entry(root, textvariable =var_IP, width = 15 , font = fontStyle)
entry_IP.grid(row = RAWnum, column = 2, pady=yPad, padx = xPad, sticky=tk.W)

RAWnum+=1
lbl_GW = tk.Label(root, text ="New gateway", font = fontStyle)
lbl_GW.grid(row = RAWnum, column = 0, pady=yPad, padx = xPad, sticky=tk.W)
var_GW = tk.StringVar()
entry_GW = tk.Entry(root, textvariable =var_GW, width = 15 , font = fontStyle)
entry_GW.grid(row = RAWnum, column = 2, pady=yPad, padx = xPad, sticky=tk.E+tk.W)

RAWnum+=1
btn_SetIP = tk.Button(root, text = 'Select interface' , 
    #command = lambda:interface.setInterface(lb_interface.selection_get(),var_IP.get(),var_GW.get()))#,font = fontStyle)
    command = lambda:interface.setInterface(lb_interface.get('sel.first','sel.last'),var_IP.get(),var_GW.get()))
btn_SetIP.grid(row = RAWnum , column = 2, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
btn_SetIP.config( height = 1, width = 15 )


btn_backUp = tk.Button(root, text = 'Backup network settings' ,  command = lambda:makeBackup())
btn_backUp.grid(row = RAWnum , column = 0, pady=yPad, padx = xPad, sticky=tk.E+tk.W)
btn_backUp.config( height = 1, width = 15 )
root.mainloop( )