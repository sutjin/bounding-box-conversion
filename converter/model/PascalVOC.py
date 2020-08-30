from dataclasses import dataclass


@dataclass
class Size:
    width: int
    height: int
    depth: int


@dataclass
class Bndbox:
    xmin: int
    ymin: int
    xmax: int
    ymax: int


@dataclass
class Object:
    name: str
    bnbbox: Bndbox


@dataclass
class Annotation:
    filename: str
    path: str
    size: Size
    objects: [Object]
