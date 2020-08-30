import json
import os
from converter.model.common import LabelMap
from dataclasses_serialization.json import JSONSerializer


class Converter:
    __instance = None
    labelmap = []

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Converter.__instance is None:
            Converter()

        return Converter.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Converter.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Converter.__instance = self

    @staticmethod
    def clear():
        try:
            Converter.__instance = None
        except KeyError:
            print('ignoring error')

    def setLabelmap(self, path=None):
        # clear labelmap
        self.labelmap.clear()

        if not path:
            path = os.path.join(os.getcwd(), 'resources/labelmap.json')

        with open(path, 'r') as file:
            data = json.loads(file.read())

        if not isinstance(data, list):
            raise Exception("label map needs to be array!")

        for label in data:
            self.labelmap.append(
                    JSONSerializer.deserialize(LabelMap, label)
                )
