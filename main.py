from os import path
from converter import Converter
from converter.factories.AnnotationFactory import Factory as A_Factory
from converter.factories.GroundtruthFactory import Factory as G_Factory

if __name__ == "__main__":
    Converter().setLabelmap()

    annotationFactory = A_Factory()
    groundtruthFactory = G_Factory('s3://somepath/')

    pascal_annotation = annotationFactory.generate_from_directory(path=path.join('tests/resource'))
    groundtruth_annotation = groundtruthFactory.generate_groundtruths(pascal_annotation)

    groundtruthFactory.output_file(groundtruth=groundtruth_annotation)

