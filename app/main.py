import math
from typing import Union, Optional


class Vector:
    def __init__(
        self,
        x_coord: float,
        y_coord: float,
        z_coord: Optional[float] = None,
        precision: int = 2
    ) -> None:
        self.x_coord = round(x_coord, precision)
        self.y_coord = round(y_coord, precision)
        self.z_coord = (
            round(z_coord, precision) if z_coord is not None else None
        )
        self._precision = precision

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord,
            self.z_coord + other.z_coord
            if self.z_coord is not None and other.z_coord is not None
            else None,
            self._precision
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord,
            self.z_coord - other.z_coord
            if self.z_coord is not None and other.z_coord is not None
            else None,
            self._precision
        )

    def __mul__(
        self,
        other: Union["Vector", float, int]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coord * other,
                self.y_coord * other,
                self.z_coord * other if self.z_coord is not None else None,
                self._precision
            )
        if isinstance(other, Vector):
            dot_product = (
                self.x_coord * other.x_coord
                + self.y_coord * other.y_coord
            )
            if self.z_coord is not None and other.z_coord is not None:
                dot_product += self.z_coord * other.z_coord
            return round(dot_product, 4)
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector":
        return self.__mul__(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            math.isclose(
                self.x_coord,
                other.x_coord,
                abs_tol=10 ** -self._precision
            )
            and math.isclose(
                self.y_coord,
                other.y_coord,
                abs_tol=10 ** -self._precision
            )
            and (
                self.z_coord is None and other.z_coord is None
                or self.z_coord is not None and other.z_coord is not None
                and math.isclose(
                    self.z_coord,
                    other.z_coord,
                    abs_tol=10 ** -self._precision
                )
            )
        )

    def get_length(self) -> float:
        components = [self.x_coord, self.y_coord]
        if self.z_coord is not None:
            components.append(self.z_coord)
        return round(
            math.sqrt(sum(c ** 2 for c in components)),
            self._precision
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(
                0,
                0,
                0 if self.z_coord is not None else None,
                self._precision
            )
        return Vector(
            self.x_coord / length,
            self.y_coord / length,
            self.z_coord / length if self.z_coord is not None else None,
            self._precision
        )

    def __repr__(self) -> str:
        if self.z_coord is not None:
            return (
                f"Vector(x={self.x_coord}, "
                f"y={self.y_coord}, z={self.z_coord})"
            )
        return
