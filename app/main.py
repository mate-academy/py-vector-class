import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Operands must be of type Vector for addition")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Operands must be of type Vector for subtraction")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError(
            "Operands must be Vector or scalar (int/float) for multiplication"
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]
                                    ) -> "Vector":
        x_component = end_point[0] - start_point[0]
        y_component = end_point[1] - start_point[1]
        return cls(x_component, y_component)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError(
                "Operand must be of type Vector for angle calculation"
            )
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return 0
        cosine_angle = dot_product / magnitude_product
        cosine_angle = max(-1.0, min(1.0, cosine_angle))
        angle = math.degrees(math.acos(cosine_angle))
        return round(angle)

    def get_angle(self) -> int:
        standard_angle = math.degrees(math.atan2(self.y, self.x))

        # Converte para o sistema com 0° no norte e sentido horário
        test_angle = (90 - standard_angle) % 360

        # Ajustes específicos
        if standard_angle < -90:  # Terceiro quadrante
            test_angle = 180 + (180 - test_angle)
        elif standard_angle > 90:  # Segundo quadrante
            test_angle = 360 - test_angle

        return round(test_angle)

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        cos_angle = math.cos(angle_rad)
        sin_angle = math.sin(angle_rad)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
