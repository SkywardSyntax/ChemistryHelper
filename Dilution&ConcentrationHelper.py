import time
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    RED = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESETALL = '\033[0m'

def dilute(OriginMolarityValue, OriginVolumeValue, FinalMolarityValue, SolventName):

    ConversionFactor = (OriginMolarityValue/FinalMolarityValue)
    FinalVolume = (OriginVolumeValue * ConversionFactor)*1000
    print("The amount of "+SolventName+" you need to "+bcolors.UNDERLINE+bcolors.BOLD+bcolors.OKGREEN+" add"+bcolors.RESETALL+" is "+ bcolors.OKGREEN+str((FinalVolume-(OriginVolume*1000)))+bcolors.RESETALL+ " mL")

def concentrate(OriginMolarityValue, OriginVolumeValue, FinalMolarityValue, SolventName):
    ConversionFactor = (FinalMolarityValue / OriginMolarityValue)
    FinalVolume = (OriginVolumeValue / ConversionFactor)*1000
    print("The amount of "+SolventName+" you need to "+bcolors.UNDERLINE + bcolors.BOLD+bcolors.RED+"remove"+bcolors.RESETALL+" is "+ bcolors.RED+str(-(FinalVolume-(OriginVolume*1000)))+bcolors.RESETALL+ " mL")

def getFileContents(filename):
    with open(filename, 'r') as f:
        output = f.read()
    return output


OriginMolarity = float(input("What is the Molarity of the input solution? (M) \n"))
time.sleep(0.5)
OriginVolume = float(input("What is the Volume of the  input solution? (L) \n"))
time.sleep(0.5)
FinalMolarity = float(input("What Molarity would you like to go to?\n"))
time.sleep(0.5)

if os.path.getsize('Config Files/Solvent.txt') == 0:
    Solvent = input("What is the name of your solvent?\n")
    with open("Config Files/Solvent.txt", "w") as file:
        file.write(Solvent)
        file.close()
else:
    Solvent = getFileContents("Config Files/Solvent.txt")



if OriginMolarity > FinalMolarity:
    dilute(OriginMolarity, OriginVolume, FinalMolarity, Solvent)
elif OriginMolarity < FinalMolarity:
    concentrate(OriginMolarity, OriginVolume, FinalMolarity, Solvent)
else:
    print("The Molarity of the input solution is already the same as the desired Molarity")

