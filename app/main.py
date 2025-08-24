import math


class Vector:
    """Класс для работы с двумерными векторами."""

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        """Инициализация вектора с округлением координат до 2 знаков."""
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __repr__(self) -> str:
        """Строковое представление для отладки."""
        return f"Vector({self.x_coordinate}, {self.y_coordinate})"

    def __str__(self) -> str:
        """Красивое строковое представление вектора."""
        return f"({self.x_coordinate}, {self.y_coordinate})"

    def __add__(self, other: "Vector") -> "Vector":
        """Сумма двух векторов."""
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate
        )

    def __sub__(self, other: "Vector") -> "Vector":
        """Разность двух векторов."""
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate
        )

    def __mul__(self, other: int | float | "Vector") -> "Vector" | float:
        """
        Умножение вектора:
        - на число (возвращает новый вектор),
        - на другой вектор (скалярное произведение).
        """
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coordinate * other,
                self.y_coordinate * other
            )
        return (self.x_coordinate * other.x_coordinate
                + self.y_coordinate * other.y_coordinate)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        """Создание вектора по двум точкам."""
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        """Длина вектора."""
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2)

    def get_normalized(self) -> "Vector":
        """Нормализованный вектор."""
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            self.x_coordinate / length,
            self.y_coordinate / length
        )

    def angle_between(self, vector: "Vector") -> int:
        """Угол между текущим вектором и другим вектором (в градусах)."""
        dot_product = (self.x_coordinate * vector.x_coordinate
                       + self.y_coordinate * vector.y_coordinate)
        length_self = self.get_length()
        length_other = vector.get_length()
        cos_theta = dot_product / (length_self * length_other)
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        """Угол между вектором и положительной осью Y (в градусах)."""
        cos_theta = self.y_coordinate / self.get_length()
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: float) -> "Vector":
        """Поворот вектора на указанный угол (в градусах)."""
        rad = math.radians(degrees)
        new_x = (self.x_coordinate * math.cos(rad)
                 - self.y_coordinate * math.sin(rad))
        new_y = (self.x_coordinate * math.sin(rad)
                 + self.y_coordinate * math.cos(rad))
        return Vector(new_x, new_y)
