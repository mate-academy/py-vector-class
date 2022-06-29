from math import degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        cls.x = (end_point[0] - start_point[0])
        cls.y = (end_point[1] - start_point[1])
        return Vector(cls.x, cls.y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other):
        mult_vect = Vector.__mul__(self, other)
        abs_vect = Vector.get_length(self) * Vector.get_length(other)
        return round(degrees(acos(mult_vect / abs_vect)))

    def get_angle(self):
        """ >Vektor(0,1)< which I used here it's the
        coordinates of Y axis and its more useful than make
        new staticmethod in this task"""
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, grad):
        angle_radn = radians(grad)
        return Vector(
            self.x * cos(angle_radn) - self.y * sin(angle_radn),
            self.x * sin(angle_radn) + self.y * cos(angle_radn)
        )
