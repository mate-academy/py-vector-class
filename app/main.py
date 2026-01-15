import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

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
        return self.x * other.x + self.y * other.y

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        cos_a = (self.__mul__(other)) / \
                (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        temp_vector = Vector(0, 1)
        angle = self.angle_between(temp_vector)
        del temp_vector
        return angle

    def rotate(self, angle):
        radians = math.radians(angle)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
