import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x + other.coord_x, self.coord_y + other.coord_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x - other.coord_x, self.coord_y - other.coord_y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)
        return round(self.coord_x * other.coord_x + self.coord_y * other.coord_y, 4)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.coord_x**2 + self.coord_y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.coord_x / length, self.coord_y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with a zero-length vector.")
        cos_angle = max(-1.0, min(1.0, dot_product / lengths_product))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees_to_rotate: int) -> "Vector":
        radians = math.radians(degrees_to_rotate)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        return Vector(
            self.coord_x * cos_angle - self.coord_y * sin_angle,
            self.coord_x * sin_angle + self.coord_y * cos_angle
        )

