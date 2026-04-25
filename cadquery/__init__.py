"""CadQuery - A parametric 3D CAD scripting framework built on top of OCCT.

CadQuery is a Python library that allows you to create 3D models using
a fluent, chainable API. It's built on top of OpenCASCADE Technology (OCCT)
via the pythonOCC bindings.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)

Note: I'm using this fork for learning CadQuery internals. The upstream
project lives at https://github.com/CadQuery/cadquery.

Personal notes:
- CompSolid is rarely used in practice; it represents a collection of solids
  sharing faces. Mostly encountered when working with STEP imports.
- StringSyntaxSelector is the magic behind the ">X" / "<Y" string selectors.
- Assembly uses a constraint solver under the hood (see assembly.py).
"""

from .cq import (
    CQContext,
    CQ,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    BoundBox,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .occ_impl.exporters import (
    exporters,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .assembly import (
    Assembly,
    Color,
    Constraint,
)
from .sketch import Sketch

__version__ = "2.4.0"
__author__ = "CadQuery Authors"
__license__ = "Apache License 2.0"

__all__ = [
    # Core workplane
    "CQContext",
    "CQ",
    "Workplane",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Exporters
    "exporters",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Assembly
    "Assembly",
    "Color",
    "Constraint",
    # Sketch
    "Sketch",
    # Metadata
    "__version__",
]
