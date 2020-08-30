"""
    * convert XML into object
    * grab all XML in path - convert to object - store in local and return all.
"""
import xml.etree.ElementTree as ET
from converter.model.PascalVOC import Size, Bndbox, Object, Annotation


class Factory:
    @staticmethod
    def convert_xml_to_annotation(xml_path):
        tree = ET.parse(xml_path)

        size = Size(width=0, height=0, depth=0)
        annotation = Annotation(filename="name", path="", size=size)

        # TODO: loop through and generate object

        annotation.objects = []
        # TODO: loop through the object and 
    