import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, int,
                "Vector"]) -> Union[float, int, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        raise TypeError(f"Unsupported operand for __mul__: {type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        length1 = self.get_length() * other.get_length()
        cos_angle = dot_product / length1
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> float:
        # Вектор осі Y
        y_axis_vector = Vector(0, 1)

        # Скалярний добуток
        dot_product = self.x * y_axis_vector.x + self.y * y_axis_vector.y

        # Добуток довжин векторів
        length_product = self.get_length() * y_axis_vector.get_length()

        # Якщо один з векторів нульовий, кут дорівнює 0
        if length_product == 0:
            return 0

        # Обчислення косинуса кута
        cos_angle = dot_product / length_product

        # Обмеження значення для acos
        cos_angle = max(-1.0, min(1.0, cos_angle))

        # Обчислення кута в радіанах та конвертація в градуси
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        coord_x = (self.x * cos) - (self.y * sin)
        coord_y = (self.x * sin) + (self.y * cos)
        return Vector(round(coord_x, 2), round(coord_y, 2))
