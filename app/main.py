from typing import Union
import math


class Vector:
    def __init__(
            self,
            x_cor: Union[float, int],
            y_cor: Union[float, int]
    ) -> None:

        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: object) -> object:
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> object:
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[int, float, object]

    ) -> Union[object, float, int]:

        if isinstance(other, Union[float, int]):
            result_of_mul = self.__class__(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

            return result_of_mul

        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> object:

        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> Union[float, int]:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> object:

        length = self.get_length()

        return self.__class__(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: object) -> Union[int, float]:

        length = self.get_length() * other.get_length()
        cos_a = self.__mul__(other) / length

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:

        zero_x_vector = Vector(0, abs(self.y))
        length = self.get_length() * zero_x_vector.get_length()
        cos_a = self.__mul__(zero_x_vector) / length

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: Union[int, float]) -> object:

        angle_cos = math.cos(math.radians(degrees))
        angle_sin = math.sin(math.radians(degrees))

        return self.__class__(
            self.x * angle_cos - angle_sin * self.y,
            self.x * angle_sin + self.y * angle_cos
        )
