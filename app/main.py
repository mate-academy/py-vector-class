import math


class Vector:

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Неможливо обчислити")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Неможливо обчислити")
        dot_prod = self * other
        cos_angle = dot_prod / (len_self * len_other)
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> float:
        length = self.get_length()
        angle = math.acos(self.y / length)
        angle_degrees = math.degrees(angle)
        return round(angle_degrees)

    def rotate(self, angle: float) -> Vector:
        angle_rad = math.radians(angle)

        a_cos = math.cos(angle_rad)
        b_sin = math.sin(angle_rad)

        new_x = a_cos * self.x - self.y * b_sin
        new_y = b_sin * self.x + self.y * a_cos

        return Vector(new_x, new_y)
