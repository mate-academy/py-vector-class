import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":

        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: "Vector") -> int:
        cos_a = (
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length())
        )

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        cos_a = self.y / length
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        rad = degrees * math.pi / 180

        x_coordinate = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_coordinate = self.x * math.sin(rad) + self.y * math.cos(rad)

        return Vector(x_coordinate, y_coordinate)
