import math


class Vector:
    def __init__(self, x_point: float | int, y_point: float | int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> object:
        return cls(
            x_point=round(end_point[0] - start_point[0], 2),
            y_point=round(end_point[1] - start_point[1], 2)
        )

    def __add__(self, other: object) -> object:
        return Vector(
            x_point=round(self.x + other.x, 2),
            y_point=round(self.y + other.y, 2)
        )

    def __sub__(self, other: object) -> object:
        return Vector(
            x_point=round(self.x - other.x, 2),
            y_point=round(self.y - other.y, 2)
        )

    def __mul__(self, mult: object | float | int) -> object:
        if type(mult) in (float, int):
            return Vector(
                x_point=round(self.x * mult, 2),
                y_point=round(self.y * mult, 2)
            )
        return self.x * mult.x + self.y * mult.y

    def get_length(self) -> int | float:
        return math.sqrt(abs(self.y) ** 2 + abs(self.x) ** 2)

    def get_normalized(self) -> object:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other_vector: object) -> int:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        length_product = self.get_length() * other_vector.get_length()

        if length_product == 0:
            return 0

        cos_angle = dot_product / length_product
        angle_deg = math.degrees(math.acos(cos_angle))
        return math.ceil(angle_deg)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return int(abs(angle_deg))

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
