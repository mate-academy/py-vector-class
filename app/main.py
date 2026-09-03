import math


class Vector:
    def __init__(
        self,
        x_coordinate: float | int,
        y_coordinate: float | int,
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: "Vector | float") -> "float | Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        magnitude = self.get_length()

        if magnitude == 0:
            return Vector(0, 0)

        return Vector(
            self.x / magnitude,
            self.y / magnitude,
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        return round(
            math.degrees(
                math.acos(dot_product / lengths_product)
            )
        )

    def get_angle(self) -> float:
        return round(
            abs(
                math.degrees(
                    math.atan2(self.x, self.y)
                )
            )
        )

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cosine = math.cos(radians)
        sine = math.sin(radians)

        new_x_coordinate = (
            self.x * cosine - self.y * sine
        )
        new_y_coordinate = (
            self.x * sine + self.y * cosine
        )

        return Vector(
            new_x_coordinate,
            new_y_coordinate,
        )
