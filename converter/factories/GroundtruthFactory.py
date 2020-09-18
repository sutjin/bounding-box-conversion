import json
from converter.utils.helper import get_label_id_from_name
from converter.model.PascalVOC import Annotation as PascalVOC
from converter.model.AWS import Object, Dimension, Annotation, \
    BoundingBox, BoundingBoxMetadata, GroundTruth
from dataclasses_serialization.json import JSONSerializer


class Factory:
    s3_path = None

    def __init__(self, s3_path):
        self.s3_path = self._validate_s3_path(s3_path)

    def _annotation_to_groundtruth(self, source):
        class_map = {}

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

            annotation_list.append(
                Annotation(
                    class_id=get_label_id_from_name(item.name),
                    top=item.bnbbox.ymin,
                    left=item.bnbbox.xmin,
                    width=item.bnbbox.xmax,
                    height=item.bnbbox.ymax
                )
            )

            class_map[get_label_id_from_name(item.name)] = item.name

        boundingBox = BoundingBox(
            image_size=[dimension],
            annotations=annotation_list
        )

        boundingBoxMetadata = BoundingBoxMetadata(
            objects=object_list,
            class_map=class_map
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

    def output_file(self, groundtruth=[], output_path='output.manifest'):

        output = open(output_path, "w")

        for gt in groundtruth:
            output.write(
                self._convert_to_string(gt)
            )
            output.write("\n")
        
        output.close()


    @staticmethod
    def _convert_to_string(input):
        f_output = json.dumps(
                    JSONSerializer.serialize(input)
                )
        # TODO: need to find a better way to do this
        f_output = f_output.replace('source_ref' , 'source-ref') \
            .replace('bounding_box' , 'bounding-box') \
            .replace('bounding_box_metadata' , 'bounding-box-metadata') \
            .replace('bounding-box_metadata' , 'bounding-box-metadata') \
            .replace('class_map' , 'class-map') \
            .replace('human_annotated' , 'human-annotated') \
            .replace('creation_date' , 'creation-date') \
            .replace('job_name' , 'job-name')
        return f_output

    def _validate_s3_path(self, input_path):
        if not input_path.startswith("s3://"):
            raise Exception("Path needs to start with s3://")

        if not input_path.endswith("/"):
            input_path += "/"

        return input_path
