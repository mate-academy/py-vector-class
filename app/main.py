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
        if not isinstance(other, Vector):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

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

    def rotate(self, degrees: int) -> tuple:
        cos_x = self.x * math.cos(math.radians(degrees))
        sin_x = self.x * math.sin(math.radians(degrees))
        cos_y = self.y * math.cos(math.radians(degrees))
        sin_y = self.y * math.sin(math.radians(degrees))

        return Vector(
            round(cos_x - sin_y, 2),
            round(sin_x + cos_y, 2)
        )
