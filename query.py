import xml.etree.ElementTree as ET

xmlfile = "plant_catalog.xml"

with open(xmlfile, "r") as file:
    tree = ET.parse(file)

all_plants = tree.findall("PLANT")
all_tags = list(set([elem.tag.lower() for elem in tree.findall("PLANT/*")]))


def search_items(interest):
    if interest.upper() == "COMMON":
        return sorted([plant.find("COMMON").text for plant in all_plants])
    else:
        return sorted([(plant.find("COMMON").text, plant.find(interest.upper()).text) for plant in all_plants])


if __name__ == "__main__":
    print("Welcome to plant catalogue!")
    interest = ""
    while interest.lower() != "exit":
        print(f"You can exit via typing 'exit', or search with the following keywords: {
              all_tags}")
        interest = input(
            "What do you want to know about the plants in catalogue? ")
        if interest.lower() == "exit":
            break
        result = search_items(interest)
        if len(result) == 0:
            print(f"Available plants in catalogue:")
            print("Nothing found!")
        else:
            print(f"Available plants in catalogue:")
            for q in result:
                if type(q) is tuple:
                    print(f"{q[0]}: {q[1]}", sep="/n")
                else:
                    print(q, sep="/n")
    print("Thanks for visiting!")
