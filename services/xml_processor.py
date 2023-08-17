import lxml.etree as ET
from fuzzyset import FuzzySet

class XMLProcessor:
    def __init__(self, xml_file) -> None:
        self.tree = ET.parse(xml_file)

    def query_xml(self,query, filters, enums):
        filters = [item for item in filters if item != ""]
        enums = [item for item in enums if item['enum'] != ""]
        query_results = []
        dropdown_results=[]

        if filters:
            dropdown_results = self.get_results_by_tag_filters(filters, enums)
        if query:
            for _, element in ET.iterwalk(self.tree.getroot()):
                if element.text is None:
                    continue
                corpus = [line.lstrip() for line in element.text.split("\n")]
                fs = FuzzySet(corpus)
                found = fs.get(query)
                if found is not None and found[0][0] > 0.8:
                    query_results.append(element)
                if query in element.text:
                    query_results.append(element)
        
        if not query_results:
            return self.structured_results(dropdown_results)
        elif not dropdown_results:
            return self.structured_results(query_results)
        
        merged_results = list(set(query_results).intersection(set(dropdown_results)))
        return self.structured_results(merged_results) if filters else self.structured_results(query_results)
    
    def structured_results(self, results):
        structured_results = []
        for result in results:
            local_name = ET.QName(result).localname if ET.QName(result).localname else ''
            text = result.text
            attributes = result.items()
            ancestors = ' > '.join([ET.QName(e).localname for e in result.xpath("ancestor-or-self::*")])
            structured_results.append({'local_name': local_name, 'text': text, 'attributes': attributes, 'ancestors':ancestors})
        return [item for item in structured_results if item['text'].strip() != ""]
    
    def get_results_by_tag_filters(self, filters, enums):
        results = []
        for _, element in ET.iterwalk(self.tree.getroot()):
            if element.text is None:
                continue
            root = [ET.QName(e).localname for e in element.xpath("ancestor-or-self::*")]
            if XMLProcessor.check_hierarchical_order(filters, root):
                results.append(element)
        return self.filter_results_by_enumerations(results, enums)
    
    
    def check_hierarchical_order(filters, tree):
        filter_index = 0  
        
        for element in tree:
            if filter_index < len(filters) and element.lower() == filters[filter_index].lower():
                filter_index += 1  
            
            if filter_index == len(filters):
                return True
        
        return False 
    
    def filter_results_by_enumerations(self, results ,enums):
        if not enums:
            return results

        enum_lookup = {(enum['parent'].lower(), enum['enum'].lower()) for enum in enums}
        filtered_results = []

        for result in results:
            result_localname = ET.QName(result).localname.lower()
            result_type = result.attrib.get('type', '').lower()

            if (result_localname, result_type) in enum_lookup:
                filtered_results.append(result)

        return filtered_results