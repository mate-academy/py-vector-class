import math


class Vector:
    def __init__(self, x_coor: float | int, y_coor: float | int) -> None:
        self.x_coor = round(x_coor, 2)
        self.y_coor = round(y_coor, 2)

    def __add__(self, vector: object) -> object:
        return Vector(
            self.x_coor + vector.x_coor,
            self.y_coor + vector.y_coor
        )

    def __sub__(self, vector: object) -> object:
        return Vector(
            self.x_coor - vector.x_coor,
            self.y_coor - vector.y_coor
        )

    def __mul__(self, multiplier: object | float) -> object | float:
        if isinstance(multiplier, Vector):
            return self.x_coor * multiplier.x_coor + self.y_coor * multiplier.y_coor
        return Vector(
            self.x_coor * multiplier,
            self.y_coor * multiplier
        )

    @classmethod
    def create_vector_by_coor_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> object:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x_coor ** 2 + self.y_coor ** 2) ** 0.5

    def get_normalized(self) -> object:
        return Vector(
            self.x_coor * (1 / Vector.get_length(self)),
            self.y_coor * (1 / Vector.get_length(self))
        )

    def angle_between(self, other: object) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.x_coor * cos - self.y_coor * sin,
            self.x_coor * sin + self.y_coor * cos
        )
