from lxml import etree
from bigtree import list_to_tree

# # Function to find target nodes (elements with "<xs:element name="">" structure) in the XSD
def find_target_nodes(xsd_tree):
    target_nodes = []
    for elem in xsd_tree.findall(".//xs:element[@name]", namespaces={"xs": "http://www.w3.org/2001/XMLSchema"}):
        target_name = elem.get("name")
        parent_path = get_parent_path(elem.getparent())
        x = f"{parent_path}{target_name}" if parent_path == "None/" else f"{parent_path}/{target_name}"
        target_nodes.append(x)
    return target_nodes

def get_parent_path(element, path=[]):
    if element is None:
        return "None/"+"/".join(reversed(path))
    if element.tag.endswith('element') and 'name' in element.attrib:
        path.append(element.get("name"))
    return get_parent_path(element.getparent(), path)

def get_nodes_with_attributes():
    pass


xsd_tree = etree.parse('../data/schema.xsd')
target_nodes = find_target_nodes(xsd_tree)

root = list_to_tree(target_nodes)
root.show(max_depth=5)