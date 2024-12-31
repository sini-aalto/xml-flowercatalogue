from lxml import etree

xmlfile = "plant_catalog.xml"
schemafile = "schema.xsd"

with open(schemafile, "r") as s:
    doc = etree.parse(s)
    schema = etree.XMLSchema(doc)

with open(xmlfile, "r") as file:
    tree = etree.parse(file)

print("Validating...")
result = schema.validate(tree)
if result:
    print("Validation successfull.")
else:
    print("XML document is not valid.")