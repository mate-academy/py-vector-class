import math
from typing import Union, Tuple
from decimal import Decimal, ROUND_HALF_UP


def _round2(value: float) -> float:
    """Round to 2 decimals using decimal HALF_UP."""
    return float(
        Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )


class Vector:
    attr_x: float
    attr_y: float

    def __init__(self, coord_x: float, coord_y: float) -> None:
        # Attributes rounded to two decimals
        self.x = _round2(float(coord_x))
        self.y = _round2(float(coord_y))

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        result_x = _round2(self.x + other.x)
        result_y = _round2(self.y + other.y)
        result_vector = Vector(0, 0)
        result_vector.x = result_x
        result_vector.y = result_y
        return result_vector

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        result_x = _round2(self.x - other.x)
        result_y = _round2(self.y - other.y)
        result_vector = Vector(0, 0)
        result_vector.x = result_x
        result_vector.y = result_y
        return result_vector

    def __mul__(
        self, other: Union[float, int, "Vector"]
    ) -> Union["Vector", float, int]:
        if isinstance(other, (int, float)):
            result_x = _round2(self.x * float(other))
            result_y = _round2(self.y * float(other))
            result_vector = Vector(0, 0)
            result_vector.x = result_x
            result_vector.y = result_y
            return result_vector
        elif isinstance(other, Vector):
            # Dot product: raw float, no rounding (tests expect exact value)
            return self.x * other.x + self.y * other.y
        return NotImplemented

    __rmul__ = __mul__

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        delta_x = _round2(end_point[0] - start_point[0])
        delta_y = _round2(end_point[1] - start_point[1])
        result_vector = cls(0, 0)
        result_vector.x = delta_x
        result_vector.y = delta_y
        return result_vector

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        norm_x = _round2(self.x / length)
        norm_y = _round2(self.y / length)
        normalized_vector = Vector(0, 0)
        normalized_vector.x = norm_x
        normalized_vector.y = norm_y
        return normalized_vector

    def angle_between(self, other: "Vector") -> int:
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0
        dot_product = (self.x * other.x) + (self.y * other.y)
        cos_angle = max(-1.0, min(1.0, dot_product / lengths_product))
        return int(round(math.degrees(math.acos(cos_angle))))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_angle = max(-1.0, min(1.0, self.y / length))
        return int(round(math.degrees(math.acos(cos_angle))))

    def rotate(self, degrees: int) -> "Vector":
        radians_angle = math.radians(degrees)
        part1 = self.x * math.cos(radians_angle)
        part2 = self.y * math.sin(radians_angle)
        new_x_coord = part1 - part2
        part3 = self.x * math.sin(radians_angle)
        part4 = self.y * math.cos(radians_angle)
        new_y_coord = part3 + part4
        rotated_x = _round2(new_x_coord)
        rotated_y = _round2(new_y_coord)
        rotated_vector = Vector(0, 0)
        rotated_vector.x = rotated_x
        rotated_vector.y = rotated_y
        return rotated_vector

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
