XML (eXtensible Markup Language) managing is a project for learning basic XML handling including e.g. file navigation and validation.

While the main point of the project is to familiarize myself with XML as a format, it is also working as a 
chance for me to refresh some python basics of mine by writing a small program that retrieves data
from the XML file based on user input.

The following python libraries have been used:
- The built-in xml.etree.ElementTree for file parsing and navigation
- The lxml library for XML file validation with XSD (XML Schema Definition)

These libraries were chosen due to their availability and the fact that while the built-in xml library is generally a good choice for smaller
files, lxml is suggested to be used for larger file sizes and it contains an easy-to-use validation function for XML trees. 

Plans to extend the project in the near-future:
- Writing or modifying XML files in addition to reading from them
- Handling element attributes
- Validation for attribute values
