import math


class Vector:
    def __init__(self, ox: float, oy: float) -> None:
        self.ox = round(ox, 2)
        self.oy = round(oy, 2)

    def __add__(self, other: "Vector" | int) -> object:
        return Vector(self.ox + other.ox, self.oy + other.oy)

    def __sub__(self, other: "Vector" | int) -> object:
        return Vector(self.ox - other.ox, self.oy - other.oy)

    def __mul__(self, other: "Vector" | int) -> object:
        if isinstance(other, Vector):
            return self.ox * other.ox + self.oy * other.oy
        return Vector(self.ox * other, self.oy * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> object:

        if (not isinstance(start_point, tuple)
                or not isinstance(end_point, tuple)):
            raise TypeError("start_point and end_point must be"
                            " a tuple of two numbers")
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError("start_point and end_point must be"
                             " a tuple of two numbers")
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        length = (self.ox ** 2 + self.oy ** 2) ** 0.5
        return abs(length)

    def get_normalized(self) -> object:
        return Vector(self.ox / self.get_length(), self.oy / self.get_length())

    def angle_between(self, vector: "Vector") -> int:
        dot = self * vector
        len_self = self.get_length()
        len_vector = vector.get_length()
        if len_self == 0 or len_vector == 0:
            raise ValueError("zero vector")
        cos_a = dot / (len_self * len_vector)
        if cos_a > 1:
            cos_a = 1
        elif cos_a < -1:
            cos_a = -1
        radians_angle = math.acos(cos_a)
        degrees_angle = math.degrees(radians_angle)
        return round(degrees_angle)

    def get_angle(self) -> int:
        len_self = self.get_length()
        if len_self == 0:
            raise ValueError("zero vector")
        angle_rad = math.atan2(self.ox, self.oy)
        angle_deg = math.degrees(angle_rad)

        return round(abs(angle_deg))

    def rotate(self, deg: int) -> object:
        rad = math.radians(deg)
        cos_t = math.cos(rad)
        sin_t = math.sin(rad)
        return Vector(self.ox * cos_t - self.oy * sin_t,
                      self.ox * sin_t + self.oy * cos_t)
