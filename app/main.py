import math
from typing import Tuple, Union


class Vector:
    __slots__ = ("_coord_x", "_coord_y")

    def __init__(self, coord_x: float, coord_y: float) -> None:
        if not isinstance(
            coord_x, (int, float)) or not isinstance(
            coord_y, (int, float)
        ):
            raise TypeError(
                "As coordenadas do vetor devem ser números (int ou float).")

        self._coord_x: float = round(float(coord_x), 2)
        self._coord_y: float = round(float(coord_y), 2)

    @property
    def x(self) -> float:
        return self._coord_x

    @property
    def y(self) -> float:
        return self._coord_y

    def __add__(self, other_vector: "Vector") -> "Vector":
        if not isinstance(other_vector, Vector):
            return NotImplemented
        return Vector(
            self._coord_x + other_vector._coord_x,
            self._coord_y + other_vector._coord_y)

    def __sub__(self, other_vector: "Vector") -> "Vector":
        if not isinstance(other_vector, Vector):
            return NotImplemented
        return Vector(
            self._coord_x - other_vector._coord_x,
            self._coord_y - other_vector._coord_y)

    def __mul__(
            self,
            other_value: Union["Vector", int, float]
    ) -> Union[float, "Vector"]:
        if isinstance(other_value, Vector):
            return float((
                self._coord_x * other_value._coord_x)
                + (self._coord_y * other_value._coord_y))

        if isinstance(other_value, (int, float)):
            return Vector(
                self._coord_x * other_value,
                self._coord_y * other_value)

        return NotImplemented

    def __rmul__(
            self,
            other_value: Union[int, float]
    ) -> Union[float, "Vector"]:
        return self.__mul__(other_value)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> "Vector":
        try:
            x_start, y_start = start_point
            x_end, y_end = end_point
        except (TypeError, ValueError):
            raise TypeError(
                "Os pontos de entrada devem ser tuplas/iteráveis"
                " contendo exatamente (x, y).")

        return cls(x_end - x_start, y_end - y_start)

    def get_length(self) -> float:
        return float(math.hypot(self._coord_x, self._coord_y))

    def get_normalized(self) -> "Vector":
        # Correção do Alerta: Garantia estrita de tipo primitivo para divisão
        total_length: float = float(self.get_length())

        if total_length == 0:
            raise ValueError(
                "Não é possível normalizar "
                "um vetor nulo (comprimento zero).")

        return Vector(
            self._coord_x / total_length,
            self._coord_y / total_length)

    def angle_between(self, other_vector: "Vector") -> int:
        if not isinstance(other_vector, Vector):
            raise TypeError("Só é possível calcular"
                            " o ângulo entre dois objetos Vector.")

        length_self: float = float(self.get_length())
        length_other: float = float(other_vector.get_length())

        if length_self == 0 or length_other == 0:
            raise ValueError(
                "Não é possível calcular o ângulo com um vetor nulo.")

        # Forçamos a saída do produto escalar
        # aqui a ser reconhecida como float pelo linter
        dot_product_value = self * other_vector
        if isinstance(dot_product_value, Vector):
            raise TypeError(
                "A multiplicação entre dois vetores "
                "deveria retornar um número escalar.")

        cos_angle: float = float(
            dot_product_value) / (length_self * length_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))

        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length_self: float = float(self.get_length())
        if length_self == 0:
            raise ValueError("Não é possível "
                             "calcular o ângulo de um vetor nulo.")

        cos_angle: float = self._coord_y / length_self
        cos_angle = max(-1.0, min(1.0, cos_angle))

        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, rotation_degrees: int) -> "Vector":
        if not isinstance(rotation_degrees, (int, float)):
            raise TypeError("O valor de rotação deve ser um número em graus.")

        angle_radians: float = math.radians(rotation_degrees)
        cos_angle: float = math.cos(angle_radians)
        sin_angle: float = math.sin(angle_radians)

        rotated_x: float = ((self._coord_x * cos_angle)
                            - (self._coord_y * sin_angle))
        rotated_y: float = ((self._coord_x * sin_angle)
                            + (self._coord_y * cos_angle))
        return Vector(rotated_x, rotated_y)

    def __repr__(self) -> str:
        return f"Vector(x={self._coord_x}, y={self._coord_y})"
