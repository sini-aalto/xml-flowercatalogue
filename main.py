import xml.etree.ElementTree as ET
filepath = "plant_catalog.xml"


with open(filepath, "r") as file:
    tree = ET.parse(file)
all_plants = tree.findall("PLANT")

all_tags = list(set([elem.tag.lower() for elem in tree.findall("PLANT/*")]))

def search_items():
    interest = input("What do you want to know about the available plants?")
    if interest.upper() == "COMMON":
        return [plant.find("COMMON").text for plant in all_plants]
    else:
        return [(plant.find("COMMON").text, plant.find(interest.upper()).text) for plant in all_plants]



# if __name__ == "__main__":
#     query = search_items()
#     print(f"Available plants in catalogue:")
#     if len(query) == 0:
#         print("Nothing found!")
#     else:
#         for q in query:
#             if type(q) is tuple:
#                 print(f"{q[0]}: {q[1]}", sep="/n")
#             else:
#                 print(q, sep="/n")