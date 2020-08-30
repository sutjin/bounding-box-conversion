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
    image_size: list[Dimension]
    annotations: list[Annotation]


@dataclass
class BoundingBoxMetadata:
    objects: [Object]
    class_map: dict
    type: str
    human_annotated: str
    creation_date: str = datetime.datetime.now()
    job_name: str = ''


@dataclass
class GroundTruth:
    source_ref: str
    bounding_box: BoundingBox
    bounding_box_metadata: BoundingBoxMetadata
