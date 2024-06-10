#!/usr/bin/python3
"""
    serialization and deserialization using XML as an
    alternative format to JSON
"""


def serialize_to_xml(dictionary, filename):
    import xml.etree.ElementTree as ET

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    import xml.etree.ElementTree as ET

    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
