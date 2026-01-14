import math as m


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start, end):
        return cls(
            end[0] - start[0],
            end[1] - start[1]
        )

    def get_length(self):
        return m.sqrt(self.x**2 + self.y**2)

    def get_normalized(self):
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other):
        product = self.__mul__(other)
        angle = product / (abs(self.get_length()) * abs(other.get_length()))
        return round(m.degrees(m.acos(angle)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, other):
        x = m.cos(m.radians(other)) * self.x - m.sin(m.radians(other)) * self.y
        y = m.sin(m.radians(other)) * self.x + m.cos(m.radians(other)) * self.y
        return Vector(x, y)
