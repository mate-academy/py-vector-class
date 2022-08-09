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
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def angle_between(self, other):
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        y_axis_vector = Vector(0, abs(self.y))
        return self.angle_between(y_axis_vector)

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def rotate(self, degrees: int):
        new_x = math.cos(math.radians(degrees)) * self.x - \
            math.sin(math.radians(degrees)) * self.y
        new_y = math.sin(math.radians(degrees)) * self.x + \
            math.cos(math.radians(degrees)) * self.y
        return Vector(new_x, new_y)
