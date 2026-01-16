from math import sin, cos, acos, degrees, radians, sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: int):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: int):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(x=end_point[0] - start_point[0],
                   y=end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length()
                      )

    def angle_between(self, other) -> int:
        return round(degrees(acos(
            (self.__mul__(other)) / (self.get_length() * other.get_length())
        )))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int):
        radian = radians(angle)
        return Vector(
            x=self.x * cos(radian) - self.y * sin(radian),
            y=self.y * cos(radian) + self.x * sin(radian),
        )
