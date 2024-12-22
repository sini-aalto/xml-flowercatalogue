import xml.etree.ElementTree as ET
filepath = "plant_catalog.xml"


with open(filepath, "r") as file:
    tree = ET.parse(file)


