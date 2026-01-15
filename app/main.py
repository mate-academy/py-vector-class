from typing import Union
import math


class Vector:

    def __init__(self, x_vectror: float, y_vectro: float) -> None:
        self.x = round(x_vectror, 2)
        self.y = round(y_vectro, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            x_new = round(self.x + other.x, 2)
            y_new = round(self.y + other.y, 2)
            return Vector(x_vectror=x_new, y_vectro=y_new)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            x_new = round(self.x - other.x, 2)
            y_new = round(self.y - other.y, 2)
            return Vector(x_vectror=x_new, y_vectro=y_new)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            x_new = self.x * other.x
            y_new = self.y * other.y
            return x_new + y_new
        elif isinstance(other, (int, float)):
            x_new = self.x * other
            y_new = self.y * other
            return Vector(x_vectror=x_new, y_vectro=y_new)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        dx = round(end_point[0] - start_point[0], 2)
        dy = round(end_point[1] - start_point[1], 2)
        return cls(x_vectror=dx, y_vectro=dy)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("I can't normalized zro vector")
        dx = self.x / length
        dy = self.y / length
        return Vector(x_vectror=dx, y_vectro=dy)

    def angle_between(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError("Error type")
        if self.get_length() == 0 or other.get_length() == 0:
            raise ValueError("I can't use zero vectors")
        a_b = self.x * other.x + self.y * other.y
        mod_a = (self.x ** 2 + self.y ** 2) ** 0.5
        mod_b = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_vectors = a_b / (mod_a * mod_b)
        angel = math.degrees(math.acos(cos_vectors))
        return int(round(angel, 0))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("I can't return zero vectors")
        a_b = self.y
        mod_a = (self.x ** 2 + self.y ** 2) ** 0.5
        mod_b = 1 ** 0.5
        cos_vectors = a_b / (mod_a * mod_b)
        angel = math.degrees(math.acos(cos_vectors))
        return int(round(angel, 0))

    def rotate(self, angel: int) -> "Vector":
        length = self.get_length
        if length == 0:
            raise ValueError("I can't use zero vectors")
        x_cos = self.x * math.cos(math.radians(angel))
        x_sin = self.y * math.sin(math.radians(angel))
        x2 = x_cos - x_sin
        y_sin = self.x * math.sin(math.radians(angel))
        y_cos = self.y * math.cos(math.radians(angel))
        y2 = y_cos + y_sin
        return Vector(x_vectror=round(x2, 2), y_vectro=round(y2, 2))
