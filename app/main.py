import math


class Vector:
    def __init__(self, coor_x: int, coor_y: int) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand "
                            f"type(s) for +: 'Distance' and {type(other)}")
        return Vector(
            coor_x=self.x + other.x,
            coor_y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand "
                            f"type(s) for -: 'Distance' and {type(other)}")
        return Vector(
            coor_x=self.x - other.x,
            coor_y=self.y - other.y
        )

    def __mul__(self, other: "Vector | int | float") -> "Vector | int | float":
        if not isinstance(other, (Vector, int, float)):
            raise TypeError(f"unsupported operand "
                            f"type(s) for *: 'Distance' and {type(other)}")

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            coor_x=self.x * other,
            coor_y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> "Vector":
        return cls(
            coor_x=end_point[0] - start_point[0],
            coor_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            coor_x=self.x / self.get_length(),
            coor_y=self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        coordinates_of_y = Vector(coor_x=0, coor_y=1)
        return self.angle_between(coordinates_of_y)

    def rotate(self, degrees: int | float) -> "Vector":
        radians = math.radians(degrees)
        return Vector(
            coor_x=(self.x * math.cos(radians)) - (self.y * math.sin(radians)),
            coor_y=(self.x * math.sin(radians)) + (self.y * math.cos(radians))
        )
