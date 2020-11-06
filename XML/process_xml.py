import xml.dom.minidom

f = open("XML/json_to_xml.xml", "r")
xmlstring = f.read()

dom = xml.dom.minidom.parseString(xmlstring)
xml = dom.toprettyxml()
print(xml)