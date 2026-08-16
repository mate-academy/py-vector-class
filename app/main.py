import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __str__(self) -> str:
        return f"Coordinate: {self.x}, coordinate: {self.y}"

    def __add__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(
            self,
            other_vector: "Vector | int | float"
    ) -> "Vector | float":
        if isinstance(other_vector, Vector):
            return self.x * other_vector.x + self.y * other_vector.y
        else:
            return Vector(self.x * other_vector, self.y * other_vector)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x_new_coord = round(end_point[0] - start_point[0], 2)
        y_new_coord = round(end_point[1] - start_point[1], 2)
        return cls(x_new_coord, y_new_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
