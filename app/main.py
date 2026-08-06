from math import sqrt, degrees, acos, radians, cos, sin


class Vector:

    def __init__(self, x: (int, float), y: (int, float)) -> None:

        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            self.x * other,
            self.y * other,)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, other):
        return round(degrees(acos(
            self.__mul__(other) / (self.get_length() * other.get_length()
                                   ))))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        rad_degrees = radians(degrees)
        return Vector(
            (cos(rad_degrees) * self.x) - (sin(rad_degrees) * self.y),
            (sin(rad_degrees) * self.x) + (cos(rad_degrees) * self.y))
