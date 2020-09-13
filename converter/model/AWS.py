from dataclasses import dataclass
import datetime


@dataclass
class Object:
    confidence: int


@dataclass
class Dimension:
    width: int
    height: int
    depth: int


@dataclass
class Annotation:
    class_id: int
    top: int
    left: int
    width: int
    height: int


@dataclass
class BoundingBox:
    image_size: [Dimension]
    annotations: [Annotation]


@dataclass
class BoundingBoxMetadata:
    objects: [Object]
    class_map: dict
    type: str = 'groundtruth/object-detection'
    human_annotated: str = 'yes'
    creation_date: str = str(datetime.datetime.now())
    job_name: str = 'manual-conversion'


@dataclass
class GroundTruth:
    source_ref: str
    bounding_box: BoundingBox
    bounding_box_metadata: BoundingBoxMetadata
