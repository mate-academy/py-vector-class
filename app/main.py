import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            x=round((end_point[0] - start_point[0]), 2),
            y=round((end_point[1] - start_point[1]), 2)
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            x=round((self.x / self.get_length()), 2),
            y=round((self.y / self.get_length()), 2)
        )

    def angle_between(self, vector):
        multiplied = self * vector
        mul_len = self.get_length() * vector.get_length()
        cos_a = multiplied / mul_len
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        angle = math.radians(degrees)
        x = math.cos(angle) * self.x - math.sin(angle) * self.y
        y = math.sin(angle) * self.x + math.cos(angle) * self.y
        return Vector(x, y)
