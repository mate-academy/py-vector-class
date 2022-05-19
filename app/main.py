import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other):
        dot_prod = self * other
        angle = dot_prod / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        angle = math.radians(degrees)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(x, y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) is Vector:
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)
