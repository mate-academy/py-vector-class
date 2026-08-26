import math


class Vector:
    def __init__(self, first_x: int, second_y: int) -> None:
        self.x = round(first_x, 2)
        self.y = round(second_y, 2)

    def __add__(self, other: None) -> None:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: None) -> None:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: None) -> None:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls
            , start_point: tuple
            , end_point: tuple
    ) -> None:
        first = end_point[0] - start_point[0]
        second = end_point[1] - start_point[1]
        return cls(first, second)

    def get_length(self) -> None:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> None:
        lenght = self.get_length()
        return Vector(round(self.x / lenght, 2), round(self.y / lenght, 2))

    def angle_between(self, other: None) -> None:
        """Обчислює кут між поточним вектором і іншим вектором у градусах."""
        # Скалярний добуток
        dot = self.__mul__(other)
        # Довжини векторів
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        # Перевірка, щоб не було ділення на 0
        # Косинус кута
        cos_angle = dot / (magnitude_self * magnitude_other)
        # Обмеження косинуса в діапазоні [-1, 1] (уникнення похибок)
        cos_angle = max(-1, min(1, cos_angle))
        # Кут у радіанах
        angle_radians = math.acos(cos_angle)
        # Кут у градусах
        return round(math.degrees(angle_radians))

    # Повертає кут між поточним вектором і позитивною віссю Y.
    def get_angle(self) -> None:
        """Обчислює кут між вектором і позитивною віссю Y."""
        magnitude_self = self.get_length()
        # Косинус кута
        cos_angle = self.y / magnitude_self
        # Обмеження косинуса в діапазоні [-1, 1]
        cos_angle = max(-1, min(1, cos_angle))
        # Кут у радіанах
        angle_radians = math.acos(cos_angle)
        # Кут у градусах
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, angle: int) -> None:
        angle_radians = math.radians(angle)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(round(new_x, 2), round(new_y, 2))
