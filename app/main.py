import math


class Vector:
    def __init__(self, cordinate_x: int, cordinate_y: int) -> None:
        self.x = round(cordinate_x, 2)
        self.y = round(cordinate_y, 2)

    def __add__(self, other: int) -> any:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: int) -> any:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: int) -> any:
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            dop_product = self.x * other.x + self.y * other.y
            return dop_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: int, end_point: int
                                    ) -> any:
        cordinate_x = end_point[0] - start_point[0]
        cordinate_y = end_point[1] - start_point[1]
        return cls(cordinate_x, cordinate_y)

    def get_length(self) -> any:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> any:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            normalized_x = self.x / length
            normalized_y = self.y / length
            return Vector(normalized_x, normalized_y)

    def angle_between(self, other: int) -> any:
        dot_product = self.x * other.x + self.y * other.y
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        else:
            cos_theta = dot_product / length_product
            angle_in_radians = math.acos(cos_theta)
            angle_in_degrees = math.degrees(angle_in_radians)
            return round(angle_in_degrees)

    def get_angle(self) -> any:
        angle_in_radians = math.atan2((self.x), (self.y))
        angle_in_degrees = math.degrees(abs(angle_in_radians))
        return round(angle_in_degrees)

    def rotate(self, degrees: int) -> any:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
