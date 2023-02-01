class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ORANGE = '\033[33m'
    magenta = '\033[35m'
    UNDERLINE = '\033[4m'
    RESETALL = '\033[0m'
avogadro = ("Avogadro's number is the number of particles in one mole of a substance. It is 6.02214179 x 10^23 particles/mol.")
molar_mass = ("The molar mass of a substance is the mass of one mole of that substance. It is measured in grams per mole (g/mol).")
periodic_trends = ("The periodic trends are the trends that occur in the periodic table. They are the trends in atomic radius, ionization energy, electronegativity, and atomic mass.")
atomic_radius = ("Atomic radius is the distance from the center of an atom to the outermost electron. The trend is that the atomic radius decreases as you go down a group and increases as you go across a period.")
ionization_energy = ("Ionization energy is the energy required to remove an electron from an atom. The trend is that the ionization energy increases as you go down a group and decreases as you go across a period.")
electronegativity = ("Electronegativity is the ability of an atom to attract electrons. The trend is that the electronegativity increases as you go up a group and decreases as you go right along the periodic table.")
soluteVsSolvent = ("A solute is the substance that is dissolved in a solvent. A solvent is the substance that dissolves the solute.")
userQuestion = input("What would you like to know about chemistry?\n1.) Avogadro's number\n2.) Molar mass\n3.) Periodic trends\n4.) Atomic radius\n5.) Ionization energy\n6.) Electronegativity\nSolute vs. Solvent\n")
if userQuestion == "1":
    print(bcolors.OKGREEN + avogadro + bcolors.RESETALL)
elif userQuestion == "2":
    print(bcolors.OKBLUE + molar_mass + bcolors.RESETALL)
elif userQuestion == "3":
    print(bcolors.OKCYAN + periodic_trends + bcolors.RESETALL)
elif userQuestion == "4":
    print(bcolors.RED + atomic_radius + bcolors.RESETALL)
elif userQuestion == "5":
    print(bcolors.ORANGE + ionization_energy + bcolors.RESETALL)
elif userQuestion == "6":
    print(bcolors.magenta + electronegativity + bcolors.RESETALL)
else:
    print(bcolors.FAIL + "Invalid input." + bcolors.RESETALL)



