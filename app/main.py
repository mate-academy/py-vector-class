import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"Unsupported operand types for *: "
                            f"'Vector' and '{type(other).__name__}'")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> "Vector":
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            angle_deg += 360
        angle_deg = (360 - angle_deg) % 360
        return round(angle_deg)

    def angle_between(self, other: "Vector") -> int:
        dot_prod = self * other  # iloczyn skalarny
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = dot_prod / (len_self * len_other)
        cos_angle = max(min(cos_angle, 1), -1)
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
