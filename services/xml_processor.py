import lxml.etree as ET
from fuzzyset import FuzzySet

class XMLProcessor:
    def __init__(self, xml_file) -> None:
        self.tree = ET.parse(xml_file)

    def query_xml(self,query):
        results = []
        for event, element in ET.iterwalk(self.tree.getroot()):
            if element.text is None:
                  continue
            corpus = [line.lstrip() for line in element.text.split("\n")]
            fs = FuzzySet(corpus)
            found = fs.get(query)
            if found is not None and found[0][0] > 0.8:
                results.append(element)
            if query in element.text:
                results.append(element)
        return self.structured_results(results)
    
    def structured_results(self, results):
        structured_results = []
        for result in results:
            local_name = ET.QName(result).localname if ET.QName(result).localname else ''
            text = result.text
            attributes = result.items()
            ancestors = ' > '.join([ET.QName(e).localname for e in result.xpath("ancestor::*")]) + ' > ' + local_name
            structured_results.append({'local_name': local_name, 'text': text, 'attributes': attributes, 'ancestors':ancestors})
        return structured_results
    
    def get_results_by_tag_filters(self, filters):
        results = []
        for event, element in ET.iterwalk(self.tree.getroot()):
            if element.text is None:
                  continue
            if XMLProcessor.check_hierarchical_order(filters, element):
                results.append(element)
        return self.structured_results(results)
    
    
    def check_hierarchical_order(filters, tree):
        filter_index = 0  
        
        for element in tree:
            if filter_index < len(filters) and element == filters[filter_index]:
                filter_index += 1  
            
            if filter_index == len(filters):
                return True
        
        return False  