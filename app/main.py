import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate: float = round(x_coordinate, 2)
        self.y_coordinate: float = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coordinate + other.x_coordinate,
                      self.y_coordinate + other.y_coordinate)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coordinate - other.x_coordinate,
                      self.y_coordinate - other.y_coordinate)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate
                    + self.y_coordinate * other.y_coordinate)  # dot product
        else:
            return Vector(self.x_coordinate * other,
                          self.y_coordinate * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate
                         ** 2 + self.y_coordinate ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x_coordinate
                      / length, self.y_coordinate / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cosine = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cosine)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        angle_in_radians = (math.atan2
                            (self.y_coordinate, self.x_coordinate))
        angle_in_degrees = math.degrees(angle_in_radians)
        angle_from_positive_x_axis = angle_in_degrees
        if angle_from_positive_x_axis < 0:
            angle_from_positive_x_axis += 360
        return round(angle_from_positive_x_axis) % 360

    def rotate(self, degrees: int) -> "Vector":
        angle_in_radians = math.radians(degrees)
        new_x = (self.x_coordinate * math.cos(angle_in_radians)
                 - self.y_coordinate * math.sin(angle_in_radians))
        new_y = (self.x_coordinate * math.sin(angle_in_radians)
                 + self.y_coordinate * math.cos(angle_in_radians))
        return Vector(new_x, new_y)
