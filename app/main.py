import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: float) -> float:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: float) -> None:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: float) -> None:
        if isinstance(other, (int, float)):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: float,
                                    end_point: float
                                    ) -> None:
        return cls(end_point[0] - start_point[0], end_point[1]
                   - start_point[1])

    def get_length(self) -> float:
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> None:
        get_length = Vector.get_length(self)
        return Vector(
            x_coord=self.x / get_length,
            y_coord=self.y / get_length
        )

    def angle_between(self, vector: tuple) -> int:
        sum_a = self.x * vector.x + self.y * vector.y
        sum_b = (self.x ** 2 + self.y ** 2) ** 0.5
        sum_c = (vector.x ** 2 + vector.y ** 2) ** 0.5
        cos_a = sum_a / (sum_b * sum_c)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        sum_a = self.y ** 2
        sum_b = (self.x ** 2 + self.y ** 2) ** 0.5
        sum_c = (self.y ** 2) ** 0.5
        cos_a = sum_a / (sum_b * sum_c)
        if self.y >= 0:
            return round(math.degrees(math.acos(cos_a)))
        return 90 + (90 - round(math.degrees(math.acos(cos_a))))

    def get_angle1(self) -> int:
        sum_a = self.y ** 2
        sum_b = (self.x ** 2 + self.y ** 2) ** 0.5
        sum_c = (self.y ** 2) ** 0.5
        cos_a = sum_a / (sum_b * sum_c)
        if self.y >= 0:
            return math.degrees(math.acos(cos_a))
        return 90 + (90 - math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> float:
        if self.x > 0 and self.y > 0:
            return Vector(
                x_coord=self.get_length() * math.cos(math.radians(
                    (90 - self.get_angle1()) + angle)),
                y_coord=self.get_length() * math.sin(math.radians(
                    (90 - self.get_angle1()) + angle))
            )

        return Vector(
            x_coord=self.get_length() * math.cos(math.radians(
                (self.get_angle1() + 90) + angle)),
            y_coord=self.get_length() * math.sin(math.radians(
                (self.get_angle1() + 90) + angle))
        )
