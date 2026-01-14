import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: any) -> object:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operation")

    def __sub__(self, other: any) -> object:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operation")

    def __mul__(self, other: any) -> any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> any:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return Vector(new_x, new_y)

    def get_length(self) -> float:
        length = math.sqrt(self.x * self.x + self.y * self.y)
        return length

    def get_normalized(self) -> object:
        length = self.get_length()
        if length == 0:
            raise ValueError("It is impossible to normalize the zero vector.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: any) -> float:
        if not isinstance(other, Vector):
            raise TypeError("Vector expected")

        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError("Unable to calculate angle with zero vector")
        cos_theta = dot_product / (length_self * length_other)
        angle_deg = math.degrees(math.acos(cos_theta))

        return round(angle_deg)

    def get_angle(self) -> float:
        angle_from_x = math.degrees(math.atan2(self.y, self.x))
        angle_from_y = (450 - angle_from_x) % 360
        if angle_from_y > 180:
            angle_from_y = 360 - angle_from_y
        return round(angle_from_y)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
