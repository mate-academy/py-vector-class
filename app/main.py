import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other: float | int | Vector) -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float, float],
            end_point: tuple[float, float]) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length < 1e-12:
            return Vector(0, 0)
        nx = self.x / length
        ny = self.y / length
        return Vector(nx, ny)

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        len1 = self.get_length()
        len2 = other.get_length()
        prod = len1 * len2
        if prod < 1e-12:
            return 0
        cos_a = dot / prod
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        if abs(self.x) < 1e-12 and abs(self.y) < 1e-12:
            return 0
        angle_x_deg = math.degrees(math.atan2(self.y, self.x))
        angle_from_y = 90 - angle_x_deg
        angle_from_y = angle_from_y % 360
        return round(angle_from_y)

    def rotate(self, angle_deg: int) -> "Vector":
        theta = math.radians(angle_deg)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        x_new = self.x * cos_t - self.y * sin_t
        y_new = self.x * sin_t + self.y * cos_t
        return Vector(x_new, y_new)
