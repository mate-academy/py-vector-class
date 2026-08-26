import math


class Vector:
    def __init__(self, xp: float, yp: float) -> None:
        self.x = round(xp, 2)
        self.y = round(yp, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        cos_theta = dot / (len_self * len_other)
        cos_theta = max(min(cos_theta, 1), -1)
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(-self.x, self.y)  # мінус перед x!
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            angle_deg += 360
        return round(angle_deg)

    def rotate(self, angle: float) -> Vector:
        angle_rad = math.radians(angle)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)
