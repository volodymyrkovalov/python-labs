from lxml import etree
import xml.dom.minidom as minidom

def validate_xml_with_dtd(xml_file, dtd_file):
    dtd = etree.DTD(open(dtd_file))
    tree = etree.parse(xml_file)
    is_valid = dtd.validate(tree)
    return is_valid, dtd.error_log.filter_from_errors()

def validate_xml_with_schema(xml_file, schema_file):
    schema_doc = etree.parse(schema_file)
    schema = etree.XMLSchema(schema_doc)
    xml_doc = etree.parse(xml_file)
    is_valid = schema.validate(xml_doc)
    return is_valid, schema.error_log.filter_from_errors()

def pretty_print_xml(xml_file):
    dom = minidom.parse(xml_file)
    pretty_xml_as_string = dom.toprettyxml()
    return pretty_xml_as_string

def save_pretty_xml(xml_file, output_file):
    pretty_xml = pretty_print_xml(xml_file)
    with open(output_file, 'w') as f:
        f.write(pretty_xml)