import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)  # noqa: VNE001
        self.y = round(y, 2)  # noqa: VNE001

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> "Vector":
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, vector: "Vector") -> int:
        cos_a = self * vector / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        degrees_rad = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(degrees_rad) - self.y * math.sin(degrees_rad),
            y=self.x * math.sin(degrees_rad) + self.y * math.cos(degrees_rad)
        )
