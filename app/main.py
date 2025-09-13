import math
from typing import Tuple, Union


class Vector:
    def __init__(
        self,
        x: float,
        y: float,
        precision: int = 2
    ) -> None:
        self.x = round(x, precision)
        self.y = round(y, precision)
        self._precision = precision

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self._precision
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self._precision
        )

    def __mul__(
        self,
        other: Union["Vector", float, int]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other,
                self._precision
            )
        if isinstance(other, Vector):
            return round(
                self.x * other.x
                + self.y * other.y,
                4
            )
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector":
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            math.isclose(
                self.x,
                other.x,
                abs_tol=10 ** -self._precision
            )
            and math.isclose(
                self.y,
                other.y,
                abs_tol=10 ** -self._precision
            )
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
        precision: int = 2
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
            precision
        )

    def get_length(self) -> float:
        return round(
            math.hypot(self.x, self.y),
            self._precision
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0, self._precision)
        return Vector(
            self.x / length,
            self.y / length,
            self._precision
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = dot_product / length_product
        cos_angle = max(-1, min(1, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self, axis: str = "y") -> int:
        length = self.get_length()
        if length == 0:
            return 0
        if axis == "y":
            cos_angle = self.y / length
        elif axis == "x":
            cos_angle = self.x / length
        else:
            raise ValueError("Axis must be 'x' or 'y'")
        cos_angle = max(-1, min(1, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

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
        return Vector(new_x, new_y, self._precision)

    def __repr__(self) -> str:
        return
