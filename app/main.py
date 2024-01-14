from __future__ import annotations
from math import sqrt, acos, degrees, atan2, radians, cos, sin

class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector / float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(x=end_point[0] - start_point[0], y=end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(x=self.x / Vector.get_length(self), y=self.y / Vector.get_length(self))

    def angle_between(self, other: Vector) -> int | float:
        numerator = Vector.__mul__(self, other)
        demominator = Vector.get_length(self) * Vector.get_length(other)
        return round(degrees(acos(numerator / demominator)))

    def get_angle(self) -> int | float:
        return abs(int(degrees(atan2(self.x, self.y))))

    def rotate(self, deg: int | float) -> Vector:
        deg_to_radians = radians(deg)
        rotation_matrix = [
            [cos(deg_to_radians), -sin(deg_to_radians)],
            [sin(deg_to_radians), cos(deg_to_radians)]
        ]
        rotaded_x = rotation_matrix[0][0] * self.x + rotation_matrix[0][1] * self.y
        rotated_y = rotation_matrix[1][0] * self.x + rotation_matrix[1][1] * self.y

        return Vector(x=rotaded_x, y=rotated_y)

vector = Vector(33, 8)
vector2 = vector.rotate(45)

print(vector2.x) #== 17.68
print(vector2.y) #== 28.99