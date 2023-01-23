import time
import math 


def dilute(OriginMolarity, OriginVolume, FinalMolarity):

    ConversionFactor = (OriginMolarity/FinalMolarity)
    FinalVolume = (OriginVolume * ConversionFactor)*1000
    print("The amount of universal solvent you need to add is "+ str((FinalVolume-(OriginVolume*1000)))+ " mL")

def concentrate(OriginMolarity, OriginVolume):
    FinalMolarity = input("What Molarity would you like to concentrate to?\n")
    ConversionFactor = (FinalMolarity / OriginMolarity)
    FinalVolume = (OriginVolume * ConversionFactor)*1000
    print("The amount of universal solvent you need ot remove is", (FinalVolume-((OriginVolume)*1000), "mL"))


OriginMolarity = float(input("What is the Molarity of the input solution? (M) \n"))
time.sleep(0.5)
OriginVolume = float(input("What is the Volume of the  input solution? (L) \n"))
time.sleep(0.5)
FinalMolarity = float(input("What Molarity would you like to dilute to?\n"))
time.sleep(0.5)

if OriginMolarity > FinalMolarity:
    dilute(OriginMolarity, OriginVolume, FinalMolarity)
elif OriginMolarity < FinalMolarity:
    concentrate(OriginMolarity, OriginVolume)

