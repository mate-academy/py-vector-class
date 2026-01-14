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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, other):
        dot_prod = Vector.__mul__(self, other)
        if not dot_prod:
            return 90
        prod_magnitudes = Vector.get_length(self) * Vector.get_length(other)
        cos_a = Vector.__mul__(self, other) / prod_magnitudes
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        pos_y_vector = self.__class__(0, 1)
        return self.angle_between(pos_y_vector)

    def rotate(self, degrees: int):
        cos_of_angle = math.cos(math.radians(degrees))
        sin_of_angle = math.sin(math.radians(degrees))
        return Vector(
            x=cos_of_angle * self.x - sin_of_angle * self.y,
            y=sin_of_angle * self.x + cos_of_angle * self.y
        )
