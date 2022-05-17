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
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (
            math.sqrt(self.x ** 2 + self.y ** 2)
        )

    def get_normalized(self):
        inv_length = 1 / Vector.get_length(self)
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other):
        cos_a = ((self * other)
                 / (Vector.get_length(self)
                    * Vector.get_length(other)))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        other = Vector(0, 1)
        cos_a = ((self * other)
                 / (Vector.get_length(self)
                    * Vector.get_length(other)))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        return Vector(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )
