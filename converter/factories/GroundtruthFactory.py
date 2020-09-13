from converter.factories.helper import get_label_id_from_name
from converter.model.PascalVOC import Annotation as PascalVOC
from converter.model.AWS import Object, Dimension, Annotation, \
    BoundingBox, BoundingBoxMetadata, GroundTruth


class Factory:
    s3_path = None

    def __init__(self, s3_path):
        self.s3_path = s3_path  # TODO: make sure its a valid s3 path

    def _annotation_to_groundtruth(self, source):
        dimension = Dimension(
            width=source.size.width,
            height=source.size.height,
            depth=source.size.depth
        )

        annotation_list = []
        object_list = []

        for item in source.objects:
            object_list.append(
                Object(
                    confidence=1
                )
            )

            # TODO: create converter,
            # figure out how to calculate value from pascal
            annotation_list.append(
                Annotation(
                    class_id=get_label_id_from_name(item.name),
                    top=1,
                    left=1,
                    width=1,
                    height=1
                )
            )

        boundingBox = BoundingBox(
            image_size=[dimension],
            annotations=annotation_list
        )

        boundingBoxMetadata = BoundingBoxMetadata(
            objects=object_list,
            class_map={}
        )

        return GroundTruth(
            source_ref=self.s3_path + source.filename,
            bounding_box=boundingBox,
            bounding_box_metadata=boundingBoxMetadata
        )

    def convert_to_groundTruth(self, source):
        if isinstance(source, PascalVOC):
            return self._annotation_to_groundtruth(source)

        return None

    def generate_groundtruths(self, annotations):
        result = []

        for annotation in annotations:
            result.append(self.convert_to_groundTruth(annotation))

        return result


    @staticmethod
    def output_file():
        print('this is where we print the file')
