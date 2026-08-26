from __future__ import annotations


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        return Vector(self.x / len_vector, self.y / len_vector)

    def angle_between(self, other: Vector) -> float:
        import math
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        import math
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(cos_a * self.x - sin_a * self.y,
                      sin_a * self.x + cos_a * self.y)
