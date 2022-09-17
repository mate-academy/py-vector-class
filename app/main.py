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
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return Vector((end_point[0] - start_point[0]),
                      (end_point[1] - start_point[1]))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        # angle = cos ** (-1) * [ (A dot B) / (|A| * |B|) ]
        numerator = self.__mul__(other)   # (A dot B)
        denominator = self.get_length() * other.get_length()   # (|A| * |B|)
        return round(math.acos(numerator / denominator) * 180 / math.pi)

    def get_angle(self):
        numerator = self.y
        denominator = self.get_length()
        return round(math.acos(numerator / denominator) * 180 / math.pi)

    def rotate(self, degrees: int):
        x = self.x
        y = self.y

        self.x = round((x * math.cos(math.radians(degrees))
                        - y * math.sin(math.radians(degrees))), 2)
        self.y = round((x * math.sin(math.radians(degrees))
                        + y * math.cos(math.radians(degrees))), 2)

        return self
