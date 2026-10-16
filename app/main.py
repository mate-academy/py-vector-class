import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int | float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            raise TypeError("Unsupported type of multiplication")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        x = end_point[0] - start_point[0]  # noqa: VNE001
        y = end_point[1] - start_point[1]  # noqa: VNE001
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def dot(self, other: Vector) -> float:
        return round(self.x * other.x + self.y * other.y, 4)

    def angle_between(self, other: Vector) -> int:
        dot = self.dot(other)
        len_self = self.get_length()
        len_other = other.get_length()
        cos_a = dot / (len_self * len_other)
        angle_rad = math.acos(max(-1, min(1, cos_a)))
        return round(math.degrees(angle_rad))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
