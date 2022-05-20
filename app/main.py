import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        m = (self.x * self.x + self.y * self.y) ** 0.5
        return Vector(self.x / m, self.y / m)

    def angle_between(self, other):
        a = self * other / (Vector.get_length(self) * Vector.get_length(other))
        return int(round(math.degrees(math.acos(a)), 0))

    def get_angle(self):
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, angle: int):
        x = math.cos(math.radians(angle)) * self.x - \
            math.sin(math.radians(angle)) * self.y
        y = math.sin(math.radians(angle)) * self.x + \
            math.cos(math.radians(angle)) * self.y
        return Vector(x, y)
