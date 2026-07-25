import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, int | float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        if (isinstance(start_point, tuple) and isinstance(end_point, tuple)):
            return Vector(end_point[0] - start_point[0],
                          end_point[1] - start_point[1])
        return NotImplemented

    def get_length(self) -> float | int:
        return abs(math.sqrt(self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(self.__mul__(other)
                                            / (self.get_length()
                                               * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, angle: int | float) -> Vector:
        return Vector(self.x * math.cos(math.radians(angle))
                      - self.y * math.sin(math.radians(angle)),
                      self.x * math.sin(math.radians(angle))
                      + self.y * math.cos(math.radians(angle)))
