import math


class Vector:
    def __init__(self, x_dot: float, y_dot: float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

    def __add__(self, other: "Vector") -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2),
                      round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        cos_angle = math.cos(math.radians(angle))
        sin_angle = math.sin(math.radians(angle))
        x_dot = cos_angle * self.x - sin_angle * self.y
        y_dot = sin_angle * self.x + cos_angle * self.y
        return Vector(x_dot, y_dot)
