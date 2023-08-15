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
        return results