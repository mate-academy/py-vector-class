from math import acos, degrees, radians, cos, sin


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other,
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector):
        cos_up = self.x * vector.x + self.y * vector.y
        cos_down1 = self.x ** 2 + self.y ** 2
        cos_down2 = vector.x ** 2 + vector.y ** 2
        cos_down = (cos_down1 * cos_down2) ** 0.5
        cos_end = cos_up / cos_down
        radi_cos = acos(cos_end)
        return round(degrees(radi_cos))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        return Vector(
            x=cos(radians(degrees)) * self.x - sin(radians(degrees)) * self.y,
            y=sin(radians(degrees)) * self.x + cos(radians(degrees)) * self.y
        )
