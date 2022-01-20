from math import acos, degrees, radians, sin, cos


class Vector:

    ROUND_DIGITS = 2
    COORD_TYPES = (int, float)

    def __init__(self, x_coord, y_coord):
        if isinstance(x_coord, self.COORD_TYPES) \
                and isinstance(y_coord, self.COORD_TYPES):
            self.x = round(float(x_coord), self.ROUND_DIGITS)
            self.y = round(float(y_coord), self.ROUND_DIGITS)

    def __add__(self, other):
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y,
        )

    def __sub__(self, other):
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y,
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, self.COORD_TYPES):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other,
            )
        else:
            raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0], end_point[1]) \
            - Vector(start_point[0], start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self):
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length(),
        )

    def angle_between(self, other):
        angle_cos = self * other / (self.get_length() * other.get_length())
        return round(degrees(acos(angle_cos)))

    def get_angle(self):
        return self.angle_between(Vector(0.0, 1.0))

    def rotate(self, deg):
        rad = radians(deg)
        return Vector(
            x_coord=self.x * cos(rad) - self.y * sin(rad),
            y_coord=self.x * sin(rad) + self.y * cos(rad),
        )
