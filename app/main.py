from __future__ import annotations

import math
from typing import Union


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        # Округлюємо координати до двох знаків після коми при ініціалізації
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        # Додавання двох векторів
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        # Віднімання двох векторів
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, int, float]) \
            -> Union[Vector, float]:
        # Якщо множимо на інший вектор - повертаємо скалярний добуток
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        # Якщо множимо на число - повертаємо новий масштабований вектор
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Multiplication is only supported"
                            " by Vector or number (int/float).")

    @classmethod
    def create_vector_by_two_points(cls, start_point: list,
                                    end_point: list) -> Vector:
        # Створюємо вектор за двома точками: кінець - початок
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)

    def get_length(self) -> float:

        # Довжина вектора (гіпотенуза)
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        # Нормалізація вектора (перетворення в одиничний вектор)
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> float:
        # Обчислення кута між двома векторами через скалярний добуток
        dot_product = self * vector
        len1 = self.get_length()
        len2 = vector.get_length()

        if len1 == 0 or len2 == 0:
            return 0

        # Знаходимо косинус кута
        cos_a = dot_product / (len1 * len2)

        # Обмежуємо значення [-1, 1], щоб уникнути помилок точності float
        cos_a = max(min(cos_a, 1.0), -1.0)

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:

        # Кут між вектором та додатною віссю Y (0, 1)
        # Створюємо тимчасовий вектор, що вказує вгору по осі Y
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees: int) -> Vector:

        # Поворот вектора на задану кількість градусів
        radians = math.radians(degrees)

        # Формула повороту
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
