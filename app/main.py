import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(float(x_coordinate), 2)
        self.y = round(float(y_coordinate), 2)
        # Для того тесту, що хоче x_axis
        self.x_axis = self.x
        self.y_axis = self.y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]
                ) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        # Скалярний добуток
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_a = max(-1.0, min(1.0, dot_product / lengths))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
