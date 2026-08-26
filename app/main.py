import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:  # noqa: VNE001
        x_val = float(x)
        y_val = float(y)

        self.x_coord = round(x_val, 2)
        self.y_coord = round(y_val, 2)

    @property
    def x(self) -> float:
        return self.x_coord

    @property
    def y(self) -> float:
        return self.y_coord

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(x=round((self.x + other.x), 2),
                      y=round((self.y + other.y), 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(x=round((self.x - other.x), 2),
                      y=round((self.y - other.y), 2))

    def __mul__(self, other: "int | float | Vector") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(x=(self.x * other),
                          y=(self.y * other))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float | int, float | int],
            end_point: tuple[float | int, float | int]
    ) -> "Vector":
        return Vector(x=round((end_point[0] - start_point[0]), 2),
                      y=round((end_point[1] - start_point[1]), 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(x=round(self.x / length, 2),
                      y=round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        return round(
            math.degrees(
                math.acos(
                    dot_product / (self.get_length() * other.get_length())
                )
            ))

    def get_angle(self) -> int:
        length = float(self.get_length())
        if length == 0:
            raise ValueError(
                "Cannot compute angle for zero-length vector"
            )
        cos_theta = float(self.y) / length
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_rad = math.acos(cos_theta)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_cos = self.x * math.cos(radians)
        y_sin = self.y * math.sin(radians)
        x_sin = self.x * math.sin(radians)
        y_cos = self.y * math.cos(radians)
        return (Vector(
            x=round((x_cos - y_sin), 2),
            y=round((x_sin + y_cos), 2)
        ))
