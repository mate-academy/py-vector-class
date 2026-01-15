import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector | int | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return Vector(
                self.x_coord + other.x_coord,
                self.y_coord + other.y_coord,
            )
        return Vector(self.x_coord + other, self.y_coord + other)

    def __sub__(self, other: "Vector | int | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return Vector(
                self.x_coord - other.x_coord,
                self.y_coord - other.y_coord,
            )
        return Vector(self.x_coord - other, self.y_coord - other)

    def __mul__(self, other: "Vector | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return (
                self.x_coord * other.x_coord + self.y_coord * other.y_coord
            )
        return Vector(self.x_coord * other, self.y_coord * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x_coord**2 + self.y_coord**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        length_self = self.get_length()
        length_vector = vector.get_length()

        if length_self == 0 or length_vector == 0:
            return 0

        cos_theta = dot_product / (length_self * length_vector)
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self) -> int:
        if self.x_coord == 0 and self.y_coord == 0:
            return 0

        angle = math.degrees(math.atan2(-self.x_coord, self.y_coord))

        return round(angle + 360 if angle < 0 else angle)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        x_new = round(
            self.x_coord * math.cos(radians)
            - self.y_coord * math.sin(radians),
            2,
        )
        y_new = round(
            self.x_coord * math.sin(radians)
            + self.y_coord * math.cos(radians),
            2,
        )
        return Vector(x_new, y_new)

    def __repr__(self) -> str:
        return f"Vector({self.x_coord}, {self.y_coord})"
