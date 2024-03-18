import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: ("Vector", float, int)) -> ("Vector", float, int):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return Vector(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.__mul__(other)
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        angle_in_radians = math.acos(dot_product / length_product)
        angle_in_degrees = math.degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def get_angle(self, vector_positive_y: tuple = (0, 1)) -> int:
        multiplication = self * Vector(*vector_positive_y)
        self_length = self.get_length()
        positive_y_length = Vector(*vector_positive_y).get_length()
        cos_angle = multiplication / (self_length * positive_y_length)
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: float) -> "Vector":
        angle_radians = math.radians(degrees)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
