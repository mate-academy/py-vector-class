import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector2):
        return Vector(self.x + vector2.x, self.y + vector2.y)

    def __sub__(self, vector2):
        return Vector(self.x - vector2.x, self.y - vector2.y)

    def __mul__(self, vector2):
        if isinstance(vector2, (int, float)):
            return Vector(self.x * vector2, self.y * vector2)
        return self.x * vector2.x + self.y * vector2.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, vector):
        cosine = self.__mul__(vector) / \
            (self.get_length() * vector.get_length())
        cosine = math.degrees(math.acos(cosine))
        return round(cosine)

    def get_angle(self):
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degree):
        radian = math.radians(degree)
        return Vector(
            x=self.x * math.cos(radian) - self.y * math.sin(radian),
            y=self.x * math.sin(radian) + self.y * math.cos(radian)
        )
