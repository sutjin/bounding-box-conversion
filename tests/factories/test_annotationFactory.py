import pytest
import os
from converter.factories.AnnotationFactory import Factory


def test_factory_should_discover_xml():
    test_filename = "2fa8dca9b46244f68249f7772d7bd998.jpg"
    factory = Factory()
    result = factory.generate_from_directory(
        os.path.join(os.getcwd(), 'tests', 'resource')
    )

    assert len(result) == 1
    assert result[0].filename == test_filename



def test_factory_should_convert_xml():
    test_result = {
        "filename": "2fa8dca9b46244f68249f7772d7bd998.jpg",
        "size": {
            "width": 550,
            "height": 360,
            "depth": 3
        },
        "object_count": 2
    }
    xml_path = os.path.join(os.getcwd(), 'tests', 'resource/sample_annotation.xml')
    result_annotation = Factory.convert_xml_to_annotation(xml_path)
    
    assert result_annotation.filename == test_result['filename']
    assert result_annotation.size.width == test_result['size']['width']
    assert result_annotation.size.height == test_result['size']['height']
    assert result_annotation.size.depth == test_result['size']['depth']
    assert len(result_annotation.objects) == test_result['object_count']