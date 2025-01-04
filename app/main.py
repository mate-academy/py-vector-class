from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord + other.x_coord, self.y_coord
                      + other.y_coord)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord - other.x_coord, self.y_coord
                      - other.y_coord)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x_coord * other, 2),
                          round(self.y_coord * other, 2))
        elif isinstance(other, Vector):
            dot_product = (self.x_coord * other.x_coord + self.y_coord
                           * other.y_coord)
            return dot_product
        else:
            raise TypeError(f"Unsupported operation for * with type "
                            f"{type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_coord_diff = end_point[0] - start_point[0]
        y_coord_diff = end_point[1] - start_point[1]
        return cls(x_coord_diff, y_coord_diff)

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        else:
            return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with a "
                             "0 length vector.")
        cos_angle = max(min(dot_product / lengths_product, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float:
        reference = Vector(0, 1)
        return self.angle_between(reference)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x_coord = (self.x_coord * math.cos(radians) - self.y_coord
                       * math.sin(radians))
        new_y_coord = (self.x_coord * math.sin(radians) + self.y_coord
                       * math.cos(radians))
        return Vector(new_x_coord, new_y_coord)
