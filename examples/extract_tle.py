from lxml import etree

def display_top_level_elements(schema_file):
    # Load the XML schema file
    schema = etree.parse(schema_file)

    # Retrieve all top-level elements
    top_level_elements = schema.xpath('/xs:schema/xs:element', 
                                      namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'})

    # Display the top-level elements
    for element in top_level_elements:
        print(element.get('name'))

# Path to your XML schema file
schema_file_path = 'schema.xsd'

# Call the function to display top-level elements
display_top_level_elements(schema_file_path)
