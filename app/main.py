import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        coord_x = self.x + other.x
        coord_y = self.y + other.y
        soma_vector = Vector(coord_x, coord_y)
        return soma_vector

    def __sub__(self, other: Vector) -> Vector:
        coord_x = self.x - other.x
        coord_y = self.y - other.y
        sub_vector = Vector(coord_x, coord_y)
        return sub_vector

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (float, int)):
            coord_x = self.x * other
            coord_y = self.y * other
            mul_vector = Vector(coord_x, coord_y)
            return mul_vector
        elif isinstance(other, Vector):
            dot_vector = (self.x * other.x) + (self.y * other.y)
            return dot_vector

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        displacement = cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )
        return displacement

    def get_length(self) -> float:
        length = math.sqrt((self.x ** 2) + (self.y ** 2))
        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        vector_normalized = (self.x / length, self.y / length)
        return Vector(*vector_normalized)

    def angle_between(self, vector: Vector) -> float:
        produto_vetores = self * vector
        length_self = self.get_length()
        length_vector = vector.get_length()
        coseno = (produto_vetores) / (length_self * length_vector)
        angle = round(math.degrees(math.acos(coseno)))
        return angle

    def get_angle(self) -> float:
        y_positivo = Vector(0, 1)
        angle_y = self.angle_between(y_positivo)
        return angle_y

    def rotate(self, degrees: float) -> Vector:
        rad = math.radians(degrees)
        sen = math.sin(rad)
        cos = math.cos(rad)
        new_coord_x = (self.x * cos) - (self.y * sen)
        new_coord_y = (self.x * sen) + (self.y * cos)
        return Vector(new_coord_x, new_coord_y)
