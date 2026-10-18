import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        add_x = self.x + other.x
        add_y = self.y + other.y
        return Vector(add_x, add_y)

    def __sub__(self, other: "Vector") -> "Vector":
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, Vector):
            formula_vect = (self.x * other.x) + (self.y * other.y)
            return formula_vect
        else:
            vec_x = self.x * other
            vec_y = self.y * other
        return Vector(vec_x, vec_y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return self._get_distance()

    def get_normalized(self) -> "Vector":
        norma = self._get_distance()
        return Vector(self.x / norma, self.y / norma)

    def _get_distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (self * vector) / (self._get_distance()
                                   * vector._get_distance())
        radiana_cos = math.acos(cos_a)
        return round(math.degrees(radiana_cos))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians_degrees = math.radians(degrees)
        new_x = (self.x * math.cos(radians_degrees)
                 - self.y * math.sin(radians_degrees))
        new_y = (self.x * math.sin(radians_degrees)
                 + self.y * math.cos(radians_degrees))
        return Vector(new_x, new_y)
