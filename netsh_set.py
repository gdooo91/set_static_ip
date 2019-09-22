### list of function used to change the static IP.

import subprocess   #
import re           # to clean strings

def getInterfaceNames():
    CmdLineOutput = subprocess.check_output("netsh interface ipv4 show interfaces", shell=True)

    ##  Decode CmdLineOutput
    CmdLineOutDecoded = CmdLineOutput.decode('utf-8')
    ##  Split the CmdLineOutDecoded by the new line "\n"
    lineByLineOut = CmdLineOutDecoded.split("\n")

    ##  Check where the usable data starts, by first lune starts after the line with '---'
    cleanLineByLineOut = []
    startData = 0
    for i in range(len(lineByLineOut)):
        if(lineByLineOut[i][:3] == '---'):
            print(i)
            startData = i
            break

    ##  Remove empty lines, count how many lines left
    for i in range(startData+1, len(lineByLineOut)):
        if(lineByLineOut[i] != "" and lineByLineOut[i] != "\r"):
            cleanLineByLineOut.append(lineByLineOut[i])


    ##  Split each line in cleanLineByLineOut by the 'connected'/ 'disconnected' and use the data after that .... 
    ##  ... and make a list of the Interfaces
    interfaceList = []
    for i in range (len(cleanLineByLineOut)):
        temp = cleanLineByLineOut[i].split("connected")
        if(len(temp) > 1):  # to make sure that there is "connected"
            interfaceName = re.sub(' +', ' ',temp[1])
            interfaceName = interfaceName.lstrip()
            interfaceName = interfaceName.strip('\r')
            interfaceList.append(interfaceName)
    return(interfaceList)