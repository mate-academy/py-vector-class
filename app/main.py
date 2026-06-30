import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float | int") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        lengths_product = self.get_length() * other.get_length()

        cosine_value = dot_product / lengths_product
        return int(round(math.degrees(math.acos(cosine_value))))

    def get_angle(self) -> int:
        cosine_value = self.y / self.get_length()
        return int(round(math.degrees(math.acos(cosine_value))))

    def rotate(self, degrees_value: float) -> "Vector":
        radians_value = math.radians(degrees_value)

        new_x_coordinate = (
            self.x * math.cos(radians_value)
            - self.y * math.sin(radians_value)
        )
        new_y_coordinate = (
            self.x * math.sin(radians_value)
            + self.y * math.cos(radians_value)
        )

        return Vector(new_x_coordinate, new_y_coordinate)
