from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type(s) for +: "
                            f" 'Vector' and '{type(other).__name__}'")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type(s) for -: "
                            f"'Vector' and '{type(other).__name__}'")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"Unsupported operand type(s) for *: "
                            f"'Vector' and '{type(other).__name__}'")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        if not (isinstance(start_point, tuple)
                and isinstance(end_point, tuple)):
            raise ValueError("start_point and end_point must be tuples")
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError("start_point and end_point"
                             " must have two coordinates each")
        x_coordinate = round(end_point[0] - start_point[0], 2)
        y_coordinate = round(end_point[1] - start_point[1], 2)
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> Vector:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        cos_a = dot_product / (magnitude_self * magnitude_other)
        cos_a = max(-1, min(1, cos_a))
        angle_rad = math.acos(cos_a)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)
        angle_deg -= 90
        if angle_deg < 0:
            angle_deg += 360

        return round(angle_deg, 0)

    def rotate(self, degrees: float) -> Vector:
        angle_rad = math.radians(degrees)
        new_x = round(self.x * math.cos(angle_rad)
                      - self.y * math.sin(angle_rad), 2)
        new_y = round(self.x * math.sin(angle_rad)
                      + self.y * math.cos(angle_rad), 2)
        return Vector(new_x, new_y)
