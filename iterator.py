# Iterating through the elements of the plant_catalog.xml with iterparse
from xml.etree.ElementTree import iterparse

xmlfile = "plant_catalog.xml"
actions = ("start", "end")

def find_chosen(filename):
    itertree = iterparse(filename, events=actions)
    for event, node in itertree:
        if "find_this" in node.attrib.keys():
            return node.find("COMMON").text
        else:
            node.clear()
            continue


if __name__ == "__main__":
    print(find_chosen(xmlfile))
