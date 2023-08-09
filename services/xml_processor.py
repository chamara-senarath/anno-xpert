import lxml.etree as ET

class XMLProcessor:
    def __init__(self, xml_file) -> None:
        self.tree = ET.parse(xml_file)

    def capture_paragraph(self,path):
        paragraphs = self.tree.xpath(path)
        paragraph_text = ""
        for paragraph in paragraphs:
            paragraph_text += "".join(paragraph.itertext())
        print(paragraph_text)
        return paragraph_text