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
        if isinstance(other, (int, float)):
            return Vector(
                x=round(self.x * other, 2),
                y=round(self.y * other, 2)
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        cls.x = start_point[0]
        cls.y = start_point[1]
        return cls(
            x=end_point[0] - cls.x,
            y=end_point[1] - cls.y
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        cos = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self):
        cos = self.y / self.get_length()
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees):
        cos_angle = math.cos(math.radians(degrees))
        sin_angle = math.sin(math.radians(degrees))
        return Vector(
            x=self.x * cos_angle - self.y * sin_angle,
            y=self.x * sin_angle + self.y * cos_angle
        )
