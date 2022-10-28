import math


class Vector:
    def __init__(self, iks: float, igr: float) -> None:
        self.x = round(iks, 2)
        self.y = round(igr, 2)

    def __add__(self, other: callable) -> callable:
        print(type(other))
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: callable) -> callable:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: callable) -> callable:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_points: tuple,
                                    end_points: tuple) -> callable:
        return Vector(round(end_points[0] - start_points[0], 2),
                      round(end_points[1] - start_points[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> callable:
        vector_length = math.sqrt(self.x * self.x + self.y * self.y)
        return Vector(round(self.x / vector_length, 2),
                      round(self.y / vector_length, 2))

    def angle_between(self, other: callable) -> callable:
        mul_vect = round(self.x * other.x + self.y * other.y, 2)
        vector1_length = math.sqrt(self.x * self.x + self.y * self.y)
        vector2_length = math.sqrt(
            other.x * other.x + other.y * other.y)
        return round(math.degrees(
            math.acos(mul_vect / (vector1_length * vector2_length))))

    def get_angle(self) -> callable:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float) -> callable:
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        coord_x = self.x * cs - self.y * sn
        coord_y = self.x * sn + self.y * cs
        return Vector(round(coord_x, 2), round(coord_y, 2))
