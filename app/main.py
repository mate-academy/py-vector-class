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
        if isinstance(other, float) or isinstance(other, int):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self):
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self):
        length = self.get_length()
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other):
        mul = self.__mul__(other)
        length_self = self.get_length()
        length_other = other.get_length()
        angle = mul / (length_other * length_self)
        return round(math.degrees(math.acos(angle)))

    def get_angle(self):
        positive_y = Vector(0, 10)
        return self.angle_between(positive_y)

    def rotate(self, degrees):
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        x = self.x * cs - self.y * sn
        y = self.x * sn + self.y * cs
        return Vector(round(x, 2), round(y, 2))
