import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple,
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        denom = self.get_length() * other.get_length()

        cos_a = dot / denom
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        cos_a = self.y / length
        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        theta = math.radians(degrees)

        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)

        return Vector(new_x, new_y)
