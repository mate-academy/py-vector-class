import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other):
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        numerator = self.x * other.x + self.y * other.y
        sqrt_1 = math.sqrt(self.x ** 2 + self.y ** 2)
        sqrt_2 = math.sqrt(other.x ** 2 + other.y ** 2)
        radians = math.acos(numerator / (sqrt_1 * sqrt_2))
        return round(math.degrees(radians))

    def get_angle(self):
        dif = self.x * 0 + self.y * 1
        sqrt_1 = math.sqrt(self.x ** 2 + self.y ** 2)
        sqrt_2 = math.sqrt(0 ** 2 + 1 ** 2)
        radians = math.acos(dif / (sqrt_1 * sqrt_2))
        return round(math.degrees(radians))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
