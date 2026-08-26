import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, Vector):
            # dot product
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
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_prod = self * other
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_angle = max(min(dot_prod / lengths, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_theta = max(min(self.y / length, 1), -1)
        angle_rad = math.acos(cos_theta)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_rad = math.cos(rad)
        sin_rad = math.sin(rad)
        x_new = self.x * cos_rad - self.y * sin_rad
        y_new = self.x * sin_rad + self.y * cos_rad
        return Vector(x_new, y_new)
