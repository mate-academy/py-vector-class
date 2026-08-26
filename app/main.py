import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate,
        )

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coordinate * other, self.y_coordinate * other
            )
        return round(
            self.x_coordinate * other.x_coordinate
            + self.y_coordinate * other.y_coordinate,
            4,
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate**2 + self.y_coordinate**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(
            self.x_coordinate / length, self.y_coordinate / length
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_product = self.get_length() * other.get_length()
        if len_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = max(-1, min(1, dot_product / len_product))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_rotated = (
            self.x_coordinate * cos_theta - self.y_coordinate * sin_theta
        )
        y_rotated = (
            self.x_coordinate * sin_theta + self.y_coordinate * cos_theta
        )
        return Vector(x_rotated, y_rotated)
