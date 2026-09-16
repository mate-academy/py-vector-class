import math


class Vector:
    def __init__(
            self,
            x: float,  # noqa: VNE001
            y: float,  # noqa: VNE001
    ) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

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
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length,
        )

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (self * vector) / (
            self.get_length() * vector.get_length()
        )

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(abs(self.x), self.y))

        if angle < 0:
            angle += 360

        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )

        new_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(new_x, new_y)
