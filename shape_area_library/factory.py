from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.base import Shape

def create_shape(shape_type: str, *args) -> Shape:
    shape_type = shape_type.lower()
    if shape_type == "circle":
        return Circle(*args)
    elif shape_type == "triangle":
        return Triangle(*args)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")
