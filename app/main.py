import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return ((self.x * other.x)
                    + (self.y * other.y))
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.point_x = end_point[0] - start_point[0]
        cls.point_y = end_point[1] - start_point[1]
        return cls(cls.point_x, cls.point_y)

    def get_length(self) -> float:
        return ((self.x) ** 2 + (self.y ** 2)) ** .5

    def get_normalized(self) -> Vector:
        normalized = self.get_length()
        return Vector(self.x / normalized, self.y / normalized)

    def angle_between(self, other: Vector) -> int:
        value = round(math.degrees(math.acos((self * other)
                                             / (self.get_length()
                                                * other.get_length()))))
        return value

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y
                                            / Vector.get_length(self))))

    def rotate(self, by_degree: int) -> Vector:

        new_x = ((math.cos(math.radians(by_degree)) * self.x)
                 - (math.sin(math.radians(by_degree)) * self.y))
        new_y = ((math.sin(math.radians(by_degree)) * self.x)
                 + (math.cos(math.radians(by_degree)) * self.y))
        return Vector(new_x, new_y)
