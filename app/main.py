import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            self.x / Vector.get_length(self), self.y / Vector.get_length(self)
        )

    def angle_between(self, other) -> int:
        mul = Vector.get_length(self) * Vector.get_length(other)
        return round(
            math.degrees(math.acos(
                Vector.__mul__(self, other) / (mul))), 0)

    def get_angle(self) -> int:
        y = Vector(0, 1)
        return Vector.angle_between(self, y)

    def rotate(self, degrees: int):
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        x1 = self.x * cs - self.y * sn
        y1 = self.x * sn + self.y * cs
        return Vector(x1, y1)
