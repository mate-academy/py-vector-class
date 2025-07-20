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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        cos_a = (self.x * other.x + self.y * other.y) / (
            self.get_length() * other.get_length()
        )
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
