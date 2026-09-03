import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float") -> "float | Vector":
        return (
            (self.x * other.x) + (self.y * other.y)
            if isinstance(other, Vector)
            else Vector(self.x * other, self.y * other)
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
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(other)
                    / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> float:
        return round(
            abs(math.degrees(math.atan2(self.x, self.y)))
        )

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_val = math.cos(rad)
        sin_val = math.sin(rad)

        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val

        return Vector(new_x, new_y)
