import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, point1, point2):
        return cls(
            point2[0] - point1[0],
            point2[1] - point1[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 10))

    def rotate(self, degree):
        cos_x = self.x * math.cos(math.radians(degree))
        sin_x = self.x * math.sin(math.radians(degree))
        cos_y = self.y * math.cos(math.radians(degree))
        sin_y = self.y * math.sin(math.radians(degree))
        return Vector(
            round(cos_x - sin_y, 2),
            round(sin_x + cos_y, 2)
        )
