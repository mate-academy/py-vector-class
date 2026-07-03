import math


class Vector:

    def __init__(self, point_x: float | int, point_y: float | int) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | int) -> Vector | float | int:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        if isinstance((start_point, end_point), tuple):
            return cls(end_point[0] - start_point[0],
                       end_point[1] - start_point[1])
        return NotImplemented

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        if isinstance(other, Vector):
            cos_a = ((self.x * other.x + self.y * other.y)
                     / (self.get_length() * other.get_length()))
            return round(math.degrees(math.acos(cos_a)))
        return NotImplemented

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)),
                      self.x * math.sin(math.radians(degrees))
                      + self.y * math.cos(math.radians(degrees)))
