import pytest
import os
from converter import Converter
from converter.model.common import LabelMap


@pytest.fixture(autouse=True)
def clear_singleton():
    yield
    Converter.clear()


def test_converter_initialiaze():
    conv_a = Converter()

    with pytest.raises(Exception):
        conv_b = Converter()


def test_converter_same_instance():
    conv_a = Converter()
    conv_b = Converter.getInstance()

    assert conv_a == conv_b

def test_converter_load_labelMap():
    converter = Converter()
    test_labelMap = LabelMap(id=0, type="name")

    converter.setLabelmap()

    assert len(converter.labelmap) == 1
    assert converter.labelmap[0] == test_labelMap

def test_converter_load_labelMap_with_custom_path():
    converter = Converter()
    costum_path = os.path.join(os.getcwd(), 'tests', 'resource/labelmap.json')
    test_labelMap = LabelMap(id=0, type="name")

    converter.setLabelmap(path=costum_path)

    assert len(converter.labelmap) == 1
    assert converter.labelmap[0] == test_labelMap
