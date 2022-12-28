def main():
    """Main function."""
    # Get input
    input_type = input("Enter 'e' for electron configuration or 'n' for element name: ")
    if input_type == "e":
        input_value = input("Enter the electron configuration: ")
    elif input_type == "n":
        input_value = input("Enter the element name: ")

    # Get the element name
    if input_type == "e":
        element_name = get_element_name(input_value)
        print(element_name)
    # Get the electron configuration
    elif input_type == "n":
        electron_configuration = get_electron_configuration(input_value)
        print(electron_configuration)
    # Invalid input
    else:
        print("Invalid input")
def get_element_name(electron_configuration):
    """Get the element name from the electron configuration."""
    # Get the element name
    element_name = ""
    for element in ELEMENTS:
        if ELEMENTS[element] == electron_configuration:
            element_name = element
    # Return the element name
    return element_name
def get_electron_configuration(element_name):
    """Get the electron configuration from the element name."""
    # Get the electron configuration
    electron_configuration = ELEMENTS[element_name]
    # Return the electron configuration
    return electron_configuration
# Dictionary of elements and their electron configurations
ELEMENTS = {
    "Hydrogen": "1s1",
    "Helium": "1s2",
    "Lithium": "1s2 2s1",
    "Beryllium": "1s2 2s2",
    "Boron": "1s2 2s2 2p1",
    "Carbon": "1s2 2s2 2p2",
    "Nitrogen": "1s2 2s2 2p3",
    "Oxygen": "1s2 2s2 2p4",
    "Fluorine": "1s2 2s2 2p5",
    "Neon": "1s2 2s2 2p6",
    "Sodium": "1s2 2s2 2p6 3s1",
    "Magnesium": "1s2 2s2 2p6 3s2",
    "Aluminum": "1s2 2s2 2p6 3s2 3p1",
    "Silicon": "1s2 2s2 2p6 3s2 3p2",
    "Phosphorus": "1s2 2s2 2p6 3s2 3p3",
    "Sulfur": "1s2 2s2 2p6 3s2 3p4",
    "Chlorine": "1s2 2s2 2p6 3s2 3p5",
    "Argon": "1s2 2s2 2p6 3s2 3p6",
    "Potassium": "1s2 2s2 2p6 3s2 3p6 4s1",
    "Calcium": "1s2 2s2 2p6 3s2 3p6 4s2",
    "Scandium": "1s2 2s2 2p6 3s2 3p6 4s2 3d1",
    "Titanium": "1s2 2s2 2p6 3s2 3p6 4s2 3d2",
    "Vanadium": "1s2 2s2 2p6 3s2 3p6 4s2 3d3",
    "Chromium": "1s2 2s2 2p6 3s2 3p6 4s2 3d4",
    "Manganese": "1s2 2s2 2p6 3s2 3p6 4s2 3d5",
    "Iron": "1s2 2s2 2p6 3s2 3p6 4s2 3d6",
    "Cobalt": "1s2 2s2 2p6 3s2 3p6 4s2 3d7",
    "Nickel": "1s2 2s2 2p6 3s2 3p6 4s2 3d8",
    "Copper": "1s2 2s2 2p6 3s2 3p6 4s1 3d9",
    "Zinc": "1s2 2s2 2p6 3s2 3p6 4s2 3d10",
    "Gallium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1",
    "Germanium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2",
    "Arsenic": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3",
    "Selenium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4",
    "Bromine": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5",
    "Krypton": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6",
    "Rubidium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1",
    "Strontium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2",
    "Yttrium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1",
    "Zirconium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2",
    "Niobium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3",
    "Molybdenum": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4",
    "Technetium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5",
    "Ruthenium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d6",
    "Rhodium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7",
    "Palladium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8",
    "Silver": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d9",
    "Cadmium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10",
    "Indium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1",
    "Tin": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2",
    "Antimony": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3",
    "Tellurium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4",
    "Iodine": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5",
    "Xenon": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6",
    "Cesium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1",
    "Barium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2",
    "Lanthanum": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1",
    "Cerium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1",
    "Praseodymium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3",
    "Neodymium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4",
    "Promethium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5",
    "Samarium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6",
    "Europium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7",
    "Gadolinium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1",
    "Terbium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9",
    "Dysprosium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10",
    "Holmium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11",
    "Erbium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12",
    "Thulium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13",
    "Ytterbium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14",
    "Lutetium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1",
    "Hafnium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2",
    "Tantalum": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3",
    "Tungsten": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4",
    "Rhenium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5",
    "Osmium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6",
    "Iridium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7",
    "Platinum": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10 5p6 6s2 4f14 5d9",
    "Gold": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10 5p6 6s1 4f14 5d10",
    "Mercury": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10 5p6 6s2 4f14 5d10",
    "Thallium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10 5p6 6s2 4f14 5d10 6p1",
    "Lead": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2",
    "Bismuth": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3",
    "Polonium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4",
    "Astatine": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5",
    "Radon": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6",
    "Francium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1",
    "Radium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2",
    "Actinium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1",
    "Thorium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2",
    "Protactinium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d3",
    "Uranium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d4",
    "Neptunium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1",
    "Plutonium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6",
    "Americium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7",
    "Curium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1",
    "Berkelium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f9",
    "Californium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f10",
    "Einsteinium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f11",
    "Fermium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f12",
    "Mendelevium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f13",
    "Nobelium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14",
    "Lawrencium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1",
    "Rutherfordium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d2",
    "Dubnium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d3",
    "Seaborgium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d4",
    "Bohrium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5",
    "Hassium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d6",
    "Meitnerium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d7",
    "Darmstadtium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d9",
    "Roentgenium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1 5f14 6d10",
    "Copernicium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10",
    "Nihonium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1",
    "Flerovium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p2",
    "Moscovium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p3",
    "Livermorium": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p4",
    "Tennessine": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p5",
    "Oganesson": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6",







}
main()
