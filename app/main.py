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
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other):
        cos_a = self.__mul__(other) / \
            (self.get_length() * (other.x**2 + other.y**2)**0.5)
        print(cos_a)
        result = round(math.degrees(math.acos(cos_a)))
        return result

    def get_angle(self):
        other = Vector(0, abs(self.y))
        cos_a = self.__mul__(other) / \
            (self.get_length() * (other.x ** 2 + other.y ** 2) ** 0.5)
        print(cos_a)
        result = round(math.degrees(math.acos(cos_a)))
        return result

    def rotate(self, other):
        cos = math.cos(math.radians(other))
        sin = math.sin(math.radians(other))
        x = cos * self.x - sin * self.y
        y = sin * self.x + cos * self.y
        return Vector(
            x=x,
            y=y
        )
