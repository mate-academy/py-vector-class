import math


class Vector:
    def __init__(self, coord_x : float, coord_y : float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other : Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other : Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other : Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return ((self.x * other.x)
                + (self.y * other.y))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_point = tuple(map(lambda x, y : y - x, start_point, end_point))
        return cls(*new_point)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other : Vector) -> int:
        cos_angle = self.__mul__(other) / (self.get_length()
                                           * other.get_length())
        arccos = math.degrees(math.acos(cos_angle))
        return round(arccos)

    def get_angle(self) -> int:
        angle = math.degrees(math.acos(self.y / self.get_length()))
        return round(angle)

    def rotate(self, degrees : int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
