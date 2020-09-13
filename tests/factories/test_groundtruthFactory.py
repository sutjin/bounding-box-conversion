import pytest
import os
from converter.factories.AnnotationFactory import Factory as AnnotationFactory
from converter.factories.GroundtruthFactory import Factory

def test_factory_should_convert_pascalVOC():
    mock_path = 'sample_path/'
    xml_path = os.path.join(os.getcwd(), 'tests', 'resource/sample_annotation.xml')
    result_annotation = AnnotationFactory.convert_xml_to_annotation(xml_path)
    
    factory = Factory(mock_path)
    test_groundtruth = factory.convert_to_groundTruth(result_annotation)

    # TODO: add more assertion between Pascal object and groundtruth object
    assert test_groundtruth.source_ref == mock_path + result_annotation.filename