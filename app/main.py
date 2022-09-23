import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self):
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, other) -> int:
        scalar_product = self.__mul__(other)
        cos = scalar_product / (self.get_length() * other.get_length())

        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return round(
            math.acos(self.y / self.get_length()) * 180 / math.pi
        )

    def rotate(self, degrees: int):
        cosinus = math.cos(math.radians(degrees))
        sinus = math.sin(math.radians(degrees))

        return Vector(
            cosinus * self.x - sinus * self.y,
            sinus * self.x + cosinus * self.y,
        )
