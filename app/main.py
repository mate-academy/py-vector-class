import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: ("Vector", int, float)) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple
                                    , end_point: tuple) -> "Vector":
        return cls((end_point[0] - start_point[0])
                   , (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        if isinstance(self, Vector):
            return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        if isinstance(self, Vector):
            return Vector(self.x / self.get_length()
                          , self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> "Vector":
        return Vector(self.x * math.cos(math.radians(degree))
                      - self.y * math.sin(math.radians(degree))
                      , self.x * math.sin(math.radians(degree))
                      + self.y * math.cos(math.radians(degree)))
