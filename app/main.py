import math


class Vector:
    def __init__(self, point_x: float | int, point_y: float | int) -> None:
        self.point_x = round(point_x, 2)
        self.point_y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.point_x + other.point_x,
                      self.point_y + other.point_y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.point_x - other.point_x,
                      self.point_y - other.point_y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.point_x * other, self.point_y * other)
        if isinstance(other, Vector):
            return ((self.point_x * other.point_x)
                    + (self.point_y * other.point_y))
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.point_x = end_point[0] - start_point[0]
        cls.point_y = end_point[1] - start_point[1]
        return cls(cls.point_x, cls.point_y)

    def get_length(self) -> float:
        return ((self.point_x) ** 2 + (self.point_y ** 2)) ** .5

    def get_normalized(self) -> Vector:
        normalized = self.get_length()
        return Vector(self.point_x / normalized, self.point_y / normalized)

    def angle_between(self, other: Vector) -> int:
        value = round(math.degrees(math.acos((self * other)
                                             / (self.get_length()
                                                * other.get_length()))))
        return value

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.point_y
                                            / Vector.get_length(self))))

    def rotate(self, by_degree: int) -> Vector:

        new_x = ((math.cos(math.radians(by_degree)) * self.point_x)
                 - (math.sin(math.radians(by_degree)) * self.point_y))
        new_y = ((math.sin(math.radians(by_degree)) * self.point_x)
                 + (math.cos(math.radians(by_degree)) * self.point_y))
        return Vector(new_x, new_y)
