import math


class Vector:
    def __init__(self, x: int or float, y: int or float):
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
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        divisor = self.get_length() * other.get_length()
        return round(
            math.degrees(math.acos((self * other) / divisor)))

    def get_angle(self):
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degrees: int):
        return \
            Vector(
                self.x * math.cos(math.radians(degrees)) - self.
                y * math.sin(math.radians(degrees)),
                self.x * math.sin(math.radians(degrees)) + self.
                y * math.cos(math.radians(degrees))
            )
