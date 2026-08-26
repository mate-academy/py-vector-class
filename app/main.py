from typing import Tuple
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        """Ініціалізує вектор з координатами (x, y), округленими до
        двох знаків після коми."""
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        """Додає два вектори і повертає новий екземпляр Vector як результат."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Віднімає один вектор від іншого і повертає новий екземпляр
        Vector як результат."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" or float) -> "Vector" or float:
        """Множить вектор на інший вектор або на число.

        При множенні на число повертає новий вектор, масштабований на це число.
        При множенні на інший вектор повертає їх скалярний добуток.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Скалярний добуток
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(f"Непідтримуваний тип операндів "
                            f"для *: 'Vector' і '{type(other)}'")

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point:
                                    Tuple[float, float]) -> "Vector":
        """Створює вектор, заданий двома точками."""
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        """Повертає довжину вектора."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        """Повертає нормалізовану копію вектора."""
        length = self.get_length()
        if length == 0:
            raise ValueError("Неможливо нормалізувати нульовий вектор.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        """Повертає кут в градусах між цим вектором та іншим."""
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        """Повертає кут в градусах між цим вектором та позитивною віссю Y,
        виміряний проти годинникової стрілки."""
        angle_radians = math.atan2(self.y, self.x)  # Обчислюємо кут
        # відносно осі X
        angle_degrees = math.degrees(angle_radians)

        # Коригуємо кут, щоб він був відносно осі Y і
        # вимірювався проти годинникової стрілки
        angle_from_y = 90 - angle_degrees
        if angle_from_y < 0:
            angle_from_y += 360

        # Обчислення кута проти
        # годинникової стрілки від осі Y
        angle_from_y_clockwise = 360 - angle_from_y if angle_from_y > 0 \
            else -angle_from_y

        return round(angle_from_y_clockwise)

    def rotate(self, degrees: int) -> "Vector":
        # Повертає новий вектор, повернутий на заданий кут в градусах.
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
