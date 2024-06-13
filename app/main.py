import math


class Vector:
    def __init__(
            self,
            x: float,
            y: float
    ):
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
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        start_point = cls(start_point[0], start_point[1])
        end_point = cls(end_point[0], end_point[1])
        return end_point - start_point

    def get_length(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self):
        vector_length = self.get_length()
        return Vector(
            x=round(self.x / vector_length, 2),
            y=round(self.y / vector_length, 2)
        )

    def angle_between(self, other):
        first_part = self * other
        second_part = self.get_length() * other.get_length()
        cosine = first_part / second_part
        ange_between_vectors = math.degrees(math.acos(cosine))
        return round(ange_between_vectors)

    def get_angle(self):
        cosine = self.y / self.get_length()
        result = math.degrees(math.acos(cosine))
        return round(result)

    def rotate(self, degrees):
        rad_angle = math.radians(degrees)
        x = math.cos(rad_angle) * self.x - math.sin(rad_angle) * self.y
        y = math.sin(rad_angle) * self.x + math.cos(rad_angle) * self.y
        return Vector(x, y)
