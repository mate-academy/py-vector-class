import math


class Vector:
    # write your code here
    pass

    def __init__(self, x_coord: int, y_coord: int) -> callable:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: int) -> callable:
        return Vector(x_coord=self.x + other.x, y_coord=self.y + other.y)

    def __sub__(self, other: int) -> callable:
        return Vector(x_coord=self.x - other.x, y_coord=self.y - other.y)

    def __mul__(self, other: int) -> callable:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> callable:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> callable:
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> callable:
        return Vector(self.x / Vector.get_length(self),
                      self.y / Vector.get_length(self))

    def angle_between(self, other: object) -> callable:
        cos_angle = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> callable:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> object:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
