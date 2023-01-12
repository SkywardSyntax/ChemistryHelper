class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESETALL = '\033[0m'
def findListIndex(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    exit("Error: Element not found.")
def clearConsole(number):
    print("\n"*number)
def repeatProgram(total,attempt):
    z = 0
    if attempt == (1):
        usrInput1 = input("Enter the element you want to find the molar mass of: ")
        calculation = MolarMass[findListIndex(TableOfElements, usrInput1)]
        usrInput2 = input("Enter the number of moles of " + usrInput1 + " you have: ")
        final = (int(usrInput2) * float(calculation))
        total +=final
        print("The molar mass of "+ str(usrInput2)+(" ")+ str(usrInput1) + " is " +bcolors.OKCYAN+str(final) +bcolors.RESETALL+ " g/mol")
        x = 0
        repeatProgram(total,2)
    else:
        usrInput = input("Are there more elements you wish to add to the calculation? (y/n): ")
        if usrInput == "y":
            while(z<1):
                usrInput1 = input("Enter the element you want to find the molar mass of: ")
                calculation = MolarMass[findListIndex(TableOfElements, usrInput1)]
                usrInput2 = input("Enter the number of moles of " + usrInput1 + " you have: ")
                final = (int(usrInput2)*float(calculation))
                total += final
                print("The molar mass of " +str(usrInput)+" "+usrInput1 + " is " + bcolors.OKCYAN+str(final) + bcolors.RESETALL+" g/mol")
                repeatProgram(total,2)
        else:
            clearConsole(15)
            print("The total molar mass of the elements you entered is " + bcolors.OKCYAN+ str(total) +bcolors.RESETALL+ " g/mol")
            exit()
total = 0
TableOfElements = ["Hydrogen", "Helium","Beryllium","Lithium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium","Magnesium","Aluminium","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine","Xenon","Caesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium","Roentgenium","Copernicium","Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Oganesson"]
TableOFElementsLocation = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118"]
MolarMass = ["1.01", "4", "6.94","9.01","10.81","12.01","14.01","16.00","19.00","20.18","22.99","24.31","26.98","28.09","30.97","32.07","35.45","39.95","39.10","40.08","44.96","47.87","50.94","51.99","54.94","55.85","58.93","58.69","63.55","65.39","69.72","72.61","74.92","78.96","79.90","83.80","85.47","87.62","88.91","91.22","92.91","95.94","98","101.07","102.91","106.42","107.87","112.41","114.82","118.71","121.76","127.60","126.90","131.29","132.91","137.33","138.91","140.12","140.91","144.24","145","150.36","151.96","157.25","158.93","162.50","164.93","167.26","168.93","173.05","174.97","178.49","180.95","183.84","186.21","190.23","192.22","195.08","196.97","200.59","204.38","207.2","208.98","209","210","222","223","226","227","232.04","231.04","238.03","237","244","243","247","247","251","252","257","258","259","262","261","262","266","264","277","268","271","272","270","286","281","280","285","284","289","288","293","294","294"]
repeatProgram(total,1)