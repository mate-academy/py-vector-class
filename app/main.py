import math


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.end_x: float = round(end_x, 2)
        self.end_y: float = round(end_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        result_x: float = self.end_x + other.end_x
        result_y: float = self.end_y + other.end_y
        return Vector(result_x, result_y)

    def __sub__(self, other: "Vector") -> "Vector":
        result_x: float = self.end_x - other.end_x
        result_y: float = self.end_y - other.end_y
        return Vector(result_x, result_y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            result_x: float = self.end_x * other
            result_y: float = self.end_y * other
            return Vector(result_x, result_y)
        if isinstance(other, Vector):
            dot_product: float = float(
                self.end_x * other.end_x + self.end_y * other.end_y
            )
            return round(dot_product, 2)
        raise TypeError(
            "Multiplicação suportada apenas por número ou outro Vector"
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        start_x: float
        start_y: float
        end_x: float
        end_y: float
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        length: float = math.sqrt(self.end_x**2 + self.end_y**2)
        return round(length, 2)

    def get_normalized(self) -> "Vector":
        length: float = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        normalized_x: float = self.end_x / length
        normalized_y: float = self.end_y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other_vector: "Vector") -> int:
        dot: float = float(self * other_vector)
        length_self: float = self.get_length()
        length_other: float = other_vector.get_length()
        if length_self == 0 or length_other == 0:
            return 0
        cos_angle: float = float(dot / (length_self * length_other))
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad: float = math.acos(cos_angle)
        angle_deg: float = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        axis_y: Vector = Vector(0.0, 1.0)
        return self.angle_between(axis_y)

    def rotate(self, degrees: int) -> "Vector":
        rad: float = math.radians(degrees)
        cos_angle: float = math.cos(rad)
        sin_angle: float = math.sin(rad)
        rotated_x: float = self.end_x * cos_angle - self.end_y * sin_angle
        rotated_y: float = self.end_x * sin_angle + self.end_y * cos_angle
        return Vector(rotated_x, rotated_y)
