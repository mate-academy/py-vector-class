import math


class Vector:
    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

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

    def __mul__(
        self,
        other: "Vector | int | float"
    ) -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        if length == 0:
            return Vector(0, 0)

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector: "Vector") -> int:
        lengths_product = (
            self.get_length() * vector.get_length()
        )

        if lengths_product == 0:
            raise ValueError(
                "The angle of a zero-length vector is undefined"
            )

        cos_a = (self * vector) / lengths_product
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(
            math.degrees(math.acos(cos_a))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        return Vector(
            self.x * math.cos(radians)
            - self.y * math.sin(radians),
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )
