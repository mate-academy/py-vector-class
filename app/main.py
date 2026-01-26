from math import sqrt, acos, degrees, radians, sin, cos


class Vector:

    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        return self

    def angle_between(self, other: Vector) -> int:
        a_norm = self.get_normalized()
        b_norm = other.get_normalized()
        dot = a_norm * b_norm
        return round(degrees(acos(dot)))

    def get_angle(self) -> int:
        a_norm = self.get_normalized()
        y_axis = Vector(0, 1)
        return a_norm.angle_between(y_axis)

    def rotate(self, angle: int) -> Vector:
        angle_rad = radians(angle)
        x_ = self.x * cos(angle_rad) - self.y * sin(angle_rad)
        y_ = self.x * sin(angle_rad) + self.y * cos(angle_rad)
        return Vector(x_, y_)
