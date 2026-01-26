from __future__ import annotations
import math

class Vector:

    def __init__(self, x: int | Vector, y: int | Vector) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector | int |float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError(f"Cannot add {type(other)} with {type(Vector)}")

    def __sub__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        else:
            raise TypeError(f"Cannot subtract {type(other)} with {type(Vector)}")

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(f"Cannot multiply {type(other)} with {type(Vector)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point) -> Vector:
        if len(start_point) != 2 or  len(end_point) != 2:
            raise ValueError(f"Both points must have exactly 2 coordinates (x, y)")
            # new_x = x2 - x1  #new_y = y2 = y1
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)


    def get_normalized(self):
        length = self.get_length()
        rounded_length = round(length, 2)
        if rounded_length == 0:
            raise ValueError(f"Cannot normalize zero vector")
        vector = Vector(self.x / length,  self.y / rounded_length)
        return vector

    def angle_between(self, vector: Vector) -> float:
        dot = self.x * vector.x + self.y * vector.y
        length_x = self.get_length()
        length_y = vector.get_length()
        if length_x == 0 or length_y == 0:
            raise ValueError(f"something to say")
        cos_a = dot / (length_x * length_y)
        



