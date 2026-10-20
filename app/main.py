from math import acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)
        self.coordinate_x = self.x
        self.coordinate_y = self.y

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(
            self,
            other: Vector | int | float) -> float | int | Vector:
        if isinstance(other, Vector):
            skalar_product = (self.x * other.x) + (self.y * other.y)
            return skalar_product
        else:
            new_vector_x = self.x * other
            new_vector_y = self.y * other
            return Vector(new_vector_x, new_vector_y)

    @classmethod
    def create_vector_by_two_points(
            cls: Vector,
            start_point: tuple,
            end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float | int:
        return ((self.x ** 2) + (self.y ** 2)) ** (0.5)

    def get_normalized(self) -> Vector:
        length_of_vector = self.get_length()
        normalized_x = round((self.x / length_of_vector), 2)
        normalized_y = round((self.y / length_of_vector), 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        product_of_vectors = self * other
        angle = product_of_vectors / (
            (self.get_length()) * (other.get_length()))
        value = degrees(acos(angle))
        return round(value)

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, degrees: int) -> Vector:
        cos_of_angle = cos(radians(degrees))
        sin_of_angle = sin(radians(degrees))
        new_x = self.x * cos_of_angle - self.y * sin_of_angle
        new_y = self.x * sin_of_angle + self.y * cos_of_angle
        return Vector(new_x, new_y)
