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
            structured_results.append({'local_name': local_name, 'text': text, 'attributes': attributes})
        return structured_results