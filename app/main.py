import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        raise TypeError

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        if len(start_point) != 2 or len(end_point) != 2:
            raise TypeError
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ZeroDivisionError
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> float | int:
        angle = math.degrees(math.atan2(-self.x, self.y))
        return int(round(angle % 360))

    def angle_between(self, other: Vector) -> int:
        dot = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        angle_rad = math.acos(dot / (len_self * len_other))
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def rotate(self, angle: float | int) -> Vector:
        radians = math.radians(angle)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
