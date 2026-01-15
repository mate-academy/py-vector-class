from math import acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_angle)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, angles):
        x = cos(radians(angles)) * self.x - sin(radians(angles)) * self.y
        y = cos(radians(angles)) * self.y + sin(radians(angles)) * self.x
        return Vector(x, y)
