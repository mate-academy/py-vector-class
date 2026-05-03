import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float | int") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        numerator = float(self * other)
        denominator = self.get_length() * other.get_length()
        cos_a = max(-1.0, min(1.0, numerator / denominator))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, angle: float) -> "Vector":
        rad = math.radians(angle)
        cos_val = math.cos(rad)
        sin_val = math.sin(rad)
        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val

        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
