from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.point_x = round(point_x, 2)
        self.point_y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.point_x + other.point_x,
            self.point_y + other.point_y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.point_x - other.point_x,
            self.point_y - other.point_y
        )

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, Vector):
            return (self.point_x
                    * other.point_x
                    + self.point_y
                    * other.point_y)

        return Vector(
            self.point_x * other,
            self.point_y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.point_x ** 2 + self.point_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            self.point_x / length,
            self.point_y / length
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector

        cos_a = (
            dot_product
            / (self.get_length() * vector.get_length())
        )

        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degree: int) -> "Vector":
        rad = radians(degree)

        new_x = self.point_x * cos(rad) - self.point_y * sin(rad)
        new_y = self.point_x * sin(rad) + self.point_y * cos(rad)

        return Vector(new_x, new_y)
