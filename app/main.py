import math


class Vector:

    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: int) -> tuple:
        return Vector(
            x_coord=round(self.x + other.x, 2),
            y_coord=round(self.y + other.y, 2),
        )

    def __sub__(self, other: int) -> tuple:
        return Vector(
            x_coord=round(self.x - other.x, 2),
            y_coord=round(self.y - other.y, 2),
        )

    def __mul__(self, other: int) -> tuple:
        if isinstance(other, (float, int)):
            return Vector(
                x_coord=round(self.x * other, 2),
                y_coord=round(self.y * other, 2),
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> tuple:

        x_coord = round(end_point[0] - start_point[0], 2)
        y_coord = round(end_point[1] - start_point[1], 2)
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> tuple:
        x_coord = round(self.x / (self.x ** 2 + self.y ** 2) ** 0.5, 2)
        y_coord = round(self.y / (self.x ** 2 + self.y ** 2) ** 0.5, 2)
        return Vector(x_coord, y_coord)

    def angle_between(self, other: float) -> float:
        mult = self.x * other.x + self.y * other.y
        length_1 = self.get_length()
        length_2 = other.get_length()

        cos_a = mult / (length_1 * length_2)

        cos_a = max(-1.0, min(1.0, cos_a))
        result = math.ceil(math.degrees(math.acos(cos_a)))

        return result

    def get_angle(self) -> float:
        return int(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degree: int) -> tuple:
        x_coord = round(self.x * math.cos(math.radians(degree))
                        - self.y * math.sin(math.radians(degree)), 2)

        y_coord = round(self.x * math.sin(math.radians(degree))
                        + self.y * math.cos(math.radians(degree)), 2)

        return Vector(x_coord, y_coord)
