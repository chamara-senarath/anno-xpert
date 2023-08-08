from lxml import etree
import bigtree as bt

class SchemaProcessor:

    def __init__(self,schema_file):
        xsd_tree = etree.parse(schema_file)
        target_nodes = self.find_target_nodes(xsd_tree)
        target_nodes_with_attributes =self.get_nodes_with_attributes(xsd_tree, target_nodes)
        self.root = bt.dict_to_tree(target_nodes_with_attributes)


    def find_target_nodes(self,xsd_tree):
        target_nodes = []
        for elem in xsd_tree.findall(".//xs:element[@name]", namespaces={"xs": "http://www.w3.org/2001/XMLSchema"}):
            target_name = elem.get("name")
            parent_path = self.get_parent_path(elem.getparent(),[])
            x = f"{parent_path}{target_name}" if parent_path == "None/" else f"{parent_path}/{target_name}"
            target_nodes.append(x)
        return target_nodes

    def get_parent_path(self, element, path=[]):
        if element is None:
            return "None/"+"/".join(reversed(path))
        if element.tag.endswith('element') and 'name' in element.attrib:
            path.append(element.get("name"))
        return self.get_parent_path(element.getparent(), path)

    def get_node_enumerations(self, xsd_tree):
        attributes = {}
        for elem in xsd_tree.findall(".//xs:enumeration[@value]", namespaces={"xs": "http://www.w3.org/2001/XMLSchema"}):
            parent_path = self.get_parent_path(elem,[])
            if parent_path not in attributes:
                attributes[parent_path] = {'enumerations': [elem.get("value")]}
            else:
                attributes[parent_path]['enumerations'].append(elem.get("value"))
        return attributes

    def get_nodes_with_attributes(self,xsd_tree, target_nodes):
        path_dict = {}
        for node in target_nodes:
            path_dict[node] = {}
        attributes = self.get_node_enumerations(xsd_tree)    
        return path_dict | attributes

    def get_tree_dot_object(self):
        graph = bt.tree_to_dot(self.root)
        return graph.to_string()

# root.show(max_depth=5,attr_list=["enumerations"])

# x = bt.findall(root, lambda node: node.depth == 2)
# for i in x:
#     print(i.name, i.get_attr("enumerations"))
