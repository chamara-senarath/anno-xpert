import xml.etree.ElementTree as ET
import xml
import pandas as pd

def transform_xml(xml_doc):
    attr = xml_doc.attrib
    for xml in xml_doc.iter():
        # if not xml.get('name') == None:
        dict = attr.copy()
        dict.update(xml.attrib)
        
        yield dict

tree = ET.parse('../data/schema.xsd')

root = tree.getroot()

trans = transform_xml(root)

df = pd.DataFrame(trans)

# print(list(trans))
print(df)
