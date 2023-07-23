import rdflib
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

def convert_xml_to_rdf(xml_file, rdf_file):
    # Create an RDF graph
    graph = Graph()

    # Define custom namespaces for the XML elements and RDF properties
    custom_ns = Namespace("http://example.com/ontology#")
    rdf_ns = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

    # Read and parse the XML file
    graph.parse(xml_file)

    # Iterate through the XML elements and convert them to RDF triples
    for subject, predicate, obj in graph:
        # Use the custom namespace for the subject and predicate
        subject = custom_ns[subject]
        predicate = custom_ns[predicate]

        # Handle repeating elements
        if isinstance(obj, rdflib.term.BNode):
            for item in graph.objects(obj, None):
                # Convert XML elements to RDF resources or literals
                if isinstance(item, rdflib.term.URIRef):
                    item = custom_ns[item]
                elif isinstance(item, rdflib.term.Literal):
                    item = Literal(item)

                # Add the triple to the RDF graph
                graph.add((subject, predicate, item))
        else:
            # Convert XML elements to RDF resources or literals
            if isinstance(obj, rdflib.term.URIRef):
                obj = custom_ns[obj]
            elif isinstance(obj, rdflib.term.Literal):
                obj = Literal(obj)

            # Add the triple to the RDF graph
            graph.add((subject, predicate, obj))

    # Serialize the RDF graph to a file
    graph.serialize(rdf_file, format='xml')

if __name__ == "__main__":
    xml_file_path = "data.xml"
    rdf_file_path = "data.rdf"

    convert_xml_to_rdf(xml_file_path, rdf_file_path)
