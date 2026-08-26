import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: any) -> any:
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, p1: tuple, p2: tuple) -> "Vector":
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between_raw(self, other: "Vector") -> float:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()

        cos_a = dot_product / (self_length * other_length)

        return math.degrees(math.acos(cos_a))

    def angle_between(self, other: "Vector") -> int:
        return int(round(self.angle_between_raw(other), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float) -> "Vector":
        beta_radians = math.radians(angle)

        magnitude = self.get_length()
        x_angle = self.angle_between_raw(Vector(magnitude, 0))
        if self.x < 0 or self.y < 0:
            x_angle = -x_angle

        alpha_radians = math.radians(x_angle)

        x2 = magnitude * math.cos(alpha_radians + beta_radians)
        y2 = magnitude * math.sin(alpha_radians + beta_radians)

        return Vector(x2, y2)
