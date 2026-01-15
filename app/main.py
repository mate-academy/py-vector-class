import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float):
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, float | int):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point : tuple, end_point: tuple
    ):
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        res = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(res)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, other):
        radian = math.radians(other)
        return Vector(
            (math.cos(radian) * self.x - math.sin(radian) * self.y),
            (math.sin(radian) * self.x + math.cos(radian) * self.y)
        )
