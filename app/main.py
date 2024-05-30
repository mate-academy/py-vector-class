import math


class Vector:
    def __init__(self, x_val: float, y_val: float) -> None:
        self.x_val = round(x_val, 2)
        self.y_val = round(y_val, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_val + other.x_val, self.y_val + other.y_val)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_val - other.x_val, self.y_val - other.y_val)

    def __mul__(self, other: float) -> "Vector" or float:
        if isinstance(other, Vector):
            return self.x_val * other.x_val + self.y_val * other.y_val
        else:
            return Vector(self.x_val * other, self.y_val * other)

    @classmethod
    def create_vector_by_val_two_points(cls,
                                        start_point: tuple,
                                        end_point: tuple) -> "Vector":

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_val ** 2 + self.y_val ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x_val / length, self.y_val / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_angle)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        angle_radians = math.atan2(self.x_val, self.y_val)
        angle_degrees = round(math.degrees(angle_radians))
        return abs(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x_val = (self.x_val * math.cos(radians)
                     - self.y_val * math.sin(radians))
        new_y_val = (self.x_val * math.sin(radians)
                     + self.y_val * math.cos(radians))
        return Vector(new_x_val, new_y_val)
