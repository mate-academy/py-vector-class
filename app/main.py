import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y)

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, mult):
        return Vector(
            x=round((self.x * mult), 2),
            y=round((self.y * mult), 2),
        ) if isinstance(mult, int) or isinstance(mult, float) else (
            self.x * mult.x + self.y * mult.y
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (((self.x)**2 + (self.y)**2)**0.5)

    def get_normalized(self):
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, other):
        # xz = self.__mul__(other) / ((self.get_length() * other.get_lenght()))
        m_len = self.get_length() * other.get_length()
        mult = self.__mul__(other)
        xz = mult / m_len
        return round(math.degrees(math.acos(xz)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, grad):
        rad = math.radians(grad)
        return Vector(
            x=math.cos(rad) * self.x - math.sin(rad) * self.y,
            y=math.sin(rad) * self.x + math.cos(rad) * self.y
        )
