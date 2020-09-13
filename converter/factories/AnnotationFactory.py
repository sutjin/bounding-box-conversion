import os
import xml.etree.ElementTree as ET
from converter.model.PascalVOC import Size, Bndbox, Object, Annotation


class Factory:
    def generate_from_directory(self, path=None):
        result = []

        with os.scandir(path) as dirs:
            for entry in dirs:
                if entry.name.endswith('xml'):
                    annotation = self.convert_xml_to_annotation(
                        os.path.join(path, entry.name)
                    )

                    result.append(annotation)

        return result

    @staticmethod
    def convert_xml_to_annotation(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        size_xml = root.find('size')
        size = Size(
            width=int(size_xml.find('width').text),
            height=int(size_xml.find('height').text),
            depth=int(size_xml.find('depth').text))

        annotation = Annotation(
            filename=root.find('filename').text,
            path="",
            size=size,
            objects=[])

        for child in root.findall('object'):
            boundbox = Bndbox(
                xmin=int(child.find('bndbox').find('xmin').text),
                ymin=int(child.find('bndbox').find('ymin').text),
                xmax=int(child.find('bndbox').find('xmax').text),
                ymax=int(child.find('bndbox').find('ymax').text)
            )
            new_object = Object(
                name=child.find('name').text,
                bnbbox=boundbox
            )

            annotation.objects.append(new_object)

        return annotation
