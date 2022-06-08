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
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        mul_length = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(self.__mul__(other) / mul_length)))

    def get_angle(self):
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degrees):
        x_part_1 = math.cos(math.radians(degrees)) * self.x
        x_part_2 = math.sin(math.radians(degrees)) * self.y
        y_part_1 = math.sin(math.radians(degrees)) * self.x
        y_part_2 = math.cos(math.radians(degrees)) * self.y
        return Vector(x_part_1 - x_part_2, y_part_1 + y_part_2)
